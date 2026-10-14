import pandas as pd
import geopandas as gpd
import numpy as np

# Wczytanie oczyszczonych danych z poprzedniego kroku
df_final = pd.read_csv("wyniki_z_metadanymi.csv")

print("Konwertowanie GeoJSON do CSV...")
gdf_here = gpd.read_file('Bulgaria_spdlmt_signs.geojson')

gdf_here['lon'] = gdf_here.geometry.x
gdf_here['lat'] = gdf_here.geometry.y

gdf_here = gdf_here.rename(columns={
    'node_id': '_id',          # Często w JSONie jest 'id', a my potrzebujemy '_id'
    'speed_limit': 'speed_lmt' # Sprawdź w JSONie jak nazywa się limit
})

final_columns = ['_id', 'speed_lmt', 'bearing', 'lat', 'lon']
available_cols = [c for c in final_columns if c in gdf_here.columns]
df_signs = pd.DataFrame(gdf_here[available_cols])
df_signs.to_csv('signs.csv', index=False)
print(f"Sukces! Plik signs.csv gotowy. Liczba znaków: {len(df_signs)}")

# --- PRZYGOTOWANIE GEOGRAFICZNE ---
# 1. Zamieniamy Twoje wyniki YOLO na mapę (metry - EPSG:32635 dla Bułgarii)
gdf_yolo = gpd.GeoDataFrame(
    df_final, 
    geometry=gpd.points_from_xy(df_final.lon, df_final.lat), 
    crs="EPSG:4326"
).to_crs(epsg=32635)

# 2. Zamieniamy bazę HERE na mapę
gdf_here = gpd.GeoDataFrame(
    df_signs, 
    geometry=gpd.points_from_xy(df_signs.lon, df_signs.lat), 
    crs="EPSG:4326"
).to_crs(epsg=32635)

# --- 1. ODŚWIEŻENIE I RZUTOWANIE ---
yolo_m = gdf_yolo.to_crs(epsg=32635).copy()
here_m = gdf_here.to_crs(epsg=32635).copy()

# --- 2. MOSTEK: POWIĄZANIE YOLO Z MAPĄ (SJOIN) ---
here_m_buff = here_m.copy()
here_m_buff['geometry'] = here_m_buff.buffer(50) # Bufor 50m dla dopasowań

# Łączymy wykrycia z bazą znaków
matches = gpd.sjoin(yolo_m, here_m_buff.reset_index(), how='inner', predicate='within')

if not matches.empty:
    # Agregacja detekcji po ID znaku
    id_col = '_id' if '_id' in matches.columns else 'index_right'
    
    detected = matches.groupby(id_col).agg({
        'sign_type': lambda x: x.mode()[0] if not x.empty else None,
        'confidence': 'mean',
        'file_name': 'count'
    }).reset_index()
    detected.columns = ['ID_JOIN', 'speed_lmt_yolo', 'avg_conf', 'n_photos']
    
    # FIX ID: usuwamy .0 i robimy string
    detected['ID_JOIN'] = pd.to_numeric(detected['ID_JOIN'], errors='coerce').fillna(0).astype(int).astype(str)
else:
    detected = pd.DataFrame(columns=['ID_JOIN', 'speed_lmt_yolo', 'avg_conf', 'n_photos'])

# --- 3. AUDYT: WSZYSTKIE ZNAKI NA TRASIE (KORYTARZ) ---
corridor = yolo_m.buffer(80).union_all() if hasattr(yolo_m.buffer(80), 'union_all') else yolo_m.buffer(80).unary_union
passed_signs = here_m[here_m.geometry.intersects(corridor)].copy().reset_index()

# Przygotowanie ID w bazie HERE
passed_signs['ID_JOIN'] = pd.to_numeric(passed_signs['_id'], errors='coerce').fillna(0).astype(int).astype(str)

# --- 4. WIELKIE ŁĄCZENIE (LEFT JOIN) ---
final_report = pd.merge(passed_signs, detected, on='ID_JOIN', how='left')

# --- 5. WERDYKT I STATUSY ---
final_report['speed_lmt'] = pd.to_numeric(final_report['speed_lmt'], errors='coerce').astype('Int64')
final_report['speed_lmt_yolo'] = pd.to_numeric(final_report['speed_lmt_yolo'], errors='coerce').astype('Int64')

def get_final_status(row):
    if pd.isna(row['speed_lmt_yolo']): 
        return "MISSING"
    return "OK" if row['speed_lmt'] == row['speed_lmt_yolo'] else "ERROR"

final_report['status'] = final_report.apply(get_final_status, axis=1)

# --- 6. STATYSTYKI I CONFIDENCE SCORE ---
print("=" * 40)
print("FINALNY RAPORT AUDYTU")
print("=" * 40)
print(f"Łączna liczba znaków na trasie: {len(final_report)}")
print("-" * 20)
print("PODSUMOWANIE STATUSÓW:")
print(final_report['status'].value_counts())
print("-" * 20)

conf_stats = final_report.groupby('status')['avg_conf'].mean()
print("ŚREDNI CONFIDENCE SCORE:")
for status, score in conf_stats.items():
    score_display = f"{score:.2%}" if not pd.isna(score) else "N/A"
    print(f"- {status}: {score_display}")

print("=" * 40)

final_report.to_csv("Raport_Audytu_HERE_Sofia.csv", index=False)
print("Pliki zostały zapisane pomyślnie!")

# ============================================================
# INTEGRACJA Z DANYMI PROBE (BGR_HPD_week_1.csv)
# ============================================================
probe = pd.read_csv("BGR_HPD_week_1.csv")
roads = gpd.read_file('Bulgaria_spdlmt_roads.geojson')

# --- 1. PRZYGOTOWANIE DANYCH PROBE ---
gdf_probe = gpd.GeoDataFrame(
    probe, 
    geometry=gpd.points_from_xy(probe.longitude, probe.latitude), 
    crs="EPSG:4326"
).to_crs(epsg=32635)

# --- 2. PRZYGOTOWANIE BUFORÓW (precyzyjne uderzenie w pas ruchu) ---
signs_to_check = final_report.to_crs(epsg=32635).copy()
signs_to_check['buffer_geometry'] = signs_to_check.geometry.buffer(2.5) 
signs_buffer_gdf = signs_to_check.set_geometry('buffer_geometry')

# --- 3. SPATIAL JOIN ---
probe_matches = gpd.sjoin(
    gdf_probe, 
    signs_buffer_gdf[['ID_JOIN', 'bearing', 'status', 'speed_lmt', 'speed_lmt_yolo', 'avg_conf', 'buffer_geometry']], 
    how='inner'
)

# --- 4. PRECYZYJNY FILTR KIERUNKU (30 stopni) ---
def is_correct_direction_tight(probe_head, sign_bear):
    if pd.isna(probe_head) or pd.isna(sign_bear): return False
    diff = abs(probe_head - sign_bear)
    return (diff <= 30) or (diff >= 330)

probe_matches['valid_dir'] = probe_matches.apply(
    lambda x: is_correct_direction_tight(x['heading'], x['bearing']), axis=1
)
probe_valid = probe_matches[probe_matches['valid_dir'] == True].copy()

# --- 5. INTELIGENTNA AGREGACJA (Mediana + Licznik punktów) ---
probe_stats = probe_valid.groupby('ID_JOIN').agg(
    avg_probe_speed=('speed', 'median'),
    probe_count=('speed', 'count')
).reset_index()

# Filtr wiarygodności: jeśli mamy mniej niż 3 auta, nie wyciągamy wniosków
probe_stats.loc[probe_stats['probe_count'] < 3, 'avg_probe_speed'] = np.nan

# --- 6. BUDOWA FINALNEGO RAPORTU ---
final_audit = pd.merge(final_report, probe_stats[['ID_JOIN', 'avg_probe_speed']], on='ID_JOIN', how='left')

# --- 7. LOGIKA EXISTENCE CONFIDENCE SCORE (ECS) ---
def calculate_existence_score(row):
    conf = row['avg_conf'] if pd.notna(row['avg_conf']) else 0.1
    
    if row['status'] == 'OK':
        # Jeśli prędkość pasuje do mapy, podbijamy pewność rekordu
        if pd.notna(row['avg_probe_speed']) and abs(row['avg_probe_speed'] - row['speed_lmt']) < 10:
            return min(conf + 0.05, 1.0)
        return conf
    
    elif row['status'] == 'ERROR':
        # Jeśli Probe potwierdza błąd (czyli auta jadą jak widzi YOLO, a nie jak chce mapa)
        if pd.notna(row['avg_probe_speed']) and abs(row['avg_probe_speed'] - row['speed_lmt_yolo']) < 15:
            return max(1 - conf - 0.2, 0.01) # Rekord HERE jest niemal na pewno błędny
        return 1 - conf
    
    else: # MISSING
        # Jeśli znak zniknął, a auta pędzą szybciej niż powinny
        if pd.notna(row['avg_probe_speed']) and row['avg_probe_speed'] > (row['speed_lmt'] + 10):
            return 0.05
        return 0.2

final_audit['existence_score'] = final_audit.apply(calculate_existence_score, axis=1)

# 1. Konwersja na stopnie (WGS84)
final_audit_wgs84 = final_audit.to_crs(epsg=4326)

# 2. Wyciągnięcie lat/lon
final_audit_wgs84['lat'] = final_audit_wgs84.geometry.y
final_audit_wgs84['lon'] = final_audit_wgs84.geometry.x

# 3. Wybór kolumn (dodaliśmy 'bearing')
output_table = final_audit_wgs84[[
    '_id', 
    'lat', 
    'lon', 
    'bearing',  # <--- To jest Twoja kolumna z kierunkiem znaku
    'speed_lmt', 
    'speed_lmt_yolo', 
    'avg_probe_speed', 
    'status', 
    'existence_score'
]]

# 4. Wyświetlenie i zapis
print("Finalna tabela z namiarami (bearing):")
print(output_table.head(20))

output_table.to_csv("HERE_Final_Audit_Data_with_Bearing.csv", index=False)

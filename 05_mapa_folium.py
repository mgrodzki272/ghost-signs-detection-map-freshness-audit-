import pandas as pd
import folium
from folium import plugins
import requests
import io
import numpy as np

# 1. WCZYTANIE DANYCH (Zmieniono na 'df' i dodano czyszczenie nagłówków)
df = pd.read_csv("HERE_Final_Audit_Data_with_Bearing.csv")
df.columns = df.columns.str.strip()  # Usuwa spacje z nazw kolumn (kluczowe!)

# 2. KONFIGURACJA API
HERE_API_KEY = "WPISZ_SWOJ_KLUCZ_API" 

def get_address(lat, lon):
    url = f"https://revgeocode.search.hereapi.com/v1/revgeocode?at={lat},{lon}&lang=en-US&apiKey={HERE_API_KEY}"
    try:
        r = requests.get(url, timeout=5)
        data = r.json()
        return data['items'][0]['address']['label'] if 'items' in data and data['items'] else "Sofia, Bulgaria"
    except: return "Location Lookup Unavailable"

# Pobieranie adresów
print("Pobieranie adresów z HERE API...")
df['address'] = df.apply(lambda r: get_address(r['lat'], r['lon']), axis=1)

# 3. GENEROWANIE MAPY
# Centrowanie mapy na średnich współrzędnych z Twojego pliku
m = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], zoom_start=14, tiles='cartodbpositron')

status_colors = {'OK': '#2ecc71', 'ERROR': '#e74c3c', 'MISSING': '#f1c40f'}

for _, row in df.iterrows():
    # Pobieranie koloru na podstawie statusu (teraz zadziała!)
    current_status = str(row['status']).strip()
    color = status_colors.get(current_status, '#3498db') # domyślny niebieski jeśli status jest inny
    score = round(row['existence_score'], 2)
    
    # Zaawansowany Tooltip HTML
    tooltip_html = f"""
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid {color}; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:{color}; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>{current_status}</span>
            <span style="font-size:10px; opacity:0.8;">ID: {int(row['_id'])}</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> {row['address']}
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">{int(row['speed_lmt'])}</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:{color};">{int(row['speed_lmt_yolo']) if pd.notna(row['speed_lmt_yolo']) else '—'}</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">{int(row['avg_probe_speed']) if pd.notna(row['avg_probe_speed']) else '—'}</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>{int(score*100)}%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:{score*100}%; background:{color}; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    """

    # Marker ze strzałką kierunkową (Bearing)
    folium.Marker(
        location=[row['lat'], row['lon']],
        icon=folium.DivIcon(
            html=f'''<div style="transform: rotate({row["bearing"]}deg); color:{color};">
                        <i class="fa fa-location-arrow" style="font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);"></i>
                    </div>''',
            icon_size=(30, 30), icon_anchor=(15, 15)
        ),
        tooltip=folium.Tooltip(tooltip_html, sticky=False)
    ).add_to(m)

# Dodanie Legendy
legend_html = f'''
     <div style="position: fixed; bottom: 50px; left: 50px; width: 180px; height: 110px; 
     border:2px solid grey; z-index:9999; font-size:14px; background-color:white;
     opacity: 0.85; padding: 10px; border-radius: 10px; font-family: 'Segoe UI', sans-serif;">
     <b style="font-size:15px;">Map Audit Summary</b><br>
     <i class="fa fa-location-arrow" style="color:#2ecc71"></i>&nbsp; Verified (OK)<br>
     <i class="fa fa-location-arrow" style="color:#e74c3c"></i>&nbsp; Attr Error (ERROR)<br>
     <i class="fa fa-location-arrow" style="color:#f1c40f"></i>&nbsp; Sign Missing
     </div>
     '''
m.get_root().html.add_child(folium.Element(legend_html))

# 4. ZAPIS
m.save("HERE_Audit_Final_Map.html")
print("Sukces! Mapa 'HERE_Audit_Final_Map.html' jest gotowa.")

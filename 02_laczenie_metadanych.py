"""
Łączenie danych meta z wykrytymi znakami oraz czyszczenie
"""
import pandas as pd

meta1 = pd.read_csv("HT412_1765878407_metadata.csv")
meta2 = pd.read_csv("HT412_1765889650_metadata.csv")
meta3 = pd.read_csv("HT412_1765955305_metadata.csv")  # ← zmień nazwę
meta  = pd.concat([meta1, meta2, meta3], ignore_index=True)
det = pd.read_csv("wyniki_detekcji.csv")

det["eventId"] = det["file_name"].str.split("-").str[1]

det["eventId"]  = det["eventId"].astype(str).str.strip()
meta["eventId"] = meta["eventId"].astype(str).str.strip()

wynik = det.merge(meta, on="eventId", how="left")

wynik.to_csv("wyniki_z_metadanymi.csv", index=False)
df = pd.read_csv("wyniki_z_metadanymi.csv")

df["sign_type"] = df["sign_type"].str.extract(r"(\d+)").astype(float).astype("Int64")

df.to_csv("wyniki_z_metadanymi.csv", index=False)
print("Gotowe!")
print(df["sign_type"].value_counts())
df.to_csv("gotowedane_z_metadanymi.csv", index=False)

# --- Czyszczenie ---
df_clean = df.dropna(subset=['sign_type']).copy()

# 3. Wybór tylko potrzebnych kolumn
# To są kolumny, które "robią robotę" w dalszych krokach:
needed_columns = [
    'eventId',       # Klucz łączący
    'file_name',     # Dowód wizualny
    'sign_type',     # Wynik z YOLO (liczba)
    'confidence',    # Pewność modelu
    'lat', 'lon',    # Współrzędne GPS
    'front_bearing'  # Kierunek jazdy (do Kroku 3)
]

df_final = df_clean[needed_columns]
df_final.to_csv("wyniki_z_metadanymi.csv", index=False)

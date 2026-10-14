[HERE_Audit_Final_Map.html](https://github.com/user-attachments/files/33426184/HERE_Audit_Final_Map.html)# Map Freshness Audit — Multi-Modal Spatial & Vision Pipeline

> Automated pipeline for detecting outdated road signage ("Ghost Signs") and attribute discrepancies in navigation databases by combining **Tiled YOLOv8 Computer Vision** with **GPS Probe Telemetry** and **Precision GIS Filtering**.

[![Presentation PDF](https://img.shields.io/badge/Presentation-Full_Slide_Deck_(PDF)-red?style=for-the-badge&logo=adobeacrobatreader)](./map-freshness-audit-presentation.pdf.pdf)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Tiled_Inference-00FFFF?style=for-the-badge)
![GeoPandas](https://img.shields.io/badge/GeoPandas-EPSG:32635-139C5A?style=for-the-badge)
![Folium](https://img.shields.io/badge/Folium-Interactive_GIS-77B829?style=for-the-badge)

> ⚠️ **Data Privacy & Licensing Note:** This project was developed by team **Geologic** during the **HERE Technologies Hackathon (May 2026)** at AGH University of Krakow. Due to data licensing agreements, proprietary datasets (raw street-level imagery, HERE Probe Data, and road network GeoJSONs) are excluded from this repository.

---

## 🎯 Cel projektu: Problem „Ghost Signs”
Bazy nawigacyjne często zawierają nieaktualne ograniczenia prędkości – znaki fizycznie znikają po remontach dróg, ale pozostają w bazie danych przez miesiące. Powoduje to błędy w systemach **Intelligent Speed Assistance (ISA)** i niepotrzebne hamowanie autonomicznych systemów.

Nasz potok (**Double-Check Pipeline**) automatycznie weryfikuje bazę mapową, zestawiając ją z **detekcją obrazu (YOLOv8 + kafelkowanie)** oraz **rzeczywistym zachowaniem kierowców (GPS Probe Data)**.

---

## 📊 Przykładowe wyniki audytu (Interaktywna mapa Folium)

Poniższe karty z wygenerowanej mapy pokazują fuzję danych (**Map Limit** z bazy HERE, detekcję **YOLO** ze zdjęć oraz medianę prędkości kierowców **Probe Speed**) wraz z obliczonym wskaźnikiem wiarygodności **Existence Score**:

<p align="center">
  <img src="https://github.com/user-attachments/assets/3b8fdb16-131a-452f-a56d-64d2d308f38b" alt="wynik1" width="31%" />
  <img src="https://github.com/user-attachments/assets/82b08224-d7f7-4c5e-8ce5-d7ad78effc2e" alt="wynik3" width="31%" />
  <img src="https://github.com/user-attachments/assets/07800b02-e0f0-4b38-87f9-37c54e9fca20" alt="wynik2" width="31%" />
</p>

---

## 📂 Zawartość repozytorium

* 📄 **[`map-freshness-audit-presentation.pdf`](./map-freshness-audit-presentation.pdf)** – Pełna prezentacja projektu z wizualizacjami i opisem architektury.
* 💻 **[`01_detekcja_yolo.py`](./01_detekcja_yolo.py)** – Kafelkowanie zdjęć ulicznych ($640 \times 640$, overlap $10\%$), odrzucanie jednolitych kafli nieba/asfaltu (`PROG_WARIANCJI = 8.0`), detekcja YOLOv8 oraz własna implementacja algorytmu NMS (`apply_nms`).
* 🔗 **[`02_laczenie_metadanych.py`](./02_laczenie_metadanych.py)** – Łączenie wyników detekcji z metadanymi GPS i kątem kamery (`front_bearing`) po kluczu `eventId`.
* 📐 **[`03_confidence_scores.py`](./03_confidence_scores.py)** – Obliczanie dystansu sferycznego (Haversine) w buforze $45\text{ m}$, filtrowanie kąta (`MAX_BEARING_DIFF = 60`) i wyliczanie ważonego wskaźnika pewności dla znaków.
* 🌍 **[`04_audyt_geopandas_probe.py`](./04_audyt_geopandas_probe.py)** – Geoprzetwarzanie w układzie metrycznym **UTM (`EPSG:32635`)**, wyznaczanie korytarza trasy ($80\text{ m}$), łączenie przestrzenne (`sjoin`) z telemetrią `Probe Data` w pasie ruchu oraz wyliczanie wieloźródłowego **Existence Confidence Score (ECS)**.
* 🗺️ **[`05_mapa_folium.py`](./05_mapa_folium.py)** – Generator interaktywnej mapy HTML w `Folium` (`HERE_Interactive_Audit_Map.html`) z oknami popup podsumowującymi audyt każdego znaku (`OK`, `ERROR`, `MISSING`).

---

## 👥 Zespół Geologic
* **Mateusz Grodzki**
* **Kamila Bodziony**
* **Aleksandra Staroch**

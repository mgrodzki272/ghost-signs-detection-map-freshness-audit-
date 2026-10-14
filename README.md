# Hackathon Project
⚠️ Data Privacy Note: This project was developed during the HERE Technologies Hackathon. Due to data licensing and confidentiality agreements, proprietary datasets (HERE Probe Data) are not included in this repository. Only the processing pipeline, model inference logic (YOLOv8 + SAHI), and system architecture are presented.
# Map Freshness Audit — Multi-Modal Spatial & Vision Pipeline

> Automated pipeline for detecting outdated road signage ("Ghost Signs") and attribute discrepancies in navigation databases by combining **Tiled YOLOv8 / SAHI Computer Vision** with **GPS Probe Telemetry** and **Precision GIS Filtering**.

[![Presentation PDF](https://img.shields.io/badge/Presentation-Full_Slide_Deck_(PDF)-red?style=for-the-badge&logo=adobeacrobatreader)](./map-freshness-audit-presentation.pdf)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Tiled_Inference-00FFFF?style=for-the-badge)
![GeoPandas](https://img.shields.io/badge/GeoPandas-EPSG:32635-139C5A?style=for-the-badge)
![Folium](https://img.shields.io/badge/Folium-Interactive_GIS-77B829?style=for-the-badge)

> ⚠️ **Data Privacy & Licensing Note:** This project was developed by team **Geologic** during the **HERE Technologies Hackathon (May 2026)** at AGH University of Krakow. Due to data licensing agreements, proprietary datasets (raw street-level imagery, HERE Probe Data, and road network GeoJSONs) and API keys are excluded from this repository. Only the processing pipeline, spatial algorithms, and aggregated visual case studies are presented.

---

## 🎯 Problem Statement: The "Ghost Sign" Risk
Navigation databases frequently suffer from outdated speed limit attributes—physical signs are removed or modified after roadworks, but remain in the digital map for months. This creates critical friction for **Intelligent Speed Assistance (ISA)** and autonomous driving systems, leading to phantom braking and loss of driver trust.

Instead of relying on manual reports, our system implements a continuous **Double-Check Pipeline**: validating what the map database states against both **street-level computer vision** and **real-world driver behavior (GPS telemetry)**.

---

## 🏗️ System Architecture & Pipeline

```text
[Street-Level Imagery] ──► (01. Tiled YOLOv8 + Empty-Tile Skip + NMS)
                                      │
                                      ▼
[Image GPS Metadata]   ──► (02. EventId Integration & Label Parsing)
                                      │
                                      ▼
[Map Signs + GPS Probes]─► (03. UTM EPSG:32635 Spatial Join + Directional Gate + ECS)
                                      │
                                      ▼
                           (04. Folium Interactive HTML Audit Map)

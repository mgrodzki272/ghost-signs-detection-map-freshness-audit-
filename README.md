[HERE_Audit_Final_Map.html](https://github.com/user-attachments/files/33426184/HERE_Audit_Final_Map.html)# Map Freshness Audit — Multi-Modal Spatial & Vision Pipeline

> Automated pipeline for detecting outdated road signage ("Ghost Signs") and attribute discrepancies in navigation databases by combining **Tiled YOLOv8 Computer Vision** with **GPS Probe Telemetry** and **Precision GIS Filtering**.
[Uploading HERE_Audi<!DOCTYPE html>
<html>
<head>
    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_89e9a55d2667377437c1b2742a8c082a {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>

            <style>html, body {
                width: 100%;
                height: 100%;
                margin: 0;
                padding: 0;
            }
            </style>

            <style>#map {
                position:absolute;
                top:0;
                bottom:0;
                right:0;
                left:0;
                }
            </style>

            <script>
                L_NO_TOUCH = false;
                L_DISABLE_3D = false;
            </script>

        
</head>
<body>
    
    
     <div style="position: fixed; bottom: 50px; left: 50px; width: 180px; height: 110px; 
     border:2px solid grey; z-index:9999; font-size:14px; background-color:white;
     opacity: 0.85; padding: 10px; border-radius: 10px; font-family: 'Segoe UI', sans-serif;">
     <b style="font-size:15px;">Map Audit Summary</b><br>
     <i class="fa fa-location-arrow" style="color:#2ecc71"></i>&nbsp; Verified (OK)<br>
     <i class="fa fa-location-arrow" style="color:#e74c3c"></i>&nbsp; Attr Error (ERROR)<br>
     <i class="fa fa-location-arrow" style="color:#f1c40f"></i>&nbsp; Sign Missing
     </div>
     
    
            <div class="folium-map" id="map_89e9a55d2667377437c1b2742a8c082a" ></div>
        
</body>
<script>
    
    
            var map_89e9a55d2667377437c1b2742a8c082a = L.map(
                "map_89e9a55d2667377437c1b2742a8c082a",
                {
                    center: [42.7735105, 23.245952],
                    crs: L.CRS.EPSG3857,
                    ...{
  "zoom": 14,
  "zoomControl": true,
  "preferCanvas": false,
}

                }
            );

            

        
    
            var tile_layer_9fcdf61591f9079bbd87cb71229a6f9b = L.tileLayer(
                "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
                {
  "minZoom": 0,
  "maxZoom": 20,
  "maxNativeZoom": 20,
  "noWrap": false,
  "attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors \u0026copy; \u003ca href=\"https://carto.com/attributions\"\u003eCARTO\u003c/a\u003e",
  "subdomains": "abcd",
  "detectRetina": false,
  "tms": false,
  "opacity": 1,
}

            );
        
    
            tile_layer_9fcdf61591f9079bbd87cb71229a6f9b.addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var marker_3e301fdaae60fc4534aced8d98f5504e = L.marker(
                [42.73759, 23.24279],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_3c03ca200eea7105eefd8cf310216bca = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(126.25deg); color:#f1c40f;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_3e301fdaae60fc4534aced8d98f5504e.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #f1c40f; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#f1c40f; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>MISSING</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1164660447</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Slivnitsa, 1390 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">30</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#f1c40f;">—</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">38</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>20%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:20.0%; background:#f1c40f; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_3e301fdaae60fc4534aced8d98f5504e.setIcon(div_icon_3c03ca200eea7105eefd8cf310216bca);
            
    
            var marker_af291c25fe2642fdd82ce7c1ed184ada = L.marker(
                [42.78292, 23.24305],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_c4a9db65a411e966b3a349380ea855a1 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(320.01deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_af291c25fe2642fdd82ce7c1ed184ada.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1260859173</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Lomsko shose, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">30</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">30</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">55</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>88%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:88.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_af291c25fe2642fdd82ce7c1ed184ada.setIcon(div_icon_c4a9db65a411e966b3a349380ea855a1);
            
    
            var marker_7dabdd4a468721ee718663f46e65b665 = L.marker(
                [42.77996999999999, 23.24641],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_975bb308930a5716baac585e0eb185fb = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(321.26deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_7dabdd4a468721ee718663f46e65b665.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1272066950</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Lomsko shose, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">30</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">30</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">55</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>89%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:89.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_7dabdd4a468721ee718663f46e65b665.setIcon(div_icon_975bb308930a5716baac585e0eb185fb);
            
    
            var marker_b0871368c508c0fc483ae52a0e00e89a = L.marker(
                [42.78252, 23.24557],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_f7602a52e780c9f89e330fe1e5aeec1b = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(128.17deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_b0871368c508c0fc483ae52a0e00e89a.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1267094170</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Magistrala Evropa, 1271 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">40</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">40</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">108</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>88%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:88.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_b0871368c508c0fc483ae52a0e00e89a.setIcon(div_icon_f7602a52e780c9f89e330fe1e5aeec1b);
            
    
            var marker_0d96941468c20da1d66dd0475f0155d0 = L.marker(
                [42.73793, 23.24217],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_eaefc693f51c1fb63dd107dc97a78e60 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(126.75deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_0d96941468c20da1d66dd0475f0155d0.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1164350132</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Slivnitsa, 1390 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">70</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">70</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">46</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>99%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:99.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_0d96941468c20da1d66dd0475f0155d0.setIcon(div_icon_eaefc693f51c1fb63dd107dc97a78e60);
            
    
            var marker_a783cf9ae577228bab80bd4e0f2195c5 = L.marker(
                [42.78514, 23.24058],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_a3eb98a7f326eebf4325b25a0515d573 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(146.37deg); color:#e74c3c;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_a783cf9ae577228bab80bd4e0f2195c5.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #e74c3c; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#e74c3c; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>ERROR</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1133384061</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Lomsko shose, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">50</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#e74c3c;">40</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">52</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>1%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:1.0%; background:#e74c3c; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_a783cf9ae577228bab80bd4e0f2195c5.setIcon(div_icon_a3eb98a7f326eebf4325b25a0515d573);
            
    
            var marker_780f5f20c711cef6ac3fb7c24e2d7e60 = L.marker(
                [42.78288999999999, 23.24472],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_ae748ad4771cf71d89d88aecbee4c1a9 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(303.61deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_780f5f20c711cef6ac3fb7c24e2d7e60.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1267094172</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Magistrala Evropa, 1271 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">40</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">40</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">107</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>92%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:92.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_780f5f20c711cef6ac3fb7c24e2d7e60.setIcon(div_icon_ae748ad4771cf71d89d88aecbee4c1a9);
            
    
            var marker_6ccde71dbfc71cbc56ac40a436f3749c = L.marker(
                [42.78771, 23.23848],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_decea3b324c22318fa8430378f3adba9 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(148.55deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_6ccde71dbfc71cbc56ac40a436f3749c.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1172555895</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> 81, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">70</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">70</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">73</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>97%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:97.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_6ccde71dbfc71cbc56ac40a436f3749c.setIcon(div_icon_decea3b324c22318fa8430378f3adba9);
            
    
            var marker_944acc05d36095040ddc4e365ae020de = L.marker(
                [42.73565999999999, 23.24602],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_afb2aeb7f4e963a9f399420f6dbcbefd = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(127.32deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_944acc05d36095040ddc4e365ae020de.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1142079458</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Slivnitsa, 1336 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">30</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">30</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">37</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>95%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:95.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_944acc05d36095040ddc4e365ae020de.setIcon(div_icon_afb2aeb7f4e963a9f399420f6dbcbefd);
            
    
            var marker_248d29df02ab40310782fc9fce036662 = L.marker(
                [42.75077, 23.22514],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_977d57314b0e9501e550e38e02fdb577 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(157.95deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_248d29df02ab40310782fc9fce036662.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1256401354</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Evropeyski pat, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">70</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">70</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">72</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>100%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:100.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_248d29df02ab40310782fc9fce036662.setIcon(div_icon_977d57314b0e9501e550e38e02fdb577);
            
    
            var marker_695d9b502d97b357e1763ac706e82cbc = L.marker(
                [42.7807, 23.24404],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_c07ecabe1c2adbb2e644a1e19ac19969 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(71.19deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_695d9b502d97b357e1763ac706e82cbc.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1272190778</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Ulitsa Druzhba, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">30</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">30</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">—</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>90%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:90.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_695d9b502d97b357e1763ac706e82cbc.setIcon(div_icon_c07ecabe1c2adbb2e644a1e19ac19969);
            
    
            var marker_3cbee581b72df9505a5f3d463feb797f = L.marker(
                [42.78482000000001, 23.24087],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_6e48beda67ad384198b37e37fa5ec56a = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(143.72deg); color:#e74c3c;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_3cbee581b72df9505a5f3d463feb797f.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #e74c3c; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#e74c3c; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>ERROR</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1133384063</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Lomsko shose, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">30</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#e74c3c;">40</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">38</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>1%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:1.0%; background:#e74c3c; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_3cbee581b72df9505a5f3d463feb797f.setIcon(div_icon_6e48beda67ad384198b37e37fa5ec56a);
            
    
            var marker_8bf999ad777b9c0d8c42f98e9b475fea = L.marker(
                [42.78504, 23.24081],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_b98032fc380101faa88bcb7c127c8962 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(325.73deg); color:#e74c3c;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_8bf999ad777b9c0d8c42f98e9b475fea.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #e74c3c; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#e74c3c; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>ERROR</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1133384064</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Lomsko shose, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">60</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#e74c3c;">40</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">44</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>1%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:1.0%; background:#e74c3c; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_8bf999ad777b9c0d8c42f98e9b475fea.setIcon(div_icon_b98032fc380101faa88bcb7c127c8962);
            
    
            var marker_fcd36f90e1f4dd734beccdf57cc639d9 = L.marker(
                [42.78200999999999, 23.24395],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_3d68aaaab7af7729e34c9730e2b66423 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(139.64deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_fcd36f90e1f4dd734beccdf57cc639d9.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1272188746</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Lomsko shose, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">30</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">30</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">47</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>96%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:96.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_fcd36f90e1f4dd734beccdf57cc639d9.setIcon(div_icon_3d68aaaab7af7729e34c9730e2b66423);
            
    
            var marker_1a6305ee3522f1e75703926ca1ce601b = L.marker(
                [42.75840999999999, 23.26644],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_b6b8d3e120546c3b0ad476dc3b0ee4f1 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(33.36deg); color:#e74c3c;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_1a6305ee3522f1e75703926ca1ce601b.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #e74c3c; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#e74c3c; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>ERROR</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1132673159</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Ulitsa Okolovrasten pat, 1360 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">50</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#e74c3c;">100</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">44</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>18%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:18.0%; background:#e74c3c; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_1a6305ee3522f1e75703926ca1ce601b.setIcon(div_icon_b6b8d3e120546c3b0ad476dc3b0ee4f1);
            
    
            var marker_babcab60e87048f7ba187486674a33ca = L.marker(
                [42.79989, 23.22648],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_1e4e46cba7ecc6cb0ff9f2da014b0a22 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(322.48deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_babcab60e87048f7ba187486674a33ca.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1211790765</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> 81, Kostinbrod, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">40</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">40</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">48</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>97%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:97.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_babcab60e87048f7ba187486674a33ca.setIcon(div_icon_1e4e46cba7ecc6cb0ff9f2da014b0a22);
            
    
            var marker_814bbc24e685a568d4eaf73f8a89fdad = L.marker(
                [42.76935000000002, 23.28597],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_b304c3362ae8e339c6db2547dff7081a = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(316.66deg); color:#e74c3c;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_814bbc24e685a568d4eaf73f8a89fdad.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #e74c3c; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#e74c3c; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>ERROR</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1132672622</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> E79, 1298 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">40</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#e74c3c;">80</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">75</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>1%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:1.0%; background:#e74c3c; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_814bbc24e685a568d4eaf73f8a89fdad.setIcon(div_icon_b304c3362ae8e339c6db2547dff7081a);
            
    
            var marker_28dfed2bd9417eb1f0fd291073b15313 = L.marker(
                [42.78445, 23.24233],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_ce115621df04ce546b79d196ce8b1137 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(277.06deg); color:#e74c3c;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_28dfed2bd9417eb1f0fd291073b15313.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #e74c3c; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#e74c3c; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>ERROR</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1272067195</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Bulevard Lomsko shose, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">30</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#e74c3c;">100</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">43</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>10%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:10.0%; background:#e74c3c; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_28dfed2bd9417eb1f0fd291073b15313.setIcon(div_icon_ce115621df04ce546b79d196ce8b1137);
            
    
            var marker_4c4e34fcd34a1e87216b9faa88085d1a = L.marker(
                [42.77521000000001, 23.27435],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_3f92144392045b48a33e82f68a0a2920 = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(177.66deg); color:#2ecc71;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_4c4e34fcd34a1e87216b9faa88085d1a.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #2ecc71; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#2ecc71; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>OK</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1272048943</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> Ulitsa Vasil Levski 67, 1261 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">50</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#2ecc71;">50</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">45</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>88%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:88.0%; background:#2ecc71; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_4c4e34fcd34a1e87216b9faa88085d1a.setIcon(div_icon_3f92144392045b48a33e82f68a0a2920);
            
    
            var marker_a0f0621e1b9dbe093d2b405a709763f0 = L.marker(
                [42.78723, 23.23887],
                {
}
            ).addTo(map_89e9a55d2667377437c1b2742a8c082a);
        
    
            var div_icon_c559112c77714008eb69aca58ca7274b = L.divIcon({
  "html": "\u003cdiv style=\"transform: rotate(149.36deg); color:#e74c3c;\"\u003e\n                        \u003ci class=\"fa fa-location-arrow\" style=\"font-size:24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);\"\u003e\u003c/i\u003e\n                    \u003c/div\u003e",
  "iconSize": [30, 30],
  "iconAnchor": [15, 15],
  "className": "empty",
});
        
    
            marker_a0f0621e1b9dbe093d2b405a709763f0.bindTooltip(
                `<div>
                     
    <div style="font-family: 'Segoe UI', sans-serif; width: 230px; border-radius: 10px; border: 2px solid #e74c3c; overflow: hidden; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">
        <div style="background:#e74c3c; color:white; padding:10px; font-weight:bold; font-size:14px; display:flex; justify-content:space-between;">
            <span>ERROR</span>
            <span style="font-size:10px; opacity:0.8;">ID: 1256434063</span>
        </div>
        <div style="padding:12px;">
            <div style="font-size:11px; color:#555; margin-bottom:8px;">
                <i class="fa fa-map-marker"></i> 81, 1346 Sofia, Bulgaria
            </div>
            <div style="display:flex; justify-content:space-between; text-align:center; margin-bottom:10px; background:#f9f9f9; padding:5px; border-radius:5px;">
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">HERE</div>
                    <div style="font-weight:bold;">60</div>
                </div>
                <div style="flex:1; border-left:1px solid #ddd; border-right:1px solid #ddd;">
                    <div style="font-size:9px; color:#888;">YOLO</div>
                    <div style="font-weight:bold; color:#e74c3c;">70</div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:9px; color:#888;">PROBE</div>
                    <div style="font-weight:bold;">69</div>
                </div>
            </div>
            <div style="font-size:10px; margin-bottom:3px; display:flex; justify-content:space-between;">
                <span>Existence Confidence</span>
                <b>1%</b>
            </div>
            <div style="width:100%; background:#eee; height:6px; border-radius:3px;">
                <div style="width:1.0%; background:#e74c3c; height:100%; border-radius:3px;"></div>
            </div>
        </div>
    </div>
    
                 </div>`,
                {
  "sticky": false,
}
            );
        
    
                marker_a0f0621e1b9dbe093d2b405a709763f0.setIcon(div_icon_c559112c77714008eb69aca58ca7274b);
            
</script>
</html>t_Final_Map.html…]()


[![Presentation PDF](https://img.shields.io/badge/Presentation-Full_Slide_Deck_(PDF)-red?style=for-the-badge&logo=adobeacrobatreader)](./map-freshness-audit-presentation.pdf)
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

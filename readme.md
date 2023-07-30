1. install ogr2ogr, download cities data from:

and run convert_gpkg.py to extract each layers to .json it will exort it to output/gpkg_layers

or if it doesnt work install ogrinfo and run commands on .gpkg file:

ogrinfo nl-geo.gpkg - to see which layers yours .gpkg contains

ogr2ogr -f GeoJSON output_buurten.json nl-geo.gpkg buurten - (layername)
ogr2ogr -f GeoJSON output_wijken.json nl-geo.gpkg wijken - (layername)
ogr2ogr -f GeoJSON output_gemeenten.json nl-geo.gpkg gemeenten - (layername)

2. run coords_to_lnglat.py but edit input file to selected layer
3. run delete_duplicates.py
4. run format.py

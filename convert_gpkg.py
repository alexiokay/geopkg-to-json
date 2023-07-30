import fiona
import geopandas as gpd

def run_ogrinfo(gpkg_file):
    geodata = fiona.open(gpkg_file)
    return geodata

def run_ogr2ogr(input_gpkg, output_geojson, layer_name):
    gdf = gpd.read_file(input_gpkg, layer=layer_name)
    gdf.to_file(output_geojson, driver="GeoJSON")

if __name__ == "__main__":
    # Replace 'nl-geo.gpkg' with the actual name of your .gpkg file
    gpkg_file = "data/nl-geo.gpkg"

    # Run ogrinfo to see which layers the .gpkg file contains
    layers_info = run_ogrinfo(gpkg_file)

    if layers_info is not None:
        for layer_name in fiona.listlayers(gpkg_file):
            print(f"{layer_name}")
            
            # Output each layer as GeoJSON
            output_geojson = f"output/gpkg_layers/{layer_name}.json"
            run_ogr2ogr(gpkg_file, output_geojson, layer_name)

        layers_info.close()  # Close the collection after iteration
    else:
        print("No layers found in the GeoPackage.")

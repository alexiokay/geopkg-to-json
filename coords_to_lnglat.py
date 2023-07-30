
import json
import unicodedata
from tqdm import tqdm
from geopy.geocoders import Nominatim

api_key = "AIzaSyBUmO4Y2x2BdqwJdN3zI0phmcPrOVozDNE"

properties_to_delete = [
    "omgevingsadressendichtheid",
    "stedelijkheid_adressen_per_km2",
    "bevolkingsdichtheid_inwoners_per_km2",
    "aantal_inwoners",
    "mannen",
    "vrouwen",
    "percentage_personen_0_tot_15_jaar",
    "percentage_personen_15_tot_25_jaar",
    "percentage_personen_25_tot_45_jaar",
    "percentage_personen_45_tot_65_jaar",
    "percentage_personen_65_jaar_en_ouder",
    "percentage_ongehuwd",
    "percentage_gehuwd",
    "percentage_gescheid",
    "percentage_verweduwd",
    "aantal_huishoudens",
    "percentage_eenpersoonshuishoudens",
    "percentage_huishoudens_zonder_kinderen",
    "percentage_huishoudens_met_kinderen",
    "gemiddelde_huishoudsgrootte",
    "percentage_westerse_migratieachtergrond",
    "percentage_niet_westerse_migratieachtergrond",
    "percentage_uit_marokko",
    "percentage_uit_nederlandse_antillen_en_aruba",
    "percentage_uit_suriname",
    "percentage_uit_turkije",
    "percentage_overige_nietwestersemigratieachtergrond",
    "oppervlakte_totaal_in_ha",
    "oppervlakte_land_in_ha",
    "oppervlakte_water_in_ha",
]


def normalize_city_name(city_name):
    return unicodedata.normalize("NFKD", city_name).encode("ASCII", "ignore").decode("utf-8")



def get_lat_lon(city_name, api_key):
    normalized_city_name = normalize_city_name(city_name)
    print(city_name)
    print(normalized_city_name)
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(normalized_city_name)

    if location is not None:
        return location.latitude, location.longitude
    else:
        return None, None

def delete_invalid_properties(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_features = len(data["features"])
    with tqdm(total=total_features, desc="Processing", unit="feature") as pbar:
        for feature in data["features"]:
            properties = feature["properties"]
            for key in properties_to_delete:
                properties.pop(key, None)
                
            # Check if the geometry contains coordinates instead of longitude and latitude
            if feature["geometry"]["type"] == "MultiPolygon":
                coordinates = feature["geometry"]["coordinates"]
                if all(isinstance(coord[0], (int, float)) for coord in coordinates[0][0]):
                    # Convert the coordinates to longitude and latitude using Google Maps API
                    city_name = feature["properties"]["gemeentenaam"]
                    lon, lat = get_lat_lon(city_name, api_key)
                    if lat is not None and lon is not None:
                        feature["properties"]["gemeentenaam"] = normalize_city_name(feature["properties"]["gemeentenaam"])
                        feature["geometry"]["coordinates"] = [lon, lat]

            pbar.update(1)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == "__main__":
    try:
        input_file = "data/output_gemeenten.json"
        output_file = "temp/gemeenten_converted.json"
        delete_invalid_properties(input_file, output_file)
    except Exception as e:
        print("An error occurred:", e)

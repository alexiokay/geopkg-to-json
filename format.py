import json

def convert_data(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    new_data = []
    for feature in data["features"]:
        city_name = feature["properties"]["gemeentenaam"]
        zip_code = feature["properties"]["gemeentecode"]
        lat, lng = feature["geometry"]["coordinates"]
        country = "Netherlands"  # You can customize this if needed
        iso2 = "NL"  # You can customize this if needed
        admin_name = ""  # You can customize this if needed
        capital = ""  # You can customize this if needed
        population = ""  # You can customize this if needed
        population_proper = ""  # You can customize this if needed

        new_entry = {
            "city": city_name,
            "zip-code": zip_code,  # You can customize this if needed
            "lat": str(lat),
            "lng": str(lng),
            "country": country,
            "iso2": iso2,
            "admin_name": admin_name,
            "capital": capital,
            "population": population,
            "population_proper": population_proper
        }

        new_data.append(new_entry)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    try:
        input_file = "temp/gemeenten_no_duplicates.json"  # Replace with your input file name
        output_file = "output/gemeenten.json"  # Replace with your desired output file name
        convert_data(input_file, output_file)
    except Exception as e:
        print("An error occurred:", e)

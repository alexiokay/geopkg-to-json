import json

def delete_duplicates(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    unique_combinations = set()
    new_features = []

    duplicate_count = 0
    for feature in data["features"]:
        gemeentecode = feature["properties"]["gemeentecode"]
        gemeentenaam = feature["properties"]["gemeentenaam"]
        combination = (gemeentecode, gemeentenaam)

        if combination not in unique_combinations:
            new_features.append(feature)
            unique_combinations.add(combination)
        else:
            # Increment the duplicate_count
            duplicate_count += 1
            # Optionally, you can print or handle the duplicates
            print(f"Duplicate found: gemeentecode={gemeentecode}, gemeentenaam={gemeentenaam}")

    print(f"Removed {duplicate_count} duplicates")
    data["features"] = new_features

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == "__main__":
    try:
        input_file = "temp/gemeenten_converted.json"
        output_file = "temp/gemeenten_no_duplicates.json"
        delete_duplicates(input_file, output_file)
    except Exception as e:
        print("An error occurred:", e)

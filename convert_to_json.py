import json

tsv_file = "amfi_data.tsv"
json_file = "amfi_data.json"

data = []
with open(tsv_file, "r", encoding="utf-8") as tsv:
    next(tsv)
    
    for line in tsv:
        scheme_name, nav_value = line.strip().split("\t")
        data.append({
            "Scheme Name": scheme_name,
            "Asset Value": nav_value
        })

with open(json_file, "w", encoding="utf-8") as json_out:
    json.dump(data, json_out, indent=2)

print(f" Data has been converted to JSON and saved to {json_file}")

import json


file_path = "data.json"
with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

print(json.dumps(json_data, indent=4))


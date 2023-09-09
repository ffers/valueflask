import json


data_get_st = {
               "apiKey": "[ВАШ КЛЮЧ]",
               "modelName": "TrackingDocument",
               "calledMethod": "getStatusDocuments",
               "methodProperties": {
            "Documents" : [
            {
            "DocumentNumber":"20400048799000",
            "Phone":"380600000000"
            }
            ,
            {
            "DocumentNumber":"20400048799001",
            "Phone":"380600000000"
            }
            ]
               }
            }

# Створюємо пустий список для зберігання JSON-об'єктів
json_objects = data_get_st["methodProperties"]["Documents"]
phone_numbers = ["380600000000", "380600000001", "380600000002"]
doc_number = "200000000000"
# Ітеруємося по списку телефонних номерів
for phone_number in phone_numbers:
    json_data = {
        "DocumentNumber": doc_number,
        "Phone": phone_number
                 }
    json_objects.append(json_data)

# Конвертуємо список JSON-об'єктів в рядок JSON
json_string = json.dumps(json_objects, indent=4)
data_get_st = json.dumps(data_get_st, indent=4, ensure_ascii=False)
# Виводимо результат
print(data_get_st)
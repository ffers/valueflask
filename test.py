import os, json, requests
from os.path import join, dirname
import sys
from dotenv import load_dotenv
# Початковий словник з даними
data = {
    "apiKey": "your_api_key",
    "modelName": "TrackingDocument",
    "calledMethod": "getStatusDocuments",
    "methodProperties": {
        "Documents": [
            {
                "DocumentNumber": "20400048799000",
                "Phone": "380600000000"
            }
        ]
    }
}

# Другий номер, який ви хочете додати
second_phone = "380600000001"

# Перевіряємо, чи потрібно додати другий номер
if second_phone:
    # Створюємо новий об'єкт для другого номеру
    second_document = {
        "DocumentNumber": "20400048799001",
        "Phone": second_phone
    }
    # Додаємо об'єкт другого номеру до списку Documents
    data["methodProperties"]["Documents"].append(second_document)

# Конвертуємо словник у JSON-рядок
json_data = json.dumps(data, ensure_ascii=False)

# Виводимо JSON-рядок
print(json_data)


# Початковий JSON-об'єкт
json_data = """
{
   "apiKey": "your_api_key",
   "modelName": "TrackingDocument",
   "calledMethod": "getStatusDocuments",
   "methodProperties": {
        "Documents": [
            {
                "DocumentNumber": "20400048799000",
                "Phone": "380600000000"
            },
            {
                "DocumentNumber": "20400048799001",
                "Phone": "380600000000"
            }
        ]
    }
}
"""

# Розбираємо JSON-рядок у Python-об'єкт




# Виводимо оновлений JSON-рядок

# response = requests.post(url, data=json_data, headers=headers)
def request_np(json_data):
    token = get_from_env("NP_TOKEN")
    data = json.loads(json_data)
    phone = get_from_env("NP_PHONE")
    DocNumber = "20450770805091"
    data["apiKey"] = token
    updated_json_data = json.dumps(data, ensure_ascii=False)
    data["methodProperties"]["Documents"][0]["DocumentNumber"] = DocNumber
    updated_json_data = json.dumps(data, ensure_ascii=False)
    data["methodProperties"]["Documents"][0]["Phone"] = phone
    updated_json_data = json.dumps(data, ensure_ascii=False)
    print(updated_json_data)

    # json_data = json.dumps(data)
    # if response.status_code == 200:
    #     print("Запит був успішно відправлений.")
    #     print("Відповідь від сервера:")
    #     print(response.text)
    # else:
    #     print("Помилка при відправці запиту. Статус код:", response.status_code)

from datetime import datetime, timezone

# Отримуємо поточну дату та час у часовому поясі UTC
current_datetime = datetime.now(timezone.utc)

# Форматуємо дату та час у бажаний формат "дд.мм.рррр"
formatted_datetime = current_datetime.strftime("%d.%m.%Y")

# Виводимо отформатовану дату
print(formatted_datetime)

def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)

request_np(json_data)

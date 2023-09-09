import os, json, requests
from os.path import join, dirname
import sys
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
import pprint

current_datetime = datetime.now(timezone.utc)
date_today = current_datetime.strftime("%d.%m.%Y")
date_yesterday_nf = current_datetime - timedelta(days=7)
date_yesterday = date_yesterday_nf.strftime("%d.%m.%Y")
date_7day_nf = current_datetime - timedelta(days=1)
date_7day = date_7day_nf.strftime("%d.%m.%Y")
api_url = "https://api.novaposhta.ua/v2.0/json/"
filename = current_datetime.strftime("%Y-%m-%d_%H%M%S")
ttn_json_f_n = "ttn/ttn_" + filename + ".txt"
stat_json_f_n = filename + "st.json"
folder_path = "ttn"
files = os.listdir(folder_path)

data = {
           "apiKey": "[ВАШ КЛЮЧ]",
           "modelName": "InternetDocument",
           "calledMethod": "getDocumentList",
           "methodProperties": {
                "DateTimeFrom" : "дд.мм.рррр",
                "DateTimeTo" : "дд.мм.рррр",
                "Page" : "1",
                "GetFullList" : "1",
                   }
                }

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


json_data = json.dumps(data, ensure_ascii=False)
get_st_json = json.dumps(data_get_st, ensure_ascii=False)


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)

def request_np(updated_json):
    response = requests.get(api_url, data=updated_json)
    if response.status_code == 200:
        api_data = response.json()
        return api_data
    else:
        print("Помилка при відправці запиту. Статус код:", response.status_code)

def get_list(json_data):
    token = get_from_env("NP_TOKEN")
    data = json.loads(json_data)
    DateTimeFrom = date_yesterday
    DateTimeTo = date_today
    data["apiKey"] = token
    updated_json_data = json.dumps(data, ensure_ascii=False)
    data["methodProperties"]["DateTimeFrom"] = DateTimeFrom
    updated_json_data = json.dumps(data, ensure_ascii=False)
    data["methodProperties"]["DateTimeTo"] = DateTimeTo
    updated_json = json.dumps(data, ensure_ascii=False)

    return request_np(updated_json)

def ttn_list(get_ttn):
    file_path = ttn_json_f_n
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     json_data = json.load(file)
    get_ttn_list = {item["IntDocNumber"] for item in get_ttn["data"] }
    with open(ttn_json_f_n, 'w', encoding='utf-8') as file:
        for item in get_ttn_list:
            file.write(item + '\n')
    return get_ttn_list

def get_stat(get_st_json, doc_num):
    token = get_from_env("NP_TOKEN")
    data = json.loads(get_st_json)
    docs = doc_num
    Phone = get_from_env("NP_PHONE")
    data["apiKey"] = token
    json_objects = data_get_st["methodProperties"]["Documents"]
    for doc in docs:
        json_data = {
            "DocumentNumber": doc,
            "Phone": Phone
        }
        json_objects.append(json_data)


    # updated_json_data = json.dumps(data, ensure_ascii=False)
    # data["methodProperties"]["methodProperties"][0]["DocumentNumber"] = DocumentNumber
    # updated_json_data = json.dumps(data, ensure_ascii=False)
    # data["methodProperties"]["methodProperties"][0]["Phone"] = Phone
    # updated_json = json.dumps(data, ensure_ascii=False)
    return request_np(json_objects)

def last_file(files):
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)
    if files:
        last_modified_file = files[0]
        return last_modified_file
    else:
        print("У папці немає файлів")


get_ttns = get_list(json_data)
get_ttn_list = ttn_list(get_ttns)
print(get_ttn_list)


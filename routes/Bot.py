from flask import Blueprint, redirect, render_template, request, flash, redirect, url_for, jsonify, session
from models import Comment, Posts, Reply, Reply2, Users
from flask_login import login_required, current_user
from db import db
import sys
from dotenv import load_dotenv
import os, json
from os.path import join, dirname


bp = Blueprint('Bot', __name__, template_folder='templates')

headers = {"Content-Type": "application/json"}

json_data = {
   "apiKey": "token_np",
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

response = requests.post(url, data=json_data, headers=headers)

def request_np(json_data):
    token = get_from_env("NP_TOKEN")
    data = json.loads(json_data)
    data["apiKey"] = token
    data["methodProperties"]["Documents"][0]["Phone"] = token

    json_data = json.dumps(data)
    if response.status_code == 200:
        print("Запит був успішно відправлений.")
        print("Відповідь від сервера:")
        print(response.text)
    else:
        print("Помилка при відправці запиту. Статус код:", response.status_code)


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)

@bp.route("/bot", methods=['POST', 'GET'])

def Bot():
    if request.method == 'POST':
        print(request.json)
        return {'ok':True}
    return render_template('index.html', user=current_user)

@bp.route("/novaposhta", methods=['POST', 'GET'])

def novaposhta():
    if request.method == 'POST':
        print(request.json)
        return {'ok':True}
    else:
        request_np()
    return render_template('index.html', user=current_user)



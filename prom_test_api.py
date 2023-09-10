import os, json, requests
from os.path import join, dirname
import sys
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
import http.client
import pprint

HOST = 'my.prom.ua'
AUTH_TOKEN = ''
current_datetime = datetime.now(timezone.utc)
date_today = current_datetime.strftime("%d.%m.%Y")
date_yesterday_nf = current_datetime - timedelta(days=1)
date_yesterday = date_yesterday_nf.strftime("%d.%m.%Y")
date_7day_nf = current_datetime - timedelta(days=7)
date_7day = date_7day_nf.strftime("%d.%m.%Y")
api_url = "https://api.novaposhta.ua/v2.0/json/"
file_name = "data.json"





# API Settigs
 # Your authorization token
HOST = 'my.prom.ua'  # e.g.: my.prom.ua, my.tiu.ru, my.satu.kz, my.deal.by, my.prom.md

def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)

class HTTPError(Exception):
    pass


class EvoClientExample(object):

    def __init__(self, token):
        self.token = token

    def make_request(self, method, url, body=None):
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                   'Content-type': 'application/json'}
        if body:
            body = json.dumps(body)

        connection.request(method, url, body=body, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            raise HTTPError('{}: {}'.format(response.status, response.reason))

        response_data = response.read()
        return json.loads(response_data.decode())

    def get_order_list(self):
        url = '/api/v1/orders/list'
        method = 'GET'

        return self.make_request(method, url)

    def get_order(self, order_id):
        url = '/api/v1/orders/{id}'
        method = 'GET'

        return self.make_request(method, url.format(id=order_id))




def main():
    AUTH_TOKEN = get_from_env("PROM_TOKEN")
    # Initialize Client
    if not AUTH_TOKEN:
        raise Exception('Sorry, there\'s no any AUTH_TOKEN!')

    api_example = EvoClientExample(AUTH_TOKEN)

    order_list = api_example.get_order_list()
    if not order_list['orders']:
        raise Exception('Sorry, there\'s no any order!')

   # pprint.pprint(api_example.get_order_list())

    # Order example data. Requred to be setup to get example work
    order_id = order_list['orders'][0]['id']

    # Setting order status

    # # Getting order by id
    #pprint.pprint(api_example.get_order(order_id))

    with open(file_name, 'w', encoding='utf-8') as file:
       json.dump(order_list, file, indent=4, ensure_ascii=False)

    


if __name__ == '__main__':
    main()
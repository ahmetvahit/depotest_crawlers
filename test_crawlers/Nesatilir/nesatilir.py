import json
import requests
from datetime import datetime


class NeSatilir():
    name = "Nesatilir"
    output = []
    BASE_URL = "https://api.nesatilir.com/api/v1/GetTop100Analysis"

    def __init__(self):
        self.headers = {
            'authority': 'api.nesatilir.com',
            'accept': '*/*',
            'accept-language': 'tr,en-US;q=0.9,en;q=0.8',
            'origin': 'https://users.nesatilir.com',
            'referer': 'https://users.nesatilir.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }
        self.json_data = {
            'siteId': 'TY',
            'categoryId': '3494',
            'Token': 'cwT8qQCgjEuf9IjpAuW6Fg56519',
        }
        self.products = None

    def post(self):
        ''' categoryId, Token ve siteId kullanarak Json_data yı kullanarak api linkine POST metodu ile gönderiyor'''

        response = requests.post(self.BASE_URL,
                                 headers=self.headers,
                                 json=self.json_data)
        self.products = json.loads(response.text)

    def parse(self):
        pass

    def close(self):
        pass
        # with open(f"data/step_1_{self.name}.json", "w", encoding="utf-8") as f:
        #     json.dump(self.products, f, ensure_ascii=False)


process = NeSatilir()
process.post()
process.close()

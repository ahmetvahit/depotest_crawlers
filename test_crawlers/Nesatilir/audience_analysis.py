import requests
from pprint import pprint
from integrations.utils.request_handler import *

BASE_URL = "https://api.nesatilir.com/api"

api = APIRequestHandler()
api.verbose = True
auth_token = "None"


def get_category_id() -> dict:
    ''' Aranacak kategoriye ait terim giriliyor ve bu api içerisinde get_target_audience fonksiyonu için gerekli
        categoryId bilgisi yer almakta ilk fonksiyonda bunları kaydedip ikinci fonksiyonda sırayla categoryID ler için
        kullanılabilir '''

    data = {
        'term': 'ka',
        'siteId': 4,
    }
    return api._request(f"{BASE_URL}/v1/HBGetSubCategories", "POST", data=data)

    # subcat_ids = api._request(f"{BASE_URL}/v1/HBGetSubCategories", "POST", data=data)
    # with open(f"data/subcats_ids.json", "w", encoding="utf-8") as f:
    #     json.dump(subcat_ids, f, ensure_ascii=False)

def get_target_audience(category_id: str) -> dict:
    data = {
        'categoryid': category_id,
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/GetTargetAudienceGraphicsV2", "POST", data=data)


pprint(get_category_id())
pprint(get_target_audience(60007508))

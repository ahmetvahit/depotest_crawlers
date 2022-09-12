import requests
from pprint import pprint
from integrations.utils.request_handler import *

BASE_URL = "https://api.nesatilir.com/api"

api = APIRequestHandler()
api.verbose = True
auth_token = "None"


def get_product_resarch(category_id: str) -> dict:  # Ürün Araştırma
    data = {
        'is_favorite': 0,
        'page': 0,
        'country': '',
        'cat': [
            category_id,
            '',
        ],
        'cattype': '1',
        'prod': {
            'all': 1,
        },
        'includev2': [],
        'orderby': 'Last30DaySales',
        'ordertype': 'DESC',
        'displayrow': 25,
        'Token': auth_token,
        'DeviceType': 0,
        'ArbitrageType': '',
        'SellerTypes': 'all',
        'BadgesTypes': 'all',
        'AmazonCountry': 'US',
    }
    return api._request(f"{BASE_URL}/v1/TYGetProducts", "POST", data=data)


def get_retail_arbitrage_products(cat_id: str, country: str = "usa", amazon_country: str = "USA") -> dict:
    data = {
        'is_favorite': 0,
        'page': 0,
        'country': country,
        'cat': [
            cat_id,
            '',
        ],
        'cattype': '1',
        'prod': {
            'all': 1,
        },
        'include': '',
        'orderby': 'FarkYuzde',
        'ordertype': 'DESC',
        'displayrow': 25,
        'Token': auth_token,
        'DeviceType': 0,
        'ArbitrageType': '',
        'SellerTypes': 'all',
        'BadgesTypes': 'all',
        'AmazonCountry': amazon_country,
    }
    return api._request(f"{BASE_URL}/v1/GetTYRetailArbitrageProducts", "POST", data=data)


def get_favorite_products(category_id: str, platfrom_id: str = "TY") -> dict: # Piyasa Analizi
    data = {
        'siteId': platfrom_id,
        'categoryId': category_id,
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/GetTop100Analysis", "POST", data=data)


def get_target_audience(category_id: str) -> dict: # Hedef Kitle Analizi
    data = {
        'categoryid': category_id,
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/GetTargetAudienceGraphicsV2", "POST", data=data)


def auto_pricing(UserStoreApiId: str) -> dict:  # Otomatik Fiyatlandırma
    data = {
        'Token': 'ygaFnIDL1E2Ci0sxG0JGxw56519',
        'UserStoreApiId': '7991',
    }
    return api._request(f"{BASE_URL}/v1/TYGetAccountInfo", "POST", data=data)


def sort_finder():  # Takip Araçları>Sıralama Bulucu
    data = {
        'Token': auth_token
    }
    return api._request(f"{BASE_URL}/v1/KeywordTrackerProductList", "POST", data=data)


def get_word_mine(keyword: str) -> dict:  # Takip Araçları>Kelime Madeni
    data = {
        'keyword': keyword,
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/GetMagnetKeywords", "POST", data=data)


def get_stock_tracker_productslist() -> dict:  # Takip Araçları>Stok Takibi
    data = {
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}StockTrackerProductList", "POST", data=data)


def buybox_add_product(product_id: str,  # Takip Araçları>Buybox Takibi (Ürün Ekleme)
                       platfrom_id: str = "TY") -> dict:
    data = {
        'img': '',
        'name': 'Proline Bebek Pudrası Kokulu Ince Tane Topaklanan Kedi Kumu 10 Lt X 2 Adet',
        'url': 'https://www.trendyol.com/skechers/bobs-bamina-star-strikez-kadin-beyaz-spor-ayakkabi-117355-ofwt-p-260194859',
        'market': platfrom_id,
        'productid': product_id,
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/BuyBoxAddProduct", "POST", data=data)


def buybox_product_list() -> dict:  # Takip Araçları>Buybox Takibi (Ürün Listeleme)
    data = {
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/BuyBoxTrackerProductList", "POST", data=data)


def price_tracking_add(product_url: str) -> dict:  # Takip Araçları>Fiyat Takibi (Ürün Ekleme)
    data = {
        'ProductLink': product_url,
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/PTAddProduct", "POST", data=data)


def price_tracking_list() -> dict:  # Takip Araçları>Fiyat Takibi (Ürün Listeleme)
    data = {
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/PriceTrackerProductList", "POST", data=data)


def get_1000_top_products() -> dict:  # Top 1000 Yorum Analizi
    data = {
        'isWeb': 1,
        'Token': auth_token,
        'keyword': '',
    }
    return api._request(f"{BASE_URL}/v1/GetTYTop1000CommentProducts", "POST", data=data)


pprint(get_product_resarch(403))
pprint(get_retail_arbitrage_products(1071))
pprint(get_favorite_products(3494))
pprint(get_target_audience(60007508))
pprint(auto_pricing(7991))
pprint(get_word_mine("iphone"))
pprint(get_stock_tracker_productslist())
pprint(buybox_add_product(6319796))
pprint(buybox_product_list())
# pprint(price_tracking_add("https://www.trendyol.com/morenica/kadin-beyaz-kar-botu-p-50222455"))
pprint(price_tracking_list())
pprint(get_1000_top_products())

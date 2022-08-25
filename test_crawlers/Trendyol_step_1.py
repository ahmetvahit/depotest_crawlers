import json
import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime


class crawl(scrapy.Spider):
    def __init__(self, x):
        self.x = x
        self.name = "Trendyol"
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        self.output = []
        # urls = [
        #     "https://www.trendyol.com/magaza/profil/easy-smart-care-m-420435",
        #     "https://www.trendyol.com/magaza/profil/cnk-m-114723",
        #     "https://www.trendyol.com/magaza/profil/gndsmart-m-138257",
        #     "https://www.trendyol.com/magaza/profil/gundogan-a-s-m-481543",
        #     "https://www.trendyol.com/magaza/profil/elm-shoes-m-497288",
        #     "https://www.trendyol.com/magaza/profil/tekce-ticaret-m-315154",
        #     "https://www.trendyol.com/magaza/profil/bonjey-market-m-455724",
        #     "https://www.trendyol.com/magaza/profil/emrepazaravm-m-166315",
        #     "https://www.trendyol.com/magaza/profil/mdz-collection-m-206113",
        #     "https://www.trendyol.com/magaza/profil/inadina-pilav-m-623453",
        #     "https://www.trendyol.com/magaza/profil/chezedo-m-549703",
        #     "https://www.trendyol.com/magaza/profil/minimono-m-522055",
        #     "https://www.trendyol.com/magaza/profil/hediyechy-m-265889",
        #     "https://www.trendyol.com/magaza/profil/organikji-m-349365",
        #     "https://www.trendyol.com/magaza/profil/luvly-pets-m-316942",
        #     "https://www.trendyol.com/magaza/profil/deafox-m-108655",
        #     "https://www.trendyol.com/magaza/profil/arabulcenter-m-597771",
        #     "https://www.trendyol.com/magaza/profil/yemci-petshop-m-144941"
        # ]

        self.today = datetime.now().strftime("%Y-%m-%d")
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_requests(self):
        # for url in self.urls:
        req = scrapy.Request(self.x, callback=self.parse, dont_filter=True, headers=self.headers)
        yield req

    def parse(self, response):
        seller_score = response.css(".seller-store__score::text").get()
        try:
            s_seller = response.xpath("//img[@class='badge-img']/@src")[0].get()
            successful_seller = s_seller.split("/")[5].replace(".svg", "").replace("_", " ").replace("i",
                                                                                                     "ı").capitalize()
        except:
            successful_seller = None
        try:
            f_seller = response.xpath("//img[@class='badge-img']/@src")[1].get()
            fast_seller = f_seller.split("/")[5].replace(".svg", "").replace("-", " ").replace("i", "ı").capitalize()
        except:
            fast_seller = None

        location = response.css(".seller-info-container__wrapper__text-container__value::text")[1].get()
        number_of_products = response.css(".seller-info-container__wrapper__text-container__value::text")[2].get()
        ty_time = response.css(".seller-info-container__wrapper__text-container__value::text").get()

        try:
            time_cargo = response.css(".seller-metrics-container__wrapper__value::text").get()
        except:
            time_cargo = None

        try:
            ans_rate = response.css(".seller-metrics-container__wrapper__value::text")[1].get()
            answer_rate = ans_rate.replace("%", "") + "%"
        except:
            answer_rate = None

        try:
            rating = float(
                response.css(".seller-product-review-container__wrapper__rating_wrapper__rating_value::text").get())
        except:
            rating = None

        self.output.append({
            "seller_rating": seller_score,
            "time_in_ty": ty_time,
            "location": location,
            "number_of_products": number_of_products,
            "time_cargo": time_cargo,
            "answer_rate": answer_rate,
            "rating_score": rating,
            "badges": {
                "successful_seller": successful_seller,
                "fast_seller": fast_seller,
            }
        })

    def close(self, spider, reason):
        with open(f"step_1_{self.name}_{self.today}.json", "w", encoding="utf-8") as f:
            json.dump(self.output, f, ensure_ascii=False)

            # df = pd.read_json(json.dumps(self.output, ensure_ascii=False), encoding="utf-8")
            # df.to_excel("sample.xlsx",encoding="utf-8", index=False)


process = CrawlerProcess()
x = str(input("Enter URL: "))
process.crawl(crawl, x)
process.start()

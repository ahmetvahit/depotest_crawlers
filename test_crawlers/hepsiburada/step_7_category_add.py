import json
import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime


class crawl(scrapy.Spider):
    name = "Hepsiburada"
    output = []
    urls = []
    headers = {
        'cookie': '_gcl_au=1.1.591549031.1660413452; _gid=GA1.2.1359170139.1660413454; hbus_anonymousId=1fc07a1a-6c79-499c-ab2a-28455d520a37; _tt_enable_cookie=1; _ttp=aaec7b4f-e629-4ebc-bbe6-c43911581ebc; cookieconsentanon=false%7C13.08.2022%2020%3A57%3A40; cto_bundle=di2ecl9kSGo5UUtjWVZYOHlLbk1wUlNtanRKdlRUQTZYUnA3WUZ6MmdkYmNsb25QRzJobGhYSU95cE0zYTA4ZXpvSlRwdERPOTRoblQlMkJCTll1V2kwVm83bU5xU0V6UmNaOUgxTkp3YlU1WFhXc3FMODJhODkzZ0RsbCUyQk5jVmJuYzY3dVdmaWIyRkJMekFFOWthYVRYVnBGcE1BJTNEJTNE; _hjSessionUser_216130=eyJpZCI6IjJmZTBhMDc5LWQ1MGMtNTc1Yi1iZmY0LWVlMmQ2Yjk0MmJhNyIsImNyZWF0ZWQiOjE2NjA0MTM0NjA2NDMsImV4aXN0aW5nIjp0cnVlfQ==; dgr_searchresults=4175746f46696c7465724e657756616c69646174696f6e56347c64656661756c747c5573654e6577546f6c6b69656e50726564696374696f6e733d64697361626c65; isGlobalIp=1; _abck=BCEFE56ACBAB66E9FB8D719449E08536~0~YAAQjdlraDqco1yCAQAAj32Fmwjsqy6huSST2lfyIP98gZZ4rvQrxpNuporZjdoRRozrDATSDbTMNEVpcvzUL0X4zQkl0p1ldicSHJQY4S/woZF7a9NGFBXWYXT95gSr8GkxhMJvdlxE35UnkVUXMOIcysskW2xUyCWsScYpiWELRbpZc7BJy7xS2ySYCP53WD2CB6j2ZIYm8s2gYwS95jCVtTfy2gQ2OcND9pnQhB82Syq4QNkOqQgirSvHsS/CQNW+JmIiYOnPI32gCe3BlSn3hMS/jOoTBYmEkqlJfomdfQaBxC3p0JOffJgoj2ZN1UcZSVNBIBNQ5Zy7pfXSfdJmjJymXcbKCy0jwjPQg99y4qdYyy7fU9uU+GIz540noa2sK1keT3o5xmzQBdeRNQncGQc1PWSu7g9b/bE=~-1~-1~-1; bm_sz=E9BE16E347AC1CD9711ADA04F047628E~YAAQjdlraDuco1yCAQAAj32FmxCDqAk9JGsO8QCr9d9O14fb6JZpXPdTMOAdwW04wIiVKth+3Fz6Wt4d6zEOa2xRxmrGvWjSuKrcWVWbq2eP8qpycpjRy/TmSY4WAbor2O9HmoK85i4u7wsFlSpHh3rRIz30MdY7GIApXqI+rwgOOOAbEa6A5cmI+W/IC2FLr2flzVKUwzMovGB2wPPDLfhQa8aJafRv/5g3+YLtIZVaMOCek3sMm4omjaax81H++mNt5ZGtkPYb/Jbwf5MwiX4R+SVthOLTzTw6zROaEy/cmcjrbzTAxw==~3618373~3159602; wt3_eid=%3B289941511384204%7C2166041346800004667%232166046659000719809; wt3_sid=%3B289941511384204; _ga=GA1.2.1374688111.1660413454; _dc_gtm_UA-834379-1=1; ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%228323f778-5247-2489-00af-05a32f6354fb%22%2C%22e%22%3A1660468391986%2C%22c%22%3A1660466591986%2C%22l%22%3A1660466591986%7D; ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%22109b04d0-6f15-4090-5850-b64f3d886e15%22%2C%22c%22%3A1660413456413%2C%22l%22%3A1660466591988%7D; ab.storage.userId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%221fc07a1a-6c79-499c-ab2a-28455d520a37%22%2C%22c%22%3A1660413470228%2C%22l%22%3A1660466591988%7D; _hjIncludedInSessionSample=0; _hjSession_216130=eyJpZCI6ImUyNzM4NTM1LTYwMWItNDUzYy1iZGVlLTcxM2ZhZTVlOTM5ZSIsImNyZWF0ZWQiOjE2NjA0NjY2MDczMjUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _ga_44CSPTX731=GS1.1.1660466590.2.1.1660466611.39; hbus_sessionId=0ffde65d-87a8-4dea-985e-ebd9b2ff1cec%7C1660468428355',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = "https://www.hepsiburada.com/magaza"
    today = datetime.now().strftime("%Y-%m-%d")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    custom_settings = {
        "DOWNLOAD_DELAY": 0.2,
        "CONCURRENT_REQUESTS": 100,
        "RETRY_ENABLED": True,
        "RETRY_TIMES": 3
    }
    oyuncak_urls = [
        "https://www.hepsiburada.com/magaza/hakbigrup",
        "https://www.hepsiburada.com/magaza/b-m-toys",
        "https://www.hepsiburada.com/magaza/onur-oyuncak",
        "https://www.hepsiburada.com/magaza/demirbey",
        "https://www.hepsiburada.com/magaza/tarzreyon",
        "https://www.hepsiburada.com/magaza/unicorns",
        "https://www.hepsiburada.com/magaza/feel-good-co",
        "https://www.hepsiburada.com/magaza/sanalavm",
        "https://www.hepsiburada.com/magaza/zekaevi",
        "https://www.hepsiburada.com/magaza/i-magaza",
        "https://www.hepsiburada.com/magaza/cavusoglupazarlama",
        "https://www.hepsiburada.com/magaza/rectangle",
        "https://www.hepsiburada.com/magaza/zeze-toys",
        "https://www.hepsiburada.com/magaza/robotikstory",
        "https://www.hepsiburada.com/magaza/harika-pelus-fabrikasi",
        "https://www.hepsiburada.com/magaza/redbutika",
        "https://www.hepsiburada.com/magaza/vipfoni",
        "https://www.hepsiburada.com/magaza/adenoyuncak",
        "https://www.hepsiburada.com/magaza/naz-amigurumi",
        "https://www.hepsiburada.com/magaza/canmagaza06",
        "https://www.hepsiburada.com/magaza/karanticaret",
        "https://www.hepsiburada.com/magaza/uga-magazacilik",
        "https://www.hepsiburada.com/magaza/ilman",
        "https://www.hepsiburada.com/magaza/karaca-home",
        "https://www.hepsiburada.com/magaza/lati",
        "https://www.hepsiburada.com/magaza/zoziva",
        "https://www.hepsiburada.com/magaza/tahtakurusutasarim",
        "https://www.hepsiburada.com/magaza/gezburada",
        "https://www.hepsiburada.com/magaza/carino",
        "https://www.hepsiburada.com/magaza/incarea",
        "https://www.hepsiburada.com/magaza/officenjoy",
        "https://www.hepsiburada.com/magaza/nasip-ticaret-tuhafiye",
        "https://www.hepsiburada.com/magaza/sagentech",
        "https://www.hepsiburada.com/magaza/junitoys",
        "https://www.hepsiburada.com/magaza/makkara",
        "https://www.hepsiburada.com/magaza/kardelendesign",
        "https://www.hepsiburada.com/magaza/jet-express",
        "https://www.hepsiburada.com/magaza/nativu-wood",
        "https://www.hepsiburada.com/magaza/karabeyogullari-ticaret",
        "https://www.hepsiburada.com/magaza/candag",
        "https://www.hepsiburada.com/magaza/mini-yasam",
        "https://www.hepsiburada.com/magaza/e-impala",
        "https://www.hepsiburada.com/magaza/zenkid-oyuncak",
        "https://www.hepsiburada.com/magaza/x-black-market",
        "https://www.hepsiburada.com/magaza/ziphida",
        "https://www.hepsiburada.com/magaza/safestore",
        "https://www.hepsiburada.com/magaza/vogue-element",
        "https://www.hepsiburada.com/magaza/jcsweilan",
        "https://www.hepsiburada.com/magaza/ugur-baby",
        "https://www.hepsiburada.com/magaza/fenteer"

    ]

    pratikev_urls = [
        "https://www.hepsiburada.com/magaza/yenicag-isg-ekipmanlari",
        "https://www.hepsiburada.com/magaza/fevito",
        "https://www.hepsiburada.com/magaza/uglshop ",
        "https://www.hepsiburada.com/magaza/vienev",
        "https://www.hepsiburada.com/magaza/fackelmann-turkiye",
        "https://www.hepsiburada.com/magaza/ecrin-temizlik-ve-gida",
        "https://www.hepsiburada.com/magaza/nergis-store",
        "https://www.hepsiburada.com/magaza/gempo",
        "https://www.hepsiburada.com/magaza/dedeevtekstil",
        "https://www.hepsiburada.com/magaza/washingnet",
        "https://www.hepsiburada.com/magaza/dedeticaret",
        "https://www.hepsiburada.com/magaza/pastel-global",
        "https://www.hepsiburada.com/magaza/taskin-home",
        "https://www.hepsiburada.com/magaza/filemingo",
        "https://www.hepsiburada.com/magaza/fetihevgerecleri",
        "https://www.hepsiburada.com/magaza/hane216",
        "https://www.hepsiburada.com/magaza/b-r-avm",
        "https://www.hepsiburada.com/magaza/falez-w",
        "https://www.hepsiburada.com/magaza/yesil-koala",
        "https://www.hepsiburada.com/magaza/paspas-love",
        "https://www.hepsiburada.com/magaza/fatihticaret",
        "https://www.hepsiburada.com/magaza/fatofotofan",
        "https://www.hepsiburada.com/magaza/bagand",
        "https://www.hepsiburada.com/magaza/zeren-avm",
        "https://www.hepsiburada.com/magaza/woodboor",
        "https://www.hepsiburada.com/magaza/rawels",
        "https://www.hepsiburada.com/magaza/daha-daha-ucuz",
        "https://www.hepsiburada.com/magaza/egem-e%20ticaret",
        "https://www.hepsiburada.com/magaza/nergis-zuccaciye",
        "https://www.hepsiburada.com/magaza/u-a",
        "https://www.hepsiburada.com/magaza/capella-stores",
        "https://www.hepsiburada.com/magaza/ebakbak",
        "https://www.hepsiburada.com/magaza/genesis",
        "https://www.hepsiburada.com/magaza/hayatevde",
        "https://www.hepsiburada.com/magaza/lemmoni",
        "https://www.hepsiburada.com/magaza/baremplastik",
        "https://www.hepsiburada.com/magaza/parlaware",
        "https://www.hepsiburada.com/magaza/m-art-home",
        "https://www.hepsiburada.com/magaza/idealxhome",
        "https://www.hepsiburada.com/magaza/jumbo-turkiye",
        "https://www.hepsiburada.com/magaza/yalcintaspls",
        "https://www.hepsiburada.com/magaza/wellproducts",
        "https://www.hepsiburada.com/magaza/ababamarket",
        "https://www.hepsiburada.com/magaza/yesil-avm",
        "https://www.hepsiburada.com/magaza/revometal",
        "https://www.hepsiburada.com/magaza/gifts-and-more-haci-ali",
        "https://www.hepsiburada.com/magaza/nealirsanalburda",
        "https://www.hepsiburada.com/magaza/inangun-yapi-market",
        "https://www.hepsiburada.com/magaza/ece-tedarik",
        "https://www.hepsiburada.com/magaza/umut-ev-gerecleri"

    ]

    def start_requests(self):
        for url in self.pratikev_urls:
            full_link = f"{url}?siralama=coksatan"
            # full_link = f"https://www.hepsiburada.com/magaza/toyzz-shop"
            req = scrapy.Request(full_link, callback=self.continues, dont_filter=True, headers=self.headers)
            req.cb_kwargs["url"] = url
            yield req

    def continues(self, response, **kwargs):
        url = kwargs["url"]
        slug = url.split("/")[4]

        urls = response.xpath("//div[@class='box product  hb-placeholder']/a/@href").getall()
        detail_url = f"https://www.hepsiburada.com{urls[0]}"

        self.urls.append(detail_url)

        infos = response.xpath("//div[@class='merchant-information']/div/div/script/text()").get()
        try:
            kep2 = [i.split("kep")[1].replace('":"', '').replace('","', '') for i in infos.split("mersisNumber")[:1]][0]
            kep = kep2 + 'kep.tr'
        except:
            kep = None
        try:
            mersis = \
                [i.split("mersisNumber")[1].replace('":"', '').replace('","', '') for i in
                 infos.split("merchantType")[:1]][
                    0]
        except:
            mersis = None

        try:
            merchant_score = float(response.xpath("//div[@data-testid='rating']/text()").get().replace(",", "."))
        except:
            merchant_score = None

        try:
            city = [i.split("city")[1].replace('":"', '').replace('","', '') for i in infos.split("profession")[:1]]
            m_city = city[0].capitalize()
        except:
            m_city = None
        try:
            name = [i.split("legalName")[1].replace('":"', '').replace('","', '') for i in infos.split("tagList")[:1]]
            m_name = name[0].lower()
        except:
            try:
                name2 = [i.split("nameAndSurname")[1].replace('":"', '').replace('","', '') for i in
                         infos.split("legalName")[:1]]
                m_name = name2[0].capitalize()
            except:
                m_name = None

        self.output.append({
            "merchant_slug": slug,
            "merchant_score": merchant_score,
            "m_name": m_name,
            "email": kep,
            "mersis_no": mersis,
            "city": m_city,
        })

    def close(self, spider, reason):
        # with open(f"data/step_7_category_oyuncak_product_url.json", "w", encoding="utf-8") as f:
        #     json.dump(self.urls, f, ensure_ascii=False)

        with open(f"data/step_7_category_pratikev_product_url.json", "w", encoding="utf-8") as f:
            json.dump(self.urls, f, ensure_ascii=False)

        # with open(f"data/step_7_category_oyuncak_company_detail.json", "w", encoding="utf-8") as f:
        #     json.dump(self.output, f, ensure_ascii=False)

        with open(f"data/step_7_category_pratikev_company_detail.json", "w", encoding="utf-8") as f:
            json.dump(self.output, f, ensure_ascii=False)


process = CrawlerProcess()
process.crawl(crawl)
process.start()

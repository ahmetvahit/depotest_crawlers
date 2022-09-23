from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
from bs4 import BeautifulSoup


class Hepsiburada:
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        chrome_options=self.browserProfile)

        self.output = []
        self.obb: str = None


        self.api_basket_headers = {
            'authority': 'checkout.hepsiburada.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'tr,en-US;q=0.9,en;q=0.8',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjE0NDA1OTksImV4cCI6MTY2MTY5OTc5OSwiaWF0IjoxNjYxNDQwNTk5LCJVc2VySWQiOiI2OTkwNzMyMi04ODM2LTRmNDUtYjQ1ZC04MzQ3NjNhZTc5MWEiLCJUaXRsZSI6IkFobWV0IFNhbGloIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlNhbGloIiwiRW1haWwiOiJzYWxpaGJleTM0MjZAZ21haWwuY29tIiwiSXNBdXRoZW50aWNhdGVkIjoiVHJ1ZSIsIkFwcEtleSI6IkFGN0YyQTM3LUNDNEItNEYxQy04N0ZELUZGMzY0MkY2N0VDQiIsIlByb3ZpZGVyIjoiR29vZ2xlIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJwIjp7InQiOltdfX0.VZREMsHmGi_UbZTsmGFczDd2z5FOKmNGYqybmjRk8Dg',
            'client-id': '47b14cfb-2cad-471a-85de-ebe4684ee95f',
            'content-type': 'application/json; charset=UTF-8',
            'origin': 'https://www.hepsiburada.com',
            'referer': 'https://www.hepsiburada.com/family-simple-tuylu-kedi-oyuncagi-yurt-disindan-p-HBCV00000ICR42?magaza=Family%20Simple',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'tenant-id': 'cc7c5241-6017-44b2-9528-93c8d8907efb',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'withcredentials': 'true',
        }
        self.json_data_basket = {
            'product': {
                'metadata': {
                    'sku': '',
                    'listingId': '',
                    'imageUrl': '',
                    'name': '',
                },
                'quantity': '1',
                'origin': 'SfProductDetail',
            },
        }

    def addbasket(self):  # Json da kayıtlı olan sku ve listingId leri API yoluyla sepete ekleme

        adds = open("data/step_8_oyuncak_basket_Hepsiburada.json", encoding="utf-8").read()
        # adds = open("data/step_8_pratikev_basket_Hepsiburada.json", encoding="utf-8").read()

        # adds = open("data/step_5_Hepsiburada.json", encoding="utf-8").read()

        adds = open("data/hepsiburada_products.json", encoding="utf-8").read()
        add = json.loads(adds)
        try:
            for d in add[1450:1500]:
                sku = d["sku"]
                listing_id = d["listingId"]

                _js = self.json_data_basket
                _js["product"]["metadata"]["sku"] = f"{sku}"
                _js["product"]["metadata"]["listingId"] = f"{listing_id}"

                requests.put('https://checkout.hepsiburada.com/api/basket', headers=self.api_basket_headers, json=_js)
        except:
            pass

    def logIn(self):

        self.browser.maximize_window()
        basket = 'https://www.hepsiburada.com/uyelik/giris?ReturnUrl=https%3A%2F%2Fcheckout.hepsiburada.com%2Fsepetim'
        # basket = "https://giris.hepsiburada.com/"
        self.browser.get(f"{basket}")
        time.sleep(3)
        self.browser.execute_script("window.scrollBy(0,450)")
        self.browser.find_element(By.ID, 'btnGoogle').click()
        time.sleep(1)
        self.browser.find_element(By.ID, 'identifierId').send_keys("" + Keys.ENTER)
        time.sleep(2)
        try:
            self.browser.find_element(By.XPATH, "//input[@type='password']").send_keys("" + Keys.ENTER)
        except:
            pass

    def order_status(self):
        time.sleep(10)
        try:  # Kişiye özel kupa da isim yazılmadan geçilmiyor isim bilgisi gönderildi
            self.browser.find_element(By.XPATH, '//div[@class="input_outer_1QKx4"]/input').send_keys("d" + Keys.ENTER)
        except:
            pass
        time.sleep(5)
        # basket = "https://checkout.hepsiburada.com/sepetim"
        # self.browser.get(f"{basket}")
        self.browser.find_element(By.ID, 'continue_step_btn').click()
        time.sleep(8)
        # self.browser.find_element(By.ID, 'continue_step_btn').click()
        # time.sleep(9)
        try:  # Havale ödemeler için
            self.browser.find_element(By.XPATH, '//*[@id="payment-money-transfer"]/div/div[1]/div[1]/div[1]/label/input').click()
            time.sleep(2)
        except:
            pass
            # self.browser.find_element(By.XPATH,
            #                           '//*[@id="payment-money-transfer"]/div/div[1]/div[1]/div[2]/div').click()
            #self.browser.find_element(By.ID, 'continue_step_btn').click()
        # except:  # Havalenin olmadığı yerde kart ödemesi için
        #     self.browser.find_element(By.XPATH, '//*[@id="payment-methods"]/div/div[1]').click()
        #     self.browser.find_element(By.XPATH, '//input[@name="cardNumber"]').send_keys(
        #         "4355084355084358" + Keys.ENTER)
        #     self.browser.find_element(By.XPATH, '//input[@name="holderName"]').send_keys("Akbank" + Keys.ENTER)
        #     self.browser.find_element(By.XPATH, '//input[@name="expireDate"]').send_keys("12/26" + Keys.ENTER)
        #     time.sleep(4)
        #     self.browser.find_element(By.XPATH, '//input[@name="cvv"]').send_keys("000" + Keys.ENTER)
        #     time.sleep(4)
        #     try:  # Kart ödemesi yaparken koşulu kabul etme buton1
        #         self.browser.find_element(By.XPATH, '//div[@id="agreement_check"]/label/input').click()
        #         time.sleep(2)
        #     except:
        #         pass
            # try:  # Kart ödemesi yaparken koşulu kabul etme buton2
            #     self.browser.find_element(By.ID, 'walletSelected').click()
            # except:
            #     pass
            # self.browser.find_element(By.ID, 'continue_step_btn').click()

    @staticmethod
    def prepare_urls():
        # data = open("data/step_4_merchant_company_details_Hepsiburada.json", encoding="utf-8").read()
        data = open("data/step_7_category_oyuncak_company_detail.json", encoding="utf-8").read()
        # data = open("data/step_7_category_pratikev_company_detail.json", encoding="utf-8").read()
        data = json.loads(data)
        names = []
        for row in data:
            names.append(row['m_name'])

        names = list(set(names))
        return names

    def contracts(self):
        response1 = requests.get('https://checkout.hepsiburada.com/api/agreement/DistantSales', cookies=self.cookies,
                                 headers=self.headers)
        response2 = requests.get('https://checkout.hepsiburada.com/api/agreement/PreliminaryInformation',
                                 cookies=self.cookies,
                                 headers=self.headers)
        self.obb = response1.json().get("result")

        # TODO MATCHLEME KISMI YAPILACAK------<<<<<<<<
        # Eklenen 10 ürünün satıcılarının name bilgisine göre matchleme

        js = json.loads(response1.text)["result"]

        # # Adres bilgisi
        # adres = js.split(" Adresi:")
        # del adres[0]
        #
        # adress = []
        # for a in adres:
        #     adr = a.split("<br/>")[0].replace("<strong>", "").strip()
        #     adress.append(adr)
        # # Tekrarlanmış adreslerin editlenmesi
        # adress_edit = []
        # for ad in adress:
        #     if ad not in adress_edit:
        #         adress_edit.append(ad)

        # Telefon bilgisini alma
        phones = js.split(" Telefon: </strong>")
        del phones[0]

        mobiles = []
        for p in phones:
            ph = p.split("<br/>")[0].replace("<strong>", "").strip()
            mobiles.append(ph)
        # Tekrarlanmış numaraların editlenmesi
        mobiles_edit = []
        for m in mobiles:
            if m not in mobiles_edit:
                mobiles_edit.append(m)

        # Ünvan bilgisini alma
        titles = js.split(" Ünvanı")
        del titles[0]
        title = []
        for i in titles:
            merc = i.split("<br/>")[0].replace(":", "").strip().lower()
            title.append(merc)

        # Tekrarlanmış isim bilgilerinin editlenmesi
        title_edit = []
        for t in title:
            if t not in title_edit:
                title_edit.append(t)

        names = self.prepare_urls()
        # MatchingName
        merchant_items = []
        for name in names:
            if name in title_edit:
                merchant_items.append(name)

        # with open("data/matching_sellers.json", "w", encoding="utf-8") as f:
        #     json.dump(merchant_items, f, ensure_ascii=False)

        # TODO Alınmış olan telefon numara listesinin,
        # Todo step_7_category_oyuncak_company_detail içerisindeki phone kısmına aktarılması gerekli

        # self.output.append({
        #     "merchant_slug": None,
        #     "email": None,
        #     "mersis_no": None,
        #     "phone": m_phone,
        #     "city": None,
        # })
        #
        # with open("data/step_4_merchant_company_details_Hepsiburada.json", "r+", encoding="utf-8") as f:
        #     json.dump(self.output, f, ensure_ascii=False)

    def extract_merchant_info(self) -> dict:
        # import re
        # _k = re.findall(r"<p>Ünvanı:(.*?)</p>(.*?)", self.obb.replace("\n", ""), re.MULTILINE)
        # print(_k)
        # merchants = []
        # for k in _k:
        #     merc = k[0].strip().split('<br>')
        #
        #     buffer = {}
        #     for m in merc:
        #         "Ünvanı: " + merc[0].strip()
        #         bits = m.strip().split(':')
        #         try:
        #             buffer[bits[0]] = bits[1].strip()
        #         except:
        #             pass
        #         merchants.append(m)
        # return merchants

        dom = BeautifulSoup(self.obb, "html.parser")
        merchants = []
        for el in dom.findAll("p"):
            if el.text.startswith("Ünvanı:"):
                buffer = {}
                for line in el.text.split("\n"):
                    bits = line.strip().split(':')
                    try:
                        # print(bits)
                        buffer[bits[0]] = bits[1].strip()
                    except:
                        print('buffer hata')
                merchants.append(buffer)
        with open("data/merchants_part30_Hepsiburada.json", "w", encoding="utf-8") as f:
            json.dump(merchants, f, ensure_ascii=False)
        return merchants

    def close(self):
        self.browser.close()


hb = Hepsiburada()
hb.addbasket()
hb.logIn()
hb.order_status()
hb.contracts()
hb.extract_merchant_info()
hb.close()

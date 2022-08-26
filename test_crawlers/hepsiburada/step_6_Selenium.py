from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

class Hepsiburada:
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        chrome_options=self.browserProfile)

        self.output = []
        self.cookies = {
            'bm_sz': 'B5A9EB0B76B27597B23B36452DEBAF14~YAAQVm7UFzDJM8qCAQAAMrY21BDSzFyxu8m3/sr37jByTDuMM4jIYWdZs4psnAbKZUQX2f/B1VKeuyev4xrenYUpjwkBIcZEDOv1b1wBJlVF9Igmnu8HyVk7x5QjSKiS9YpUEJicNjdvvtvegaE/eZ2mNN123prbIu50NAnJe3yAJnHFCmVdTom9J8eYtvD1odKtHyy9c0ahJNQJpWHfLG8XyPOn0lDln6nZuGe4IeLnKbPgo2gXh21JBNvldmQzFk3O8dMMw1IZyuMmoAofVey8Jrl8lvZjEFvmoV1H9PThjPKa2yEX0g==~3687476~3683896',
            'wt3_sid': '%3B289941511384204',
            '_gcl_au': '1.1.1556782419.1661417733',
            'hbus_anonymousId': 'ac8d8d61-0ee0-488e-b4c7-c312e61ad2c2',
            '_gid': 'GA1.2.2081015239.1661417733',
            '_ga': 'GA1.2.343949682.1661417733',
            '_fbp': 'fb.1.1661417733928.146492714',
            'cto_bundle': 'pn3INV9PaW8wNE1xeFFmcFl6czAzaXNCamlmNUFzSnlxWmpvb2JrRGxyMGNya3JwM3RxNzA1NXFoM3hlN0t6UUdHNVgzazcxcDk0Sm5aOWdjcGVGYnRoQW56WjVqYmF6Y1dXYnlZTkNhOEl3ZXdocVJsSW9admVvZVUlMkJSQVJzZiUyRlclMkZNUjUzZzEyWUFlUjA4aElVTjJWTjJnTmclM0QlM0Q',
            '_tt_enable_cookie': '1',
            '_ttp': 'a53010bf-8241-46b5-8fe4-b7e934698a6f',
            'ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec': '%7B%22g%22%3A%227ad9ed6d-3775-b160-d101-cf395d2a7976%22%2C%22e%22%3A1661419534308%2C%22c%22%3A1661417734308%2C%22l%22%3A1661417734308%7D',
            'ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec': '%7B%22g%22%3A%22701a2df8-629f-ac9f-fe65-01d93500a553%22%2C%22c%22%3A1661417734309%2C%22l%22%3A1661417734309%7D',
            'cookieconsentanon': 'false%7C25.08.2022%2011%3A55%3A39',
            '_hjFirstSeen': '1',
            '_hjSession_216130': 'eyJpZCI6IjA3N2RlMTZkLWM1MTItNDViNC1iOTM2LWI0NDBhMmRkMGFkNCIsImNyZWF0ZWQiOjE2NjE0MTc3Mzk0NTQsImluU2FtcGxlIjpmYWxzZX0=',
            '_hjAbsoluteSessionInProgress': '1',
            'AKA_A2': 'A',
            '_ga_44CSPTX731': 'GS1.1.1661417733.1.1.1661417746.47.0.0',
            '_dgr_top_parent_category': '',
            '_hjSessionUser_216130': 'eyJpZCI6IjYyM2U3MGQ4LTFmNTItNTMxNi04OTE3LWYzMWJjZGJhOGY3NCIsImNyZWF0ZWQiOjE2NjE0MTc3Mzk0NDQsImV4aXN0aW5nIjp0cnVlfQ==',
            'wt_fa': 'lv~1661417747086|1692521747086#cv~1|1692521747086#fv~2022-08|1692521747086#',
            '__gads': 'ID=8fd492dd65f90f2b:T=1661417746:S=ALNI_MYSI7feoH2inx9bdKd7ZTbcqcS6Tw',
            '__gpi': 'UID=00000af7f536b0ee:T=1661417746:RT=1661417746:S=ALNI_MYQw9pqUTZ2rpUtQHsvFq8_FGUyfA',
            'lazyContinueUrl': 'https://checkout.hepsiburada.com/teslimat',
            'auth': '96F60710A8D7A007F3466F25C3308D62EBD6019A1A9A672104B2492A00767D69F233BDAE26CC13FDD9C6C5F8DD8FF3BC42B59F892AF1B885F8E22B68D6C965048D3D3CF48D2A029CC32B4FA5082B768BE2AC1E8333707172141E8F6E909BC7153F6ABC77C08794D9B468D451C757575FA2A9F37207B2E590C01D54908882A8C28855066F6ADC65A56EA9132049122EE6572352835EEFD0169238850A3327CA5B90CE80CB9F6DDB0847431846AEE46E33D08F7BF71BE7409FDA58D2FF01A9366009C1FE804CD2015E7F0DAC464BD8526BAB3F5F0989BAFACE0CE362498787EB76300F53A1F775B18CCF06D6233581A8CAA298EFBA420F92329D24E94D066B149E0DF22E1EB862DA9CDF872258AB654122C2B94CC25814544F050AC10B0C7874E48F203CB29C3B1458F284CBE98DC32F0241291F26EA79C2137C184602531CA3FDF0B241F4643EFB8BDFE15F6E26039F6F00154C8AB346069DBE1CBC2B27B5B12C28E8D67AA90ED164419EA1BACAF56CDBC1B8EE3F0207A666701DAC0760488A29D7BC680C6B2A1723C812B645B719D50BF7D36C50AFCDFBF3DD63006E1499DD77252E45051603C99B574EDC379E4FB1EB228922AA6D52459078DA0CCBC6874CD5093BD5DA70672BF4C482D347C2A98AA3FA91106551825CBC75302C8C944362D89CD4A05E50B29E85E2D3CD8F60A1DAB8468C4D617B5CDE353BE84A43D41DF423345A4ED380F168A38924E1D5BC13D2A1EF6C45E177A9AB3AC363736D41ED36E662CACFECD445AD84EF321F6B252F5A237B7439A559DCD3D0A1840010E0BFACBFE21E086306B971931CB1026252F3C1EF8F59FFA0300236A84C425F0CACF397D516420BC8D1CC5C5EF7373E03717A5DF4C2E844B382EA68BDCBC3A4921644A8CEE5FA7480320BC778B46BFD61F51EB467796D0A2404604ABC7D1DCA7B432A2774',
            'anon': 'BF26169CAD1211D086F3699D383CC3D7CF051CA891D0D2F94F352375E982C2BD03177F765F55BF464F9EE37F45E4D65F3E63C62A5F9426D9F800C6D12E9090074812614A34B6B9AE7E5A3B90DFBB98886A61EB365604EA6E0C99FEB3C1C4A0BE9AB0CB1B202DAFB238C11862394E00DE301BC5040F19DD076FBC472472E48987382E8266570918C237EBB2B05107FD0E3B452AC8327FECB23C86B9FAFF3F5D3B84F2D086A2B655D4CAFE3C09C4B8F6796BFF5400BCA606A7CA966E06FBBD138A2415A7619C7F7F8918AF2C8A5FD186A1400867C4C21134AF864F863F527D7202134A1C2DDD20E3E33BC38036B8797DEE266B7C8C1495CC76DB19943E5ED494722CDE3A30E8803412DA9ED6A2E3EFE30529FB4C4203A322F12F1A62BE173BB23DFA7766495161F2B7ABEA7AFEF4DB7023AE18C4A4385A1C73DF5ADAAFB4B51D62AD8090ACB64C5B256FFC8DCE',
            'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjE0MTc3NjcsImV4cCI6MTY2MTY3Njk2NywiaWF0IjoxNjYxNDE3NzY3LCJVc2VySWQiOiI2OTkwNzMyMi04ODM2LTRmNDUtYjQ1ZC04MzQ3NjNhZTc5MWEiLCJUaXRsZSI6IkFobWV0IFNhbGloIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlNhbGloIiwiRW1haWwiOiJzYWxpaGJleTM0MjZAZ21haWwuY29tIiwiSXNBdXRoZW50aWNhdGVkIjoiVHJ1ZSIsIkFwcEtleSI6IkFGN0YyQTM3LUNDNEItNEYxQy04N0ZELUZGMzY0MkY2N0VDQiIsIlByb3ZpZGVyIjoiR29vZ2xlIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJwIjp7InQiOltdfX0.RHlHo1hws_55wlRMrVyTHNdtx4zYAuQhjMEi17Nb4ZI',
            'eJwt': 'ttT1DojhgOUTOBUmIS%2BAJrQegpHCWh25Zea3HeCiHlY4v5POtvZIJo2VHixqnc1rB%2FvIBaSPu4yR558ebq2Ak04tGGhH%2BhyringjseIoPZ%2Bfs1TnDSniTgMQjW1ofGTHkMc%2F5VQAp514axoh%2F85AscLS%2FI%2Bb%2BHvf%2F%2BEchqw2ikW6r0xUs6vO89JpX54KVa5Bjpx1VE4mjncE2oNKz6aGRrQ4grItH3jQt3%2FVLLR6EzIepG%2F%2BINELe5SUzSbRMGc7SqE8rXu0Y33Yv2tdBt7ZD7FG2BRLfokiCsWFbMNZEzX4Lx2Oh3vPTQYdCt0eZPi%2F00gW8R92aHYzZul1%2BJpZlRQX%2Fu1l7amEnSrtbWMeoazTAhF6LLFJi8US8p85BwFKe5nkVaZX9dAhX0ZTJNPPrQEWEOFVoeX2N89R0btVpwYskwIgiixiN3t%2FxdZqx8Vn%2FMicWmxZjsH6WASwPsxZxeXzF60ay0oCJFbacwrZZ2w8tu2F%2FbwVq1jyQpD3eJ%2FS0NjiQt9eOwpavC0cFULpegq6uFn1j%2FYtvyf7tX%2BMwz%2BGKfJ%2FV4GhBRfdzC4YsL%2B9DUpErQKDze8mDne7WEf7rJYyBVRVHBpCeKN7mPnXPl0XBoUBR7kY1O%2BAiTAvFMmPDuRXJFWa6Wr6hrVD60nvFLCxJnQBqFnjHJYoSrwtlQZo5oflY7HSPDOSrm2ILfFf',
            'cookieconsentauth': 'true',
            'loginType': 'SignIn',
            '_hjIncludedInSessionSample': '0',
            '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IlVzZXIgSWQiOiI2OTkwNzMyMi04ODM2LTRmNDUtYjQ1ZC04MzQ3NjNhZTc5MWEifSwidXNlcklkIjoiMjE2MTMwIn0=',
            'RT': '"z=1&dm=hepsiburada.com&si=5k2st704p9c&ss=l78t89nr&sl=0&tt=0"',
            'hbus_sessionId': '877319ae-36b4-4cb2-a992-0d7c35354166%7C1661419830970',
            'wt3_eid': '%3B289941511384204%7C2166141773200280806%232166141803000819268',
            'wt_fa_s': 'start~1|1692954030977#',
            '_abck': '271E097775D13EF27E57061DD72E2581~-1~YAAQRm7UF71TC9KCAQAAcFo71AiFY7awUykNengT6RnXaKCpmCPwWq+7k7oE5IQOMIZnNsxsAv0UIEOYYK/ODoTTS3BVzxKWeagIw7cDUZRL3jR40/fgDTAET3mWtwP/QiFd3wC3GxzpdlNAraEU1SGkAjxaop6MckteE6fyGduJuuqvLBh98jCZBC/Oyh6tyOjheOCaCHFbHb1qnTFK9yPZ9EbrQCWpaElOCXPHIYiuWE1IigGaJ3GCSQGw4F72efeLjqo9PD5dh33IFWZtNAVd6pXi0/1cXuJki1gSqcRNnfsNOIXFL0tAmFzONVkxtFNuCDXOioEubdK9GVO6cDshghToNQ5AmvMIrnOMcvxoRKWEeycAYWz8gcDvId+tGUWTmkAmrJVIxZEsKxlq~-1~-1~-1',
        }
        self.headers = {
            'authority': 'checkout.hepsiburada.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en,en_US;q=0.9',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjE0MTc3NjcsImV4cCI6MTY2MTY3Njk2NywiaWF0IjoxNjYxNDE3NzY3LCJVc2VySWQiOiI2OTkwNzMyMi04ODM2LTRmNDUtYjQ1ZC04MzQ3NjNhZTc5MWEiLCJUaXRsZSI6IkFobWV0IFNhbGloIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlNhbGloIiwiRW1haWwiOiJzYWxpaGJleTM0MjZAZ21haWwuY29tIiwiSXNBdXRoZW50aWNhdGVkIjoiVHJ1ZSIsIkFwcEtleSI6IkFGN0YyQTM3LUNDNEItNEYxQy04N0ZELUZGMzY0MkY2N0VDQiIsIlByb3ZpZGVyIjoiR29vZ2xlIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJwIjp7InQiOltdfX0.RHlHo1hws_55wlRMrVyTHNdtx4zYAuQhjMEi17Nb4ZI',
            'client-id': '47b14cfb-2cad-471a-85de-ebe4684ee95f',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'bm_sz=B5A9EB0B76B27597B23B36452DEBAF14~YAAQVm7UFzDJM8qCAQAAMrY21BDSzFyxu8m3/sr37jByTDuMM4jIYWdZs4psnAbKZUQX2f/B1VKeuyev4xrenYUpjwkBIcZEDOv1b1wBJlVF9Igmnu8HyVk7x5QjSKiS9YpUEJicNjdvvtvegaE/eZ2mNN123prbIu50NAnJe3yAJnHFCmVdTom9J8eYtvD1odKtHyy9c0ahJNQJpWHfLG8XyPOn0lDln6nZuGe4IeLnKbPgo2gXh21JBNvldmQzFk3O8dMMw1IZyuMmoAofVey8Jrl8lvZjEFvmoV1H9PThjPKa2yEX0g==~3687476~3683896; wt3_sid=%3B289941511384204; _gcl_au=1.1.1556782419.1661417733; hbus_anonymousId=ac8d8d61-0ee0-488e-b4c7-c312e61ad2c2; _gid=GA1.2.2081015239.1661417733; _ga=GA1.2.343949682.1661417733; _fbp=fb.1.1661417733928.146492714; cto_bundle=pn3INV9PaW8wNE1xeFFmcFl6czAzaXNCamlmNUFzSnlxWmpvb2JrRGxyMGNya3JwM3RxNzA1NXFoM3hlN0t6UUdHNVgzazcxcDk0Sm5aOWdjcGVGYnRoQW56WjVqYmF6Y1dXYnlZTkNhOEl3ZXdocVJsSW9admVvZVUlMkJSQVJzZiUyRlclMkZNUjUzZzEyWUFlUjA4aElVTjJWTjJnTmclM0QlM0Q; _tt_enable_cookie=1; _ttp=a53010bf-8241-46b5-8fe4-b7e934698a6f; ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%227ad9ed6d-3775-b160-d101-cf395d2a7976%22%2C%22e%22%3A1661419534308%2C%22c%22%3A1661417734308%2C%22l%22%3A1661417734308%7D; ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%22701a2df8-629f-ac9f-fe65-01d93500a553%22%2C%22c%22%3A1661417734309%2C%22l%22%3A1661417734309%7D; cookieconsentanon=false%7C25.08.2022%2011%3A55%3A39; _hjFirstSeen=1; _hjSession_216130=eyJpZCI6IjA3N2RlMTZkLWM1MTItNDViNC1iOTM2LWI0NDBhMmRkMGFkNCIsImNyZWF0ZWQiOjE2NjE0MTc3Mzk0NTQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; AKA_A2=A; _ga_44CSPTX731=GS1.1.1661417733.1.1.1661417746.47.0.0; _dgr_top_parent_category=; _hjSessionUser_216130=eyJpZCI6IjYyM2U3MGQ4LTFmNTItNTMxNi04OTE3LWYzMWJjZGJhOGY3NCIsImNyZWF0ZWQiOjE2NjE0MTc3Mzk0NDQsImV4aXN0aW5nIjp0cnVlfQ==; wt_fa=lv~1661417747086|1692521747086#cv~1|1692521747086#fv~2022-08|1692521747086#; __gads=ID=8fd492dd65f90f2b:T=1661417746:S=ALNI_MYSI7feoH2inx9bdKd7ZTbcqcS6Tw; __gpi=UID=00000af7f536b0ee:T=1661417746:RT=1661417746:S=ALNI_MYQw9pqUTZ2rpUtQHsvFq8_FGUyfA; lazyContinueUrl=https://checkout.hepsiburada.com/teslimat; auth=96F60710A8D7A007F3466F25C3308D62EBD6019A1A9A672104B2492A00767D69F233BDAE26CC13FDD9C6C5F8DD8FF3BC42B59F892AF1B885F8E22B68D6C965048D3D3CF48D2A029CC32B4FA5082B768BE2AC1E8333707172141E8F6E909BC7153F6ABC77C08794D9B468D451C757575FA2A9F37207B2E590C01D54908882A8C28855066F6ADC65A56EA9132049122EE6572352835EEFD0169238850A3327CA5B90CE80CB9F6DDB0847431846AEE46E33D08F7BF71BE7409FDA58D2FF01A9366009C1FE804CD2015E7F0DAC464BD8526BAB3F5F0989BAFACE0CE362498787EB76300F53A1F775B18CCF06D6233581A8CAA298EFBA420F92329D24E94D066B149E0DF22E1EB862DA9CDF872258AB654122C2B94CC25814544F050AC10B0C7874E48F203CB29C3B1458F284CBE98DC32F0241291F26EA79C2137C184602531CA3FDF0B241F4643EFB8BDFE15F6E26039F6F00154C8AB346069DBE1CBC2B27B5B12C28E8D67AA90ED164419EA1BACAF56CDBC1B8EE3F0207A666701DAC0760488A29D7BC680C6B2A1723C812B645B719D50BF7D36C50AFCDFBF3DD63006E1499DD77252E45051603C99B574EDC379E4FB1EB228922AA6D52459078DA0CCBC6874CD5093BD5DA70672BF4C482D347C2A98AA3FA91106551825CBC75302C8C944362D89CD4A05E50B29E85E2D3CD8F60A1DAB8468C4D617B5CDE353BE84A43D41DF423345A4ED380F168A38924E1D5BC13D2A1EF6C45E177A9AB3AC363736D41ED36E662CACFECD445AD84EF321F6B252F5A237B7439A559DCD3D0A1840010E0BFACBFE21E086306B971931CB1026252F3C1EF8F59FFA0300236A84C425F0CACF397D516420BC8D1CC5C5EF7373E03717A5DF4C2E844B382EA68BDCBC3A4921644A8CEE5FA7480320BC778B46BFD61F51EB467796D0A2404604ABC7D1DCA7B432A2774; anon=BF26169CAD1211D086F3699D383CC3D7CF051CA891D0D2F94F352375E982C2BD03177F765F55BF464F9EE37F45E4D65F3E63C62A5F9426D9F800C6D12E9090074812614A34B6B9AE7E5A3B90DFBB98886A61EB365604EA6E0C99FEB3C1C4A0BE9AB0CB1B202DAFB238C11862394E00DE301BC5040F19DD076FBC472472E48987382E8266570918C237EBB2B05107FD0E3B452AC8327FECB23C86B9FAFF3F5D3B84F2D086A2B655D4CAFE3C09C4B8F6796BFF5400BCA606A7CA966E06FBBD138A2415A7619C7F7F8918AF2C8A5FD186A1400867C4C21134AF864F863F527D7202134A1C2DDD20E3E33BC38036B8797DEE266B7C8C1495CC76DB19943E5ED494722CDE3A30E8803412DA9ED6A2E3EFE30529FB4C4203A322F12F1A62BE173BB23DFA7766495161F2B7ABEA7AFEF4DB7023AE18C4A4385A1C73DF5ADAAFB4B51D62AD8090ACB64C5B256FFC8DCE; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjE0MTc3NjcsImV4cCI6MTY2MTY3Njk2NywiaWF0IjoxNjYxNDE3NzY3LCJVc2VySWQiOiI2OTkwNzMyMi04ODM2LTRmNDUtYjQ1ZC04MzQ3NjNhZTc5MWEiLCJUaXRsZSI6IkFobWV0IFNhbGloIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlNhbGloIiwiRW1haWwiOiJzYWxpaGJleTM0MjZAZ21haWwuY29tIiwiSXNBdXRoZW50aWNhdGVkIjoiVHJ1ZSIsIkFwcEtleSI6IkFGN0YyQTM3LUNDNEItNEYxQy04N0ZELUZGMzY0MkY2N0VDQiIsIlByb3ZpZGVyIjoiR29vZ2xlIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJwIjp7InQiOltdfX0.RHlHo1hws_55wlRMrVyTHNdtx4zYAuQhjMEi17Nb4ZI; eJwt=ttT1DojhgOUTOBUmIS%2BAJrQegpHCWh25Zea3HeCiHlY4v5POtvZIJo2VHixqnc1rB%2FvIBaSPu4yR558ebq2Ak04tGGhH%2BhyringjseIoPZ%2Bfs1TnDSniTgMQjW1ofGTHkMc%2F5VQAp514axoh%2F85AscLS%2FI%2Bb%2BHvf%2F%2BEchqw2ikW6r0xUs6vO89JpX54KVa5Bjpx1VE4mjncE2oNKz6aGRrQ4grItH3jQt3%2FVLLR6EzIepG%2F%2BINELe5SUzSbRMGc7SqE8rXu0Y33Yv2tdBt7ZD7FG2BRLfokiCsWFbMNZEzX4Lx2Oh3vPTQYdCt0eZPi%2F00gW8R92aHYzZul1%2BJpZlRQX%2Fu1l7amEnSrtbWMeoazTAhF6LLFJi8US8p85BwFKe5nkVaZX9dAhX0ZTJNPPrQEWEOFVoeX2N89R0btVpwYskwIgiixiN3t%2FxdZqx8Vn%2FMicWmxZjsH6WASwPsxZxeXzF60ay0oCJFbacwrZZ2w8tu2F%2FbwVq1jyQpD3eJ%2FS0NjiQt9eOwpavC0cFULpegq6uFn1j%2FYtvyf7tX%2BMwz%2BGKfJ%2FV4GhBRfdzC4YsL%2B9DUpErQKDze8mDne7WEf7rJYyBVRVHBpCeKN7mPnXPl0XBoUBR7kY1O%2BAiTAvFMmPDuRXJFWa6Wr6hrVD60nvFLCxJnQBqFnjHJYoSrwtlQZo5oflY7HSPDOSrm2ILfFf; cookieconsentauth=true; loginType=SignIn; _hjIncludedInSessionSample=0; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7IlVzZXIgSWQiOiI2OTkwNzMyMi04ODM2LTRmNDUtYjQ1ZC04MzQ3NjNhZTc5MWEifSwidXNlcklkIjoiMjE2MTMwIn0=; RT="z=1&dm=hepsiburada.com&si=5k2st704p9c&ss=l78t89nr&sl=0&tt=0"; hbus_sessionId=877319ae-36b4-4cb2-a992-0d7c35354166%7C1661419830970; wt3_eid=%3B289941511384204%7C2166141773200280806%232166141803000819268; wt_fa_s=start~1|1692954030977#; _abck=271E097775D13EF27E57061DD72E2581~-1~YAAQRm7UF71TC9KCAQAAcFo71AiFY7awUykNengT6RnXaKCpmCPwWq+7k7oE5IQOMIZnNsxsAv0UIEOYYK/ODoTTS3BVzxKWeagIw7cDUZRL3jR40/fgDTAET3mWtwP/QiFd3wC3GxzpdlNAraEU1SGkAjxaop6MckteE6fyGduJuuqvLBh98jCZBC/Oyh6tyOjheOCaCHFbHb1qnTFK9yPZ9EbrQCWpaElOCXPHIYiuWE1IigGaJ3GCSQGw4F72efeLjqo9PD5dh33IFWZtNAVd6pXi0/1cXuJki1gSqcRNnfsNOIXFL0tAmFzONVkxtFNuCDXOioEubdK9GVO6cDshghToNQ5AmvMIrnOMcvxoRKWEeycAYWz8gcDvId+tGUWTmkAmrJVIxZEsKxlq~-1~-1~-1',
            'referer': 'https://checkout.hepsiburada.com/siparis-ozeti',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'tenant-id': 'cc7c5241-6017-44b2-9528-93c8d8907efb',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
            'withcredentials': 'true',
        }

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

    def inUrl(self):

        adds = open("data/step_5_Hepsiburada.json", encoding="utf-8").read()
        add = json.loads(adds)
        for d in add:
            sku = d["merchantId"]
            listing_id = d["listingId"]

            _js = self.json_data_basket
            _js["product"]["metadata"]["sku"] = f"{sku}"
            _js["product"]["metadata"]["listingId"] = f"{listing_id}"

            requests.put('https://checkout.hepsiburada.com/api/basket', headers=self.api_basket_headers, json=_js)
        time.sleep(7)

        self.browser.maximize_window()
        basket = 'https://www.hepsiburada.com/uyelik/giris?ReturnUrl=https%3A%2F%2Fcheckout.hepsiburada.com%2Fsepetim'
        self.browser.get(f"{basket}")
        time.sleep(2)
        self.browser.find_element(By.ID, 'btnGoogle').click()
        time.sleep(3)
        self.browser.find_element(By.ID, 'identifierId').send_keys("salihbey3426@gmail.com" + Keys.ENTER)
        time.sleep(3)
        self.browser.find_element(By.XPATH, "//input[@type='password']").send_keys("ahmetsalih1234" + Keys.ENTER)
        time.sleep(10)

        self.browser.find_element(By.ID, 'continue_step_btn').click()
        time.sleep(5)
        self.browser.find_element(By.ID, 'continue_step_btn').click()
        time.sleep(5)
        self.browser.find_element(By.XPATH, '//*[@id="payment-methods"]/div/div[2]/div[1]/div[1]/div').click()
        time.sleep(7)
        self.browser.find_element(By.XPATH, '//*[@id="payment-money-transfer"]/div/div[1]/div[1]/div[2]/div').click()
        time.sleep(3)
        self.browser.find_element(By.ID, 'continue_step_btn').click()
        time.sleep(5)
        time.sleep(3)
        response1 = requests.get('https://checkout.hepsiburada.com/api/agreement/DistantSales', cookies=self.cookies,
                                 headers=self.headers)
        response2 = requests.get('https://checkout.hepsiburada.com/api/agreement/PreliminaryInformation', cookies=self.cookies,
                               headers=self.headers)
        print('hi')
        # TODO MATCHLEME KISMI YAPILACAK------<<<<<<<<
        # TODO MATCHLEME KISMI YAPILACAK------<<<<<<<<
        # Eklenen 10 ürünün satıcılarının name bilgisine göre matchleme
        js = json.loads(response2.text)["result"]
        jk = js.split(" Ünvanı")
        del jk[0]
        del jk[0]
        del jk[1]
        del jk[2]
        del jk[3]
        del jk[4]
        del jk[5]
        del jk[6]
        del jk[7]
        del jk[8]
        del jk[9]
        # [i.split("<br/>") for i in jk]
        list = []
        for i in jk:
            merc = i.split("<br/>")[0].replace(":", "").strip().capitalize()
            list.append(merc)

        try:
            jss = json.loads(response1.text)["result"]
            mobile = [i.split("Telefon")[1].replace(":", "") for i in jss.split("Fax")[:1]][0]
            m_phone = mobile.strip().split("\n")[0]
        except:
            m_phone = None
        # js = json.loads(response2.text)["result"]

        self.output.append({
            "merchant_slug": None,
            "email": None,
            "mersis_no": None,
            "phone": m_phone,
            "city": None,
        })

        with open("data/step_4_merchant_company_details_Hepsiburada.json", "r+", encoding="utf-8") as f:
            json.dump(self.output, f, ensure_ascii=False)

    def close(self):
        self.browser.close()


stap = Hepsiburada()
stap.inUrl()
stap.close()

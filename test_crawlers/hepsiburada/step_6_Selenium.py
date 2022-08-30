from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import collections


class Hepsiburada:
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        chrome_options=self.browserProfile)

        self.output = []

        self.cookies = {
            'bm_sz': '65AE6AADC78AE8781BD07B2686BEB780~YAAQX27UF9hINOWCAQAA+l9G6BBM6H7FOpwOmf6Ruu809iNm3Hav6JGjcBkzfY4/R/ok4/kHFvYRO+BoKqMeJ54STf65f+HFX3tWFsomc+CEg0Pflb5Yo8KizhmODewNb/hMaoUUk4VPzBXz64E32RwnrDUkF6KFleLgCPhjOwkONkLhxPORAIKxgOfHTccpPeTjmllxCuEJGYTSw3PzLyg+9ZZ0BlMk9cYcE1auIuucazuesdc0DfAxDY4uE7MwhyhBM6/p0OrLTiqyoVKEzJQ/5tEcXxi0rqeGjeR1dGmR6ZgcnnDqXw==~3617841~4272688',
            'hbus_anonymousId': 'efb3f92d-c57c-49e8-9cac-20c53def19c0',
            'AKA_A2': 'A',
            '_dgr_top_parent_category': '',
            'auth': '45705A82AB521D35F1FA1B6BD2F54AAA0DE517D70CD5983B8C28ED9DB97A85EE3DCDA1300FFE9189C7C8190372F89D7FD1A4BD11D08F695BC6FB727EB59D4D877FA978714E31444B2E84B4C866F5DE3B260407FA51CA5B70C87FFA41066E99B3D418B6127705CE75CF2DA4D92725BF327F635997D9FAF81EA5CF6D8EFD71DDDD9567826349184229A1F554A6EA9299A5C643A2BAEF0A36CF3CED3AB92DEDCAE17B1EF873E6A33550EF7E5FCCDA91B172EA2A7E4EF220D648ECD85DF12FD8C013D905770DA87E244A22EB8D4D917539AD3C9A736BCCE0FCA4C4C9D48406330B3C78BBB1C399B1CEC5B4B42A670516246D31B9FFC26E90A6D7603CC215E0F424E3ED60D1F88666424458C05EE9C16066EF40178E3252CA13DA048BE5834CD3DF81F639435E93C4D575B65DCED4801A4A05F2DB1F9B9234EDD9BCAF1DD094DD79EDCDFCEC8E90FE32CF844AD85D39E5D340D7A3FDC83046BC1DCFBFD8BFBFF40EC3FE509784583703E7AC940D18DB7A188457FD0620338DAEBDC8BFB60CF38BEC5A1B5F52E5BA2EBA1F890DDDDA5D9FB0CE1ECBEFC4E7604366AB1E87E9D3E4EC3DCF870AE93168120F19500F720E2C9A318464C90DA821F36AAC89CA86D4007A038B300725D29E0DECA758EB9AD9F3451FC4896A9198F4FB7E30DD6F178359CC00CDC6ACBB5C6F3B2283AC3262DA0B1EA416416D91B9C05BE1571DF25E495861F7C16C4AE68917C255323A054799CB3152AF7A2F2F664EC664D1AF4295CCBC7059E782A94DD045898F477938B3862E6739675344E268AD6B9677C0EB1C047F02E922A2D14922998B4A795C34C19813AD140C3EB070B046B93FBAC7EAF8B6251BE4991AD84FFF17B3C3C8398041FE7F8A8E80055715B48790AF59ECA489D9FB0309DCCD98D34C6E7DF7606D0A57DDE059E3346AF1CF2B01EA23F1FC3D27FFBE583F',
            'anon': '53E92D0D7C9E569CE3EA61ECBF40D9B6AC67A459829047705130BC5FC5EC526D2A4C14B4937E458D414D11754F2D0E9C3AA748D923B0F5EA746BF4425A4A231C2114430D2AF00E05B91C009C7476344765498BCD7666144BF259FDF62F9304929050F2B999AA49F72BB382FEAD53371BB98C0DFDC5CD5979E0E98AED81EFC4F09F6C11C004F5D08C2C1DD165553DBF388028A3697BB11A3A322BADC1798BDDC6188C517BEAFD7FFF17FC53753492D6EE3A455DB30F607F912B377D7D04A3B782289833AC8622DA2DFFB321C20FDA6D5FB498CA58B32B0286AFCDC03188F3830E12F971C823476637F7D6FCC263F951C116072170C0B04CBE2A5180F886008C5CF72D5680A31D2DD73EEDBE661EE34D02148467BCDFA0D0DE7F51AB3D2DEB333EFB1305878D3590217708A26AB8FEDB781A7DE2FEA11AF575DC62F2B31ECB50AA4EABCE0D6535FA1F749B0981',
            'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjE3NTQzMTQsImV4cCI6MTY2MjAxMzUxNCwiaWF0IjoxNjYxNzU0MzE0LCJVc2VySWQiOiI2OTkwNzMyMi04ODM2LTRmNDUtYjQ1ZC04MzQ3NjNhZTc5MWEiLCJUaXRsZSI6IkFobWV0IFNhbGloIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlNhbGloIiwiRW1haWwiOiJzYWxpaGJleTM0MjZAZ21haWwuY29tIiwiSXNBdXRoZW50aWNhdGVkIjoiVHJ1ZSIsIkFwcEtleSI6IkFGN0YyQTM3LUNDNEItNEYxQy04N0ZELUZGMzY0MkY2N0VDQiIsIlByb3ZpZGVyIjoiR29vZ2xlIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJwIjp7InQiOltdfX0.t5CQaI9tIz0pyX8zW54yYZxBMPICIYTVva4TJjwrw-k',
            'eJwt': 'ttT1DojhgOUTOBUmIS%2BAJrQegpHCWh25Zea3HeCiHlY4v5POtvZIJo2VHixqnc1rbywpEl6EYndbB1dqzY9fkVpbjD%2BA7N7a0D2hSOw1AGPzCC1ROxCs4CXL%2F1MWT8xqgeO2%2FQvE3k0CeVqDyzuICk54eXXcZ0lzIkhoh24OC83jJrW2bxhg2547kLSNDKVltB%2BXTRQsJIPjZvtvVsXnIrI6XigkYbQCIpZA4sk8kpcEc5NowDf3tcYd0IP3m994YCxaxgItrRgZzP24bvjtEt%2Ft9ESdr9EFHhVng%2BjcSSGCt2BqJO8rupfFh6qWvjBXPlqElL%2BqeOlPAUTxsC8iPvDF%2FClBNCLjTgtuiRgVBuUfo5O%2BXTwkiQ8HcIehmxEjnqRGHChIMD7P7h60lnxGdyxZ7xKtjMEw6WOweycs8lkmSUYELXKrCfqQTtB3Q%2FmCAXGplxEygciGebnVFpJUx7fRdJ1zXzeqHLGHj9zpOlNAoVAUQ7KJaHd0gffPcDJ5WCGQoPysGXg5s%2BuhRWSkTZRw1GWj6QQAPHW%2FydlkEY2eki63HqOJU7Q76V5A6it14LD71vKhQrjY8McIm3l6LX1Tz09jJ8ZWcGwMIQSv4k4WCRg8cSyk6OoZS4xajkRbJ9pi76pOQshFnlI2ZeaBLjx8fSOGohUl6P0O3ddoOmdgTnsAtj3FZskbj0yRuzfg',
            'cookieconsentauth': 'true',
            'loginType': 'SignIn',
            '_hjFirstSeen': '1',
            '_hjSession_216130': 'eyJpZCI6ImZhMDNmNWQ1LWExOGQtNDQ4Zi05YTZkLTM5YWFlNTJlMzQ1ZiIsImNyZWF0ZWQiOjE2NjE3NTQzMTQxMjMsImluU2FtcGxlIjpmYWxzZX0=',
            '_hjAbsoluteSessionInProgress': '1',
            'wt3_sid': '%3B289941511384204',
            'wt_fa': 'lv~1661754314676|1692858314676#cv~1|1692858314676#fv~2022-08|1692858314676#',
            '__gads': 'ID=e952604ffa340e7d-226e406c0ace00f6:T=1661754318:S=ALNI_Ma5Fi2e-TTZvkQQ-_VtCaSvcWv6gg',
            '__gpi': 'UID=00000b05f8b6cac1:T=1661754318:RT=1661754318:S=ALNI_MYAW3BlhoNXe3RYVbJaEVapOTkYUg',
            '_hjSessionUser_216130': 'eyJpZCI6IjBiYWRhZGY2LTI1NzEtNTkwMi05OTM3LTU3YTFhN2RjNTcyMCIsImNyZWF0ZWQiOjE2NjE3NTQzMTQwOTAsImV4aXN0aW5nIjp0cnVlfQ==',
            '_hjIncludedInSessionSample': '0',
            '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IlVzZXIgSWQiOiI2OTkwNzMyMi04ODM2LTRmNDUtYjQ1ZC04MzQ3NjNhZTc5MWEifSwidXNlcklkIjoiMjE2MTMwIn0=',
            'RT': '"z=1&dm=hepsiburada.com&si=54ownsrru2m&ss=l7edlsdz&sl=0&tt=0"',
            'wt3_eid': '%3B289941511384204%7C2166175431400658303%232166175434100866176',
            'wt_fa_s': 'start~1|1693290341798#',
            'hbus_sessionId': 'cd4e862b-b389-4f03-bbd0-69ac7a165293%7C1661756142004',
            '_abck': '7BB3B536AB1DB41C32A3BFE39C411C97~-1~YAAQTd86F29z5smCAQAAUw9H6AgUZVcxtuitg10FHXBoiHS/rQbysbtqi4VfuMVY7uZemJozQAwrAl/mJL9b8zGYLFq3o2hM6HFGf0tphVqWRYlLcLnKoRghvzu1JNbna4/rsWsn3ht+07ncz+IE9d6zMPqy4/jkDfy6ReZoj56u4IxTHj5aKdFa42Ar5F8ez8jII0ql9ziWX9BV2YeLaWGYlJdCTJ+xoqtaVQXSqDMSJKBFSTL7I9temok52nzWs+yxfmDEpwbYhUzK8jwg+gGONCPasIZBFH3n2N8/movDh+QcmbiBlo3grnGXHxS6hkopEgKxSLZYhHOW7NuqML06gXI+OQeQ2dnFfzyClzBiKCyi2Tea0btcjvjheDSFxzVmX9eR3Por4l4EPz8Z~-1~-1~-1',
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

    def addbasket(self):  # Json da kayıtlı olan sku ve listingId leri API yoluyla sepete ekleme

        adds = open("data/step_8_oyuncak_basket_Hepsiburada.json", encoding="utf-8").read()
        # adds = open("data/step_8_pratikev_basket_Hepsiburada.json", encoding="utf-8").read()

        # adds = open("data/step_5_Hepsiburada.json", encoding="utf-8").read()
        add = json.loads(adds)
        try:
            for d in add:
                sku = d["merchantId"]
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
        self.browser.find_element(By.ID, 'identifierId').send_keys("salihbey3426@gmail.com" + Keys.ENTER)
        time.sleep(2)
        try:
            self.browser.find_element(By.XPATH, "//input[@type='password']").send_keys("ahmetsalih1234" + Keys.ENTER)
        except:
            pass

    def order_status(self):
        time.sleep(8)
        # basket = "https://checkout.hepsiburada.com/sepetim"
        # self.browser.get(f"{basket}")
        self.browser.find_element(By.ID, 'continue_step_btn').click()
        time.sleep(6)
        self.browser.find_element(By.ID, 'continue_step_btn').click()
        time.sleep(6)
        self.browser.find_element(By.XPATH, '//*[@id="payment-methods"]/div/div[2]/div[1]/div[1]/div').click()
        self.browser.find_element(By.XPATH, '//*[@id="payment-money-transfer"]/div/div[1]/div[1]/div[2]/div').click()
        self.browser.find_element(By.ID, 'continue_step_btn').click()

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

        # TODO MATCHLEME KISMI YAPILACAK------<<<<<<<<
        # Eklenen 10 ürünün satıcılarının name bilgisine göre matchleme

        js = json.loads(response2.text)["result"]

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

        with open("data/matching_sellers.json", "w", encoding="utf-8") as f:
            json.dump(merchant_items, f, ensure_ascii=False)

        # TODO Alınmış olan telefon numara listesinin,
        # Todo step_7_category_oyuncak_company_detail içerisindeki phone kısmına aktarılması gerekli


        print('hi')
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

    def close(self):
        self.browser.close()


hb = Hepsiburada()
# hb.addbasket()
hb.logIn()
hb.order_status()
hb.contracts()
hb.close()

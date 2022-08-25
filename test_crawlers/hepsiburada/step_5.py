import json
import time
import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import requests


class crawl(scrapy.Spider):
    name = "Hepsiburada"
    output = []
    headers = {
        'cookie': '_gcl_au=1.1.591549031.1660413452; _gid=GA1.2.1359170139.1660413454; hbus_anonymousId=1fc07a1a-6c79-499c-ab2a-28455d520a37; _tt_enable_cookie=1; _ttp=aaec7b4f-e629-4ebc-bbe6-c43911581ebc; cookieconsentanon=false%7C13.08.2022%2020%3A57%3A40; cto_bundle=di2ecl9kSGo5UUtjWVZYOHlLbk1wUlNtanRKdlRUQTZYUnA3WUZ6MmdkYmNsb25QRzJobGhYSU95cE0zYTA4ZXpvSlRwdERPOTRoblQlMkJCTll1V2kwVm83bU5xU0V6UmNaOUgxTkp3YlU1WFhXc3FMODJhODkzZ0RsbCUyQk5jVmJuYzY3dVdmaWIyRkJMekFFOWthYVRYVnBGcE1BJTNEJTNE; _hjSessionUser_216130=eyJpZCI6IjJmZTBhMDc5LWQ1MGMtNTc1Yi1iZmY0LWVlMmQ2Yjk0MmJhNyIsImNyZWF0ZWQiOjE2NjA0MTM0NjA2NDMsImV4aXN0aW5nIjp0cnVlfQ==; dgr_searchresults=4175746f46696c7465724e657756616c69646174696f6e56347c64656661756c747c5573654e6577546f6c6b69656e50726564696374696f6e733d64697361626c65; isGlobalIp=1; _abck=BCEFE56ACBAB66E9FB8D719449E08536~0~YAAQjdlraDqco1yCAQAAj32Fmwjsqy6huSST2lfyIP98gZZ4rvQrxpNuporZjdoRRozrDATSDbTMNEVpcvzUL0X4zQkl0p1ldicSHJQY4S/woZF7a9NGFBXWYXT95gSr8GkxhMJvdlxE35UnkVUXMOIcysskW2xUyCWsScYpiWELRbpZc7BJy7xS2ySYCP53WD2CB6j2ZIYm8s2gYwS95jCVtTfy2gQ2OcND9pnQhB82Syq4QNkOqQgirSvHsS/CQNW+JmIiYOnPI32gCe3BlSn3hMS/jOoTBYmEkqlJfomdfQaBxC3p0JOffJgoj2ZN1UcZSVNBIBNQ5Zy7pfXSfdJmjJymXcbKCy0jwjPQg99y4qdYyy7fU9uU+GIz540noa2sK1keT3o5xmzQBdeRNQncGQc1PWSu7g9b/bE=~-1~-1~-1; bm_sz=E9BE16E347AC1CD9711ADA04F047628E~YAAQjdlraDuco1yCAQAAj32FmxCDqAk9JGsO8QCr9d9O14fb6JZpXPdTMOAdwW04wIiVKth+3Fz6Wt4d6zEOa2xRxmrGvWjSuKrcWVWbq2eP8qpycpjRy/TmSY4WAbor2O9HmoK85i4u7wsFlSpHh3rRIz30MdY7GIApXqI+rwgOOOAbEa6A5cmI+W/IC2FLr2flzVKUwzMovGB2wPPDLfhQa8aJafRv/5g3+YLtIZVaMOCek3sMm4omjaax81H++mNt5ZGtkPYb/Jbwf5MwiX4R+SVthOLTzTw6zROaEy/cmcjrbzTAxw==~3618373~3159602; wt3_eid=%3B289941511384204%7C2166041346800004667%232166046659000719809; wt3_sid=%3B289941511384204; _ga=GA1.2.1374688111.1660413454; _dc_gtm_UA-834379-1=1; ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%228323f778-5247-2489-00af-05a32f6354fb%22%2C%22e%22%3A1660468391986%2C%22c%22%3A1660466591986%2C%22l%22%3A1660466591986%7D; ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%22109b04d0-6f15-4090-5850-b64f3d886e15%22%2C%22c%22%3A1660413456413%2C%22l%22%3A1660466591988%7D; ab.storage.userId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%221fc07a1a-6c79-499c-ab2a-28455d520a37%22%2C%22c%22%3A1660413470228%2C%22l%22%3A1660466591988%7D; _hjIncludedInSessionSample=0; _hjSession_216130=eyJpZCI6ImUyNzM4NTM1LTYwMWItNDUzYy1iZGVlLTcxM2ZhZTVlOTM5ZSIsImNyZWF0ZWQiOjE2NjA0NjY2MDczMjUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _ga_44CSPTX731=GS1.1.1660466590.2.1.1660466611.39; hbus_sessionId=0ffde65d-87a8-4dea-985e-ebd9b2ff1cec%7C1660468428355',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    api_basket_headers = {
        'authority': 'checkout.hepsiburada.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjA3Mjg2NTcsImV4cCI6MTY2MDk4Nzg1NywiaWF0IjoxNjYwNzI4NjU3LCJVc2VySWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QiLCJUaXRsZSI6IkFobWV0IFRvcGFuIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlRvcGFuIiwiRW1haWwiOiJ3dGNuOTk4QGdtYWlsLmNvbSIsIklzQXV0aGVudGljYXRlZCI6IlRydWUiLCJBcHBLZXkiOiJBRjdGMkEzNy1DQzRCLTRGMUMtODdGRC1GRjM2NDJGNjdFQ0IiLCJQcm92aWRlciI6IkhlcHNpYnVyYWRhIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJHZW5kZXIiOiIxIiwicCI6eyJ0IjpbXX19.diu-1fXr2BGIbwOP6zRgYq4sckyIejn0U7x7u3hgFbQ',
        'client-id': '47b14cfb-2cad-471a-85de-ebe4684ee95f',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.hepsiburada.com',
        'referer': 'https://www.hepsiburada.com/homend-foodrunner-2002h-el-mikseri-p-HBV0000111FUT?magaza=--YAVUZLAR--',
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
    sales_headers = {
        'authority': 'checkout.hepsiburada.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjA3Mjg2NTcsImV4cCI6MTY2MDk4Nzg1NywiaWF0IjoxNjYwNzI4NjU3LCJVc2VySWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QiLCJUaXRsZSI6IkFobWV0IFRvcGFuIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlRvcGFuIiwiRW1haWwiOiJ3dGNuOTk4QGdtYWlsLmNvbSIsIklzQXV0aGVudGljYXRlZCI6IlRydWUiLCJBcHBLZXkiOiJBRjdGMkEzNy1DQzRCLTRGMUMtODdGRC1GRjM2NDJGNjdFQ0IiLCJQcm92aWRlciI6IkhlcHNpYnVyYWRhIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJHZW5kZXIiOiIxIiwicCI6eyJ0IjpbXX19.diu-1fXr2BGIbwOP6zRgYq4sckyIejn0U7x7u3hgFbQ',
        'client-id': '47b14cfb-2cad-471a-85de-ebe4684ee95f',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.591549031.1660413452; _gid=GA1.2.1359170139.1660413454; hbus_anonymousId=1fc07a1a-6c79-499c-ab2a-28455d520a37; _tt_enable_cookie=1; _ttp=aaec7b4f-e629-4ebc-bbe6-c43911581ebc; _hjSessionUser_216130=eyJpZCI6IjJmZTBhMDc5LWQ1MGMtNTc1Yi1iZmY0LWVlMmQ2Yjk0MmJhNyIsImNyZWF0ZWQiOjE2NjA0MTM0NjA2NDMsImV4aXN0aW5nIjp0cnVlfQ==; cookieconsentanon=true%7C15.08.2022%2009%3A28%3A18; cookieconsentauth=true; useinternal=true; SFSESSIONID=0687182d-c35e-44c0-9f9d-b4bf96dfa75e; anon=5845308228C1AEF9A5479ECC321482558FD7C0FBBC3A36F279BA7FB237A570E542085422041E36A974B2128451B91A9917BB0CAF828D660C69163F4DC33E1F39BFF8FE8447AD335BD6C17F5AF7BE4E06B03E12CD2F189782155AE09A579C750F8AF62FE233C090DCE7C9DF7A1D6003DC85BF47EE987877F2AFB32D2C2FB331BBC97A47824D1A5A80DBE43A3244F5CB7F72C14BCCD435FD47A552CAB3E22D67BADC39DE6AB2B6538FCB5FBA8F4D5B7814909AF7CFC840F79341FF4108DF68060917FEDA51F0218CD1E5A9EE76412EBB3DCF1382D9D779C07EFC5589AC3A61F0FB9A590390D94C6474D8FCB95D94AF8DAF5A0263C0315DD880CAEA54D0C522D09624F6279DEA3A3DA73356AFFE0E13F680BB7E5843B1C076B306D53146FFB4566B8C89EC55D035E9A9A43379E76A2DE8B33705AC4A14B7AFEB29F0F70D29CC3037FE08B08797F31AE804CBD82A; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjA3Mjg2NTcsImV4cCI6MTY2MDk4Nzg1NywiaWF0IjoxNjYwNzI4NjU3LCJVc2VySWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QiLCJUaXRsZSI6IkFobWV0IFRvcGFuIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlRvcGFuIiwiRW1haWwiOiJ3dGNuOTk4QGdtYWlsLmNvbSIsIklzQXV0aGVudGljYXRlZCI6IlRydWUiLCJBcHBLZXkiOiJBRjdGMkEzNy1DQzRCLTRGMUMtODdGRC1GRjM2NDJGNjdFQ0IiLCJQcm92aWRlciI6IkhlcHNpYnVyYWRhIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJHZW5kZXIiOiIxIiwicCI6eyJ0IjpbXX19.diu-1fXr2BGIbwOP6zRgYq4sckyIejn0U7x7u3hgFbQ; eJwt=ttT1DojhgOUTOBUmIS%2BAJrQegpHCWh25Zea3HeCiHlY4v5POtvZIJo2VHixqnc1rGBqT0snFhI0k8Re3%2Fgblanw6fRuejFopiX2fMxFwwmj%2B3AViqGb9Yqo4F%2Fp4x%2FzYOWb69eGQUM0yRwRIS0Y4Z6p2RP%2FHkGXLlmo4OMVz9KeDmnH4CYIelb0TEntNLOcS2fFtieyk%2FhPQohBzPUCq7J4aEWO%2FWu38jUvwAN4k7NiC2%2BQjABMAvROTASqV3bQ1jEt91Y9gn%2BmEMs%2BrQwY7x4TdR3pab8Ako6DH9a0jMrJTRru3sYn2QNFvIWurUNxHBH4gpI%2FLghYwsLQFrBaWgJZWwfuidQwfoveybN0ZI%2B081mPbzKHn9bnrEQZNGDZqTSsAwFNB%2FsjWFL5YBy3F%2Br1jdjZDowyMGUum11ZoJL3OrNu%2B8GZV8iQf1iS3K%2FEq2QxZRnPd2hrmY4OGsbZ3TlyIVqD4htsT%2BNqvKZ2%2ByeDPMoh9YKRDkpa3ZNBnghPiZSfm1JV8ja%2F6CQS9HfND%2BAi8s7HyqUEd6CsAOl6kfZH%2FVqFbl6O11ri70RiHkjDZ9CtG3f9RXfQFIYSSwe0arm88amqTu4kb0F9rSXl0daUSnkAHVztJtjXXZigCn%2FWUgCvT%2BOkD3taTSnew0UV4vwV8BcLyZFueZvYjTXbCWnuJzYd8mr7XqXzpXBAltDAVuBnCbPYxHyeKE0wXLXpFyQ%3D%3D; isFavoritesRequiredToReload=false; __zlcmid=1BVl9pxlbghoWaj; wt3_sid=%3B289941511384204; wt_fa=lv~1660846712758|1691950712758#cv~3|1691950712758#fv~2022-08|1691825787121#vf~0|1691950712758#; searchHistory=[%22porland%20dokulu%20alt%C4%B1n%20rip%22%2C%22porland%20l20233%20f%C4%B1a%20dokulu%22]; _abck=BCEFE56ACBAB66E9FB8D719449E08536~0~YAAQVGUQAtj2OGWCAQAAJ9iytAjUshi+zBqHh86AlUxo65gz51g7P+lBxs+BquICJyDqEG1ZB3QvMyBc98UgDLLqnqDSBBRFnMNEVRDE9KP5OsyumABqW0vpxuYzp1knqnuzYZJBcxj3n4JDMV/I0QsXadToYzS62e16rpLZWtvEfy09O4P1lvbS0roHAPBGP1ieOQ4Vzhi6oM1M4lpMpkcnlmnBI08kFw/DjRqgtQ1gDwpC8pnEhEgYe3b2LqWdkk9LdOUopptjqH+RZsdTm9WUvBe61BZzIfOk1RmyMu5Js+B/4GgH6D7xwc+PZF7s53e5IYm1JL0MXMvZOJMz6MJlMok/Ny8//+PIV8qRgenBg672rFWChHCfQT4uTgVwqf++MIAEAqCZEPCIVlz6ynMj5u5uV7OsvPewNMs=~-1~-1~-1; AKA_A2=A; _hjSession_216130=eyJpZCI6IjJhMDViMGI2LTM5MGEtNDhhYy1hNjBiLTU2NTQwOWZkMDY0YyIsImNyZWF0ZWQiOjE2NjA5MDA0MzY4ODAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga=GA1.2.1374688111.1660413454; ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%22dbbe83a7-1e8d-47ef-0976-b798ec0b07f7%22%2C%22e%22%3A1660902258840%2C%22c%22%3A1660900458841%2C%22l%22%3A1660900458841%7D; ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%22109b04d0-6f15-4090-5850-b64f3d886e15%22%2C%22c%22%3A1660413456413%2C%22l%22%3A1660900458842%7D; ab.storage.userId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%2276d54b71-a85e-4930-a40a-414facf07c3d%22%2C%22c%22%3A1660728660914%2C%22l%22%3A1660900458842%7D; cto_bundle=Kr6nuV9kSGo5UUtjWVZYOHlLbk1wUlNtanRGaDFmZ2ZURXVReXh6YzJTcXhrdGJNeFRaS2VKczBaVzdmWVhCeW54YWZlJTJCMXJxV2pBS1dWRzVkMW8zdDB1Z1hlOG8yRkdTbEdjVkFZRkdmS0NCbkRYYVZKa1ZsdjdRWU9HR0tmZ3hDT2Z5d2d2aFRPQ29DNWFpb3hKU3F5SjYwQSUzRCUzRA; _dgr_top_parent_category=; _ga_44CSPTX731=GS1.1.1660900436.46.1.1660901831.60.0.0; bm_sz=9DB48D64E123F42E6EE7145D18554ACB~YAAQjdlraAHrW7SCAQAAA2WLtRCGGZ4L62wCgCQk00B2na9tT6LdUIhQtJ06t/kGYwTY5Ky/1uwuO/ISz5L02Ac26+cmu2FJa+zyFAA0A7mRSynJkDeCBwqBvN/ifJG+h4V6a36K/YW+9+j+AkgrVZ6LosB5MyH7J7EcuuJwbmkikcGROzgusoFAexYz6lYfDNyNtqgTuV3qzqoa3Ay6Rl7H0TXMpRASH0f6hjb52DC7mdm5sLk0UT35T4cLZidfNv1hgVdJufvIFh31sykTugWL1Gn13MWPz7zwfvB2fPaVA5DbxeLEvlqiQs6M+f1kFCjhTA8I5phowyu6M5KVlA==~3682627~4536120; _hjIncludedInSessionSample=0; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7IlVzZXIgSWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QifSwidXNlcklkIjoiMjE2MTMwIn0=; RT="z=1&dm=hepsiburada.com&si=nhkgjz6nv0f&ss=l6xetcfo&sl=0&tt=0"; hbus_sessionId=06d4103d-9ef9-4ed6-b22f-695a734aee63%7C1660905055778; wt3_eid=%3B289941511384204%7C2166041346800004667%232166090325500157216; wt_fa_s=start~1|1692439255793#',
        'referer': 'https://checkout.hepsiburada.com/siparis-ozeti',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'tenant-id': 'cc7c5241-6017-44b2-9528-93c8d8907efb',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'withcredentials': 'true',
    }
    url = "https://checkout.hepsiburada.com/siparis-ozeti"
    today = datetime.now().strftime("%Y-%m-%d")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    custom_settings = {
        "DOWNLOAD_DELAY": 0.1,
        "CONCURRENT_REQUESTS": 100,
        "RETRY_ENABLED": True,
        "RETRY_TIMES": 3
    }
    cookies = {
        '_gcl_au': '1.1.591549031.1660413452',
        '_gid': 'GA1.2.1359170139.1660413454',
        'hbus_anonymousId': '1fc07a1a-6c79-499c-ab2a-28455d520a37',
        '_tt_enable_cookie': '1',
        '_ttp': 'aaec7b4f-e629-4ebc-bbe6-c43911581ebc',
        '_hjSessionUser_216130': 'eyJpZCI6IjJmZTBhMDc5LWQ1MGMtNTc1Yi1iZmY0LWVlMmQ2Yjk0MmJhNyIsImNyZWF0ZWQiOjE2NjA0MTM0NjA2NDMsImV4aXN0aW5nIjp0cnVlfQ==',
        'cookieconsentanon': 'true%7C15.08.2022%2009%3A28%3A18',
        'cookieconsentauth': 'true',
        'useinternal': 'true',
        'SFSESSIONID': '0687182d-c35e-44c0-9f9d-b4bf96dfa75e',
        'anon': '5845308228C1AEF9A5479ECC321482558FD7C0FBBC3A36F279BA7FB237A570E542085422041E36A974B2128451B91A9917BB0CAF828D660C69163F4DC33E1F39BFF8FE8447AD335BD6C17F5AF7BE4E06B03E12CD2F189782155AE09A579C750F8AF62FE233C090DCE7C9DF7A1D6003DC85BF47EE987877F2AFB32D2C2FB331BBC97A47824D1A5A80DBE43A3244F5CB7F72C14BCCD435FD47A552CAB3E22D67BADC39DE6AB2B6538FCB5FBA8F4D5B7814909AF7CFC840F79341FF4108DF68060917FEDA51F0218CD1E5A9EE76412EBB3DCF1382D9D779C07EFC5589AC3A61F0FB9A590390D94C6474D8FCB95D94AF8DAF5A0263C0315DD880CAEA54D0C522D09624F6279DEA3A3DA73356AFFE0E13F680BB7E5843B1C076B306D53146FFB4566B8C89EC55D035E9A9A43379E76A2DE8B33705AC4A14B7AFEB29F0F70D29CC3037FE08B08797F31AE804CBD82A',
        'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjA3Mjg2NTcsImV4cCI6MTY2MDk4Nzg1NywiaWF0IjoxNjYwNzI4NjU3LCJVc2VySWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QiLCJUaXRsZSI6IkFobWV0IFRvcGFuIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlRvcGFuIiwiRW1haWwiOiJ3dGNuOTk4QGdtYWlsLmNvbSIsIklzQXV0aGVudGljYXRlZCI6IlRydWUiLCJBcHBLZXkiOiJBRjdGMkEzNy1DQzRCLTRGMUMtODdGRC1GRjM2NDJGNjdFQ0IiLCJQcm92aWRlciI6IkhlcHNpYnVyYWRhIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJHZW5kZXIiOiIxIiwicCI6eyJ0IjpbXX19.diu-1fXr2BGIbwOP6zRgYq4sckyIejn0U7x7u3hgFbQ',
        'eJwt': 'ttT1DojhgOUTOBUmIS%2BAJrQegpHCWh25Zea3HeCiHlY4v5POtvZIJo2VHixqnc1rGBqT0snFhI0k8Re3%2Fgblanw6fRuejFopiX2fMxFwwmj%2B3AViqGb9Yqo4F%2Fp4x%2FzYOWb69eGQUM0yRwRIS0Y4Z6p2RP%2FHkGXLlmo4OMVz9KeDmnH4CYIelb0TEntNLOcS2fFtieyk%2FhPQohBzPUCq7J4aEWO%2FWu38jUvwAN4k7NiC2%2BQjABMAvROTASqV3bQ1jEt91Y9gn%2BmEMs%2BrQwY7x4TdR3pab8Ako6DH9a0jMrJTRru3sYn2QNFvIWurUNxHBH4gpI%2FLghYwsLQFrBaWgJZWwfuidQwfoveybN0ZI%2B081mPbzKHn9bnrEQZNGDZqTSsAwFNB%2FsjWFL5YBy3F%2Br1jdjZDowyMGUum11ZoJL3OrNu%2B8GZV8iQf1iS3K%2FEq2QxZRnPd2hrmY4OGsbZ3TlyIVqD4htsT%2BNqvKZ2%2ByeDPMoh9YKRDkpa3ZNBnghPiZSfm1JV8ja%2F6CQS9HfND%2BAi8s7HyqUEd6CsAOl6kfZH%2FVqFbl6O11ri70RiHkjDZ9CtG3f9RXfQFIYSSwe0arm88amqTu4kb0F9rSXl0daUSnkAHVztJtjXXZigCn%2FWUgCvT%2BOkD3taTSnew0UV4vwV8BcLyZFueZvYjTXbCWnuJzYd8mr7XqXzpXBAltDAVuBnCbPYxHyeKE0wXLXpFyQ%3D%3D',
        'isFavoritesRequiredToReload': 'false',
        '__zlcmid': '1BVl9pxlbghoWaj',
        'wt3_sid': '%3B289941511384204',
        'wt_fa': 'lv~1660846712758|1691950712758#cv~3|1691950712758#fv~2022-08|1691825787121#vf~0|1691950712758#',
        'searchHistory': '[%22porland%20dokulu%20alt%C4%B1n%20rip%22%2C%22porland%20l20233%20f%C4%B1a%20dokulu%22]',
        '_abck': 'BCEFE56ACBAB66E9FB8D719449E08536~0~YAAQVGUQAtj2OGWCAQAAJ9iytAjUshi+zBqHh86AlUxo65gz51g7P+lBxs+BquICJyDqEG1ZB3QvMyBc98UgDLLqnqDSBBRFnMNEVRDE9KP5OsyumABqW0vpxuYzp1knqnuzYZJBcxj3n4JDMV/I0QsXadToYzS62e16rpLZWtvEfy09O4P1lvbS0roHAPBGP1ieOQ4Vzhi6oM1M4lpMpkcnlmnBI08kFw/DjRqgtQ1gDwpC8pnEhEgYe3b2LqWdkk9LdOUopptjqH+RZsdTm9WUvBe61BZzIfOk1RmyMu5Js+B/4GgH6D7xwc+PZF7s53e5IYm1JL0MXMvZOJMz6MJlMok/Ny8//+PIV8qRgenBg672rFWChHCfQT4uTgVwqf++MIAEAqCZEPCIVlz6ynMj5u5uV7OsvPewNMs=~-1~-1~-1',
        'AKA_A2': 'A',
        '_hjSession_216130': 'eyJpZCI6IjJhMDViMGI2LTM5MGEtNDhhYy1hNjBiLTU2NTQwOWZkMDY0YyIsImNyZWF0ZWQiOjE2NjA5MDA0MzY4ODAsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '_ga': 'GA1.2.1374688111.1660413454',
        'ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec': '%7B%22g%22%3A%22dbbe83a7-1e8d-47ef-0976-b798ec0b07f7%22%2C%22e%22%3A1660902258840%2C%22c%22%3A1660900458841%2C%22l%22%3A1660900458841%7D',
        'ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec': '%7B%22g%22%3A%22109b04d0-6f15-4090-5850-b64f3d886e15%22%2C%22c%22%3A1660413456413%2C%22l%22%3A1660900458842%7D',
        'ab.storage.userId.a19ee87d-6625-49ed-ad8c-f427b0067dec': '%7B%22g%22%3A%2276d54b71-a85e-4930-a40a-414facf07c3d%22%2C%22c%22%3A1660728660914%2C%22l%22%3A1660900458842%7D',
        'cto_bundle': 'Kr6nuV9kSGo5UUtjWVZYOHlLbk1wUlNtanRGaDFmZ2ZURXVReXh6YzJTcXhrdGJNeFRaS2VKczBaVzdmWVhCeW54YWZlJTJCMXJxV2pBS1dWRzVkMW8zdDB1Z1hlOG8yRkdTbEdjVkFZRkdmS0NCbkRYYVZKa1ZsdjdRWU9HR0tmZ3hDT2Z5d2d2aFRPQ29DNWFpb3hKU3F5SjYwQSUzRCUzRA',
        '_dgr_top_parent_category': '',
        '_ga_44CSPTX731': 'GS1.1.1660900436.46.1.1660901831.60.0.0',
        'bm_sz': '9DB48D64E123F42E6EE7145D18554ACB~YAAQjdlraAHrW7SCAQAAA2WLtRCGGZ4L62wCgCQk00B2na9tT6LdUIhQtJ06t/kGYwTY5Ky/1uwuO/ISz5L02Ac26+cmu2FJa+zyFAA0A7mRSynJkDeCBwqBvN/ifJG+h4V6a36K/YW+9+j+AkgrVZ6LosB5MyH7J7EcuuJwbmkikcGROzgusoFAexYz6lYfDNyNtqgTuV3qzqoa3Ay6Rl7H0TXMpRASH0f6hjb52DC7mdm5sLk0UT35T4cLZidfNv1hgVdJufvIFh31sykTugWL1Gn13MWPz7zwfvB2fPaVA5DbxeLEvlqiQs6M+f1kFCjhTA8I5phowyu6M5KVlA==~3682627~4536120',
        '_hjIncludedInSessionSample': '0',
        '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IlVzZXIgSWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QifSwidXNlcklkIjoiMjE2MTMwIn0=',
        'RT': '"z=1&dm=hepsiburada.com&si=nhkgjz6nv0f&ss=l6xetcfo&sl=0&tt=0"',
        'hbus_sessionId': '06d4103d-9ef9-4ed6-b22f-695a734aee63%7C1660905055778',
        'wt3_eid': '%3B289941511384204%7C2166041346800004667%232166090325500157216',
        'wt_fa_s': 'start~1|1692439255793#',
    }
    # HB Token Bilgisi
    token = {
        "xsrfToken": "CfDJ8B9VfNNTUIRMsi4tN37G2veH_hQ4RLsoiDY4ObXK3CNDRvP7OFTreZcODGYkJThTIbB8oMZh6vJ0rTfRgpcmjGnqb0ncMKJo9KDHxx19rkbL0a-TchuGT-QCWRAddWRtSNZA9JcccusGN4S9eMeauZQ"}
    token2 = {
        "xsrfToken": "CfDJ8B9VfNNTUIRMsi4tN37G2vffoHJsg9ueNIj9qaye2gzHqlTDb7K3aooORO8tkqx6R18yNUGBOmXzpxCkVn69r1AaiD7a7x432idg9kVgPUUdeQ23r_t3c3Kg3RjDn8SuvX4JdHo5RxQ24MxdmLSaGu8"}
    headerss = {
        'authority': 'checkout.hepsiburada.com',
        'accept': '*/*',
        'accept-language': 'tr,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjA3Mjg2NTcsImV4cCI6MTY2MDk4Nzg1NywiaWF0IjoxNjYwNzI4NjU3LCJVc2VySWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QiLCJUaXRsZSI6IkFobWV0IFRvcGFuIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlRvcGFuIiwiRW1haWwiOiJ3dGNuOTk4QGdtYWlsLmNvbSIsIklzQXV0aGVudGljYXRlZCI6IlRydWUiLCJBcHBLZXkiOiJBRjdGMkEzNy1DQzRCLTRGMUMtODdGRC1GRjM2NDJGNjdFQ0IiLCJQcm92aWRlciI6IkhlcHNpYnVyYWRhIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJHZW5kZXIiOiIxIiwicCI6eyJ0IjpbXX19.diu-1fXr2BGIbwOP6zRgYq4sckyIejn0U7x7u3hgFbQ',
        'client-id': '47b14cfb-2cad-471a-85de-ebe4684ee95f',
        'content-type': 'application/json; charset=utf-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.591549031.1660413452; _gid=GA1.2.1359170139.1660413454; hbus_anonymousId=1fc07a1a-6c79-499c-ab2a-28455d520a37; _tt_enable_cookie=1; _ttp=aaec7b4f-e629-4ebc-bbe6-c43911581ebc; _hjSessionUser_216130=eyJpZCI6IjJmZTBhMDc5LWQ1MGMtNTc1Yi1iZmY0LWVlMmQ2Yjk0MmJhNyIsImNyZWF0ZWQiOjE2NjA0MTM0NjA2NDMsImV4aXN0aW5nIjp0cnVlfQ==; cookieconsentanon=true%7C15.08.2022%2009%3A28%3A18; cookieconsentauth=true; useinternal=true; SFSESSIONID=0687182d-c35e-44c0-9f9d-b4bf96dfa75e; anon=5845308228C1AEF9A5479ECC321482558FD7C0FBBC3A36F279BA7FB237A570E542085422041E36A974B2128451B91A9917BB0CAF828D660C69163F4DC33E1F39BFF8FE8447AD335BD6C17F5AF7BE4E06B03E12CD2F189782155AE09A579C750F8AF62FE233C090DCE7C9DF7A1D6003DC85BF47EE987877F2AFB32D2C2FB331BBC97A47824D1A5A80DBE43A3244F5CB7F72C14BCCD435FD47A552CAB3E22D67BADC39DE6AB2B6538FCB5FBA8F4D5B7814909AF7CFC840F79341FF4108DF68060917FEDA51F0218CD1E5A9EE76412EBB3DCF1382D9D779C07EFC5589AC3A61F0FB9A590390D94C6474D8FCB95D94AF8DAF5A0263C0315DD880CAEA54D0C522D09624F6279DEA3A3DA73356AFFE0E13F680BB7E5843B1C076B306D53146FFB4566B8C89EC55D035E9A9A43379E76A2DE8B33705AC4A14B7AFEB29F0F70D29CC3037FE08B08797F31AE804CBD82A; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjA3Mjg2NTcsImV4cCI6MTY2MDk4Nzg1NywiaWF0IjoxNjYwNzI4NjU3LCJVc2VySWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QiLCJUaXRsZSI6IkFobWV0IFRvcGFuIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlRvcGFuIiwiRW1haWwiOiJ3dGNuOTk4QGdtYWlsLmNvbSIsIklzQXV0aGVudGljYXRlZCI6IlRydWUiLCJBcHBLZXkiOiJBRjdGMkEzNy1DQzRCLTRGMUMtODdGRC1GRjM2NDJGNjdFQ0IiLCJQcm92aWRlciI6IkhlcHNpYnVyYWRhIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJHZW5kZXIiOiIxIiwicCI6eyJ0IjpbXX19.diu-1fXr2BGIbwOP6zRgYq4sckyIejn0U7x7u3hgFbQ; eJwt=ttT1DojhgOUTOBUmIS%2BAJrQegpHCWh25Zea3HeCiHlY4v5POtvZIJo2VHixqnc1rGBqT0snFhI0k8Re3%2Fgblanw6fRuejFopiX2fMxFwwmj%2B3AViqGb9Yqo4F%2Fp4x%2FzYOWb69eGQUM0yRwRIS0Y4Z6p2RP%2FHkGXLlmo4OMVz9KeDmnH4CYIelb0TEntNLOcS2fFtieyk%2FhPQohBzPUCq7J4aEWO%2FWu38jUvwAN4k7NiC2%2BQjABMAvROTASqV3bQ1jEt91Y9gn%2BmEMs%2BrQwY7x4TdR3pab8Ako6DH9a0jMrJTRru3sYn2QNFvIWurUNxHBH4gpI%2FLghYwsLQFrBaWgJZWwfuidQwfoveybN0ZI%2B081mPbzKHn9bnrEQZNGDZqTSsAwFNB%2FsjWFL5YBy3F%2Br1jdjZDowyMGUum11ZoJL3OrNu%2B8GZV8iQf1iS3K%2FEq2QxZRnPd2hrmY4OGsbZ3TlyIVqD4htsT%2BNqvKZ2%2ByeDPMoh9YKRDkpa3ZNBnghPiZSfm1JV8ja%2F6CQS9HfND%2BAi8s7HyqUEd6CsAOl6kfZH%2FVqFbl6O11ri70RiHkjDZ9CtG3f9RXfQFIYSSwe0arm88amqTu4kb0F9rSXl0daUSnkAHVztJtjXXZigCn%2FWUgCvT%2BOkD3taTSnew0UV4vwV8BcLyZFueZvYjTXbCWnuJzYd8mr7XqXzpXBAltDAVuBnCbPYxHyeKE0wXLXpFyQ%3D%3D; isFavoritesRequiredToReload=false; __zlcmid=1BVl9pxlbghoWaj; wt3_sid=%3B289941511384204; wt_fa=lv~1660846712758|1691950712758#cv~3|1691950712758#fv~2022-08|1691825787121#vf~0|1691950712758#; searchHistory=[%22porland%20dokulu%20alt%C4%B1n%20rip%22%2C%22porland%20l20233%20f%C4%B1a%20dokulu%22]; _hjSession_216130=eyJpZCI6IjJhMDViMGI2LTM5MGEtNDhhYy1hNjBiLTU2NTQwOWZkMDY0YyIsImNyZWF0ZWQiOjE2NjA5MDA0MzY4ODAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; bm_sz=9DB48D64E123F42E6EE7145D18554ACB~YAAQjdlraAHrW7SCAQAAA2WLtRCGGZ4L62wCgCQk00B2na9tT6LdUIhQtJ06t/kGYwTY5Ky/1uwuO/ISz5L02Ac26+cmu2FJa+zyFAA0A7mRSynJkDeCBwqBvN/ifJG+h4V6a36K/YW+9+j+AkgrVZ6LosB5MyH7J7EcuuJwbmkikcGROzgusoFAexYz6lYfDNyNtqgTuV3qzqoa3Ay6Rl7H0TXMpRASH0f6hjb52DC7mdm5sLk0UT35T4cLZidfNv1hgVdJufvIFh31sykTugWL1Gn13MWPz7zwfvB2fPaVA5DbxeLEvlqiQs6M+f1kFCjhTA8I5phowyu6M5KVlA==~3682627~4536120; ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%22109b04d0-6f15-4090-5850-b64f3d886e15%22%2C%22c%22%3A1660413456413%2C%22l%22%3A1660910999172%7D; ab.storage.userId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%2276d54b71-a85e-4930-a40a-414facf07c3d%22%2C%22c%22%3A1660728660914%2C%22l%22%3A1660910999172%7D; _ga=GA1.2.1374688111.1660413454; ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%229249e807-e20f-f3d3-4f6b-c27e450c47d0%22%2C%22e%22%3A1660912865542%2C%22c%22%3A1660910999171%2C%22l%22%3A1660911065542%7D; cto_bundle=wSk3wl9kSGo5UUtjWVZYOHlLbk1wUlNtanRMMkpzZG54TGxqbGRxVkpaTEZDZFFaTmJXckMwM2k0MWNuc2JsdiUyQm1za21xdkV6SWh4aHUlMkZEY1pmZmpIQkxJVSUyQmpDbVQ5QVZaWHFLR3U3MVR3cSUyQjRxbEliWWdpZFVKRTVad0dBaXhRTElaamE1dG5LcFljRk4xUENWZ2ZQRFZWZyUzRCUzRA; _ga_44CSPTX731=GS1.1.1660909649.48.1.1660911066.57.0.0; _dgr_top_parent_category=; RT="z=1&dm=hepsiburada.com&si=xjyj4fhoh5&ss=l6xetcfo&sl=0&tt=0"; _hjIncludedInSessionSample=0; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7IlVzZXIgSWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QifSwidXNlcklkIjoiMjE2MTMwIn0=; wt3_eid=%3B289941511384204%7C2166041346800004667%232166091323200566072; wt_fa_s=start~1|1692449232480#; _abck=BCEFE56ACBAB66E9FB8D719449E08536~0~YAAQVj0WAs5ifbSCAQAAndMktgjJsG7WzHzK+iB89V0atAvHtEHzQpbghRjDooKE3kEXX3Gnqklz/+Pq998AGsMLU+eUTmn4L2qsDJsgmewcCqtAOP3IIQUpgMXkIebaeYtfCCdpRLmapIqok3TfFWpfltR9xDAPBd+R6d6+IqItZvUXlduUBHbjMhQHKPgSmKY5axh4SBWFa/zDIMrWBWGx3JJ0dE+3eM+AbJH13TV50+DYYbs+cq7ipdqDRoicMMCeMAHIlNVPGxPWEgsMqvLrZ/LDNGWxlzkcJpNg04+2e3OA2qmqx1q38IoVp6SWx6doim3SGQ9HB/ZCRFCojit8S3Q1zDRUN1LXXqRtRWA/D/yceiYkPFL5JNmYeBZseQny~-1~-1~-1; hbus_sessionId=b46bca75-d2bc-41b3-86cf-cbe7a1ca0cd6%7C1660915052264',
        'origin': 'https://checkout.hepsiburada.com',
        'referer': 'https://checkout.hepsiburada.com/teslimat',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'tenant-id': 'cc7c5241-6017-44b2-9528-93c8d8907efb',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-correlation-id': '496cce94-5ea8-42d2-a885-2cb9ed4c77a6',
    }

    json_data_basket = {
        'product': {  # TODO DIŞARDAN SKU VE LİSTİNGID göndermen gerekiyor
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

    # cook = {
    #     '_gcl_au': '1.1.591549031.1660413452',
    #     'hbus_anonymousId': '1fc07a1a-6c79-499c-ab2a-28455d520a37',
    #     '_tt_enable_cookie': '1',
    #     '_ttp': 'aaec7b4f-e629-4ebc-bbe6-c43911581ebc',
    #     '_hjSessionUser_216130': 'eyJpZCI6IjJmZTBhMDc5LWQ1MGMtNTc1Yi1iZmY0LWVlMmQ2Yjk0MmJhNyIsImNyZWF0ZWQiOjE2NjA0MTM0NjA2NDMsImV4aXN0aW5nIjp0cnVlfQ==',
    #     'cookieconsentanon': 'true%7C15.08.2022%2009%3A28%3A18',
    #     'cookieconsentauth': 'true',
    #     'useinternal': 'true',
    #     'SFSESSIONID': '0687182d-c35e-44c0-9f9d-b4bf96dfa75e',
    #     '__zlcmid': '1BVl9pxlbghoWaj',
    #     'searchHistory': '[%22porland%20dokulu%20alt%C4%B1n%20rip%22%2C%22porland%20l20233%20f%C4%B1a%20dokulu%22]',
    #     'cto_bundle': 'wSk3wl9kSGo5UUtjWVZYOHlLbk1wUlNtanRMMkpzZG54TGxqbGRxVkpaTEZDZFFaTmJXckMwM2k0MWNuc2JsdiUyQm1za21xdkV6SWh4aHUlMkZEY1pmZmpIQkxJVSUyQmpDbVQ5QVZaWHFLR3U3MVR3cSUyQjRxbEliWWdpZFVKRTVad0dBaXhRTElaamE1dG5LcFljRk4xUENWZ2ZQRFZWZyUzRCUzRA',
    #     '_ga': 'GA1.1.1374688111.1660413454',
    #     'ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec': '%7B%22g%22%3A%22114e98a6-349f-2074-0f05-c255472b02f9%22%2C%22e%22%3A1661002034672%2C%22c%22%3A1661000234672%2C%22l%22%3A1661000234672%7D',
    #     'ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec': '%7B%22g%22%3A%22109b04d0-6f15-4090-5850-b64f3d886e15%22%2C%22c%22%3A1660413456413%2C%22l%22%3A1661000234673%7D',
    #     'ab.storage.userId.a19ee87d-6625-49ed-ad8c-f427b0067dec': '%7B%22g%22%3A%2276d54b71-a85e-4930-a40a-414facf07c3d%22%2C%22c%22%3A1660728660914%2C%22l%22%3A1661000234674%7D',
    #     '_ga_44CSPTX731': 'GS1.1.1661000234.51.0.1661000235.59.0.0',
    #     '_dgr_top_parent_category': '',
    #     'anon': '8BAC4D0BD11AF41D99788D2A6242D6ADA0B459E7F6C68E2EF9D6014C5EF31350CD3C73CE4669956B0C206DE8F052BBF91FB4656F5E220DF9DFD6F7944A06D93110C4C6952392224E139967F33E5714777D8A2B7892EB6294EC9C23AAE2F90997077DAD9D9C610FDFB55AF9E4206F67659B2AB7181B88E20B54FC1971A5FB2DDF6473EEAB2566F00AD8B8DB8D46A80C21AAF4225D28F1352A8B95692662BE45B56DB4742C8160B454312834A0FB78BB7F327A3BC21F623EA2FCFCE516E17C3F776D9606634951CAD4EA6C1F2057A19EC516C5DDCD0B8AFD6ED11DD1F00D1DD3BFED09E6FEBB702911B61CF2F003891BB9D18C55CA6DFCC99BDC8424CA9AD9555888A8DE3E23E7DB897EF610580340924A6D864B6B1B0847C6BD211B2279AD6978158FE4ABF550C1A884D7FEB05A34EE7B96DAC7CF1FAA844975AD15C027619005026D7FE7BC67C3757F168E60',
    #     'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjEwMDA2NDgsImV4cCI6MTY2MTI1OTg0OCwiaWF0IjoxNjYxMDAwNjQ4LCJVc2VySWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QiLCJUaXRsZSI6IkFobWV0IFRvcGFuIiwiRmlyc3ROYW1lIjoiQWhtZXQiLCJMYXN0TmFtZSI6IlRvcGFuIiwiRW1haWwiOiJ3dGNuOTk4QGdtYWlsLmNvbSIsIklzQXV0aGVudGljYXRlZCI6IlRydWUiLCJBcHBLZXkiOiJBRjdGMkEzNy1DQzRCLTRGMUMtODdGRC1GRjM2NDJGNjdFQ0IiLCJQcm92aWRlciI6IkhlcHNpYnVyYWRhIiwiU2hhcmVEYXRhUGVybWlzc2lvbiI6IlRydWUiLCJHZW5kZXIiOiIxIiwicCI6eyJ0IjpbXX19.EbsyRh0wA1t-UtJNjNen7OmQivTtg2kSNSkgwgZMG8k',
    #     'eJwt': 'ttT1DojhgOUTOBUmIS%2BAJrQegpHCWh25Zea3HeCiHlY4v5POtvZIJo2VHixqnc1ry7FwZt%2FgknSgxQF9%2Bw5%2Flfx6qVMANccZBqEwB9cOpZhCx%2B0PMb4%2BVcQy2pK4drUXB6crUTL0LdDlb6qsPl%2BD0xMLIrkFtQL6rbDxqN%2F99aOxM91VtExTogox8t6zUvakqtUdrC8NmIDl3QWo7jnEzE1s8FerdiuvozLd%2F8jiIwC3Sr9NFCfrGiLIAmJHACqCjP220%2FGRvMuKtTyTQ3PBG%2Fi%2Fob6xwKvaHeLQMZUmIHldB03Gbgnx79j36EuT5P9AtjvJqL5Vh9YxS1p4IWvZJMrALsxS0%2Ftb9z6PB1vDmdoelbop9ZPZilWSCDH%2BJ1AE3Cumnrx4iMw%2FvJABcJmsQMJiBtwJo1D7RJBxrEabAyqHisqxfVt2%2Fdadh8NE1vrHP4%2FESVmhphn5mU9Ts1U4Y2E%2BR%2Fr8Dnd%2FoyPtKAduU3ExWoQQ23Sqfav902gjx6mh5btULwP28kqAc%2B1r9Co3s8%2F55QtPDFx%2F0xfgxr47q54iOI4NES%2FNjDWK2694C%2F2B%2F9k4JsVOg9QAu5SdAu9WL2fv%2Bg5DLrHRCyBPJIGWX%2FQxpK0leeE%2FuS8mqKEwC%2FKKfRzsjokmD4%2FX5pA8N7qnT%2BUa7%2FD4om3%2BAngPvC2oUwah4CiHCOPWUQSMW2X9p41lrvG%2FHeRUzymT1Z9X4stptA%3D%3D',
    #     'wt3_sid': '%3B289941511384204',
    #     'wt_fa': 'lv~1661147689986|1692251689986#cv~10|1692251689986#fv~2022-08|1691825787121#vf~1|1692251689985#',
    #     'RT': '"z=1&dm=hepsiburada.com&si=y36kaw5otki&ss=l6xetcfo&sl=0&tt=0"',
    #     '_hjAbsoluteSessionInProgress': '0',
    #     '_abck': 'BCEFE56ACBAB66E9FB8D719449E08536~0~YAAQrtlraFSAB7WCAQAAUTAexQhynzxocjrjGqgvQM5iatLMmANj6sHfJUK30tqKfFBtpJ5t2qYzfPx1R0dqPTQNHcIkZkRdxCWNMgxesn19mZ5PpjwYU4negiMVPFGp9h5+x+ou7QO7bIcKv2t8HMnQ3zvgqDV7i6J/01XrVY0Iszq4hGy0DbQ/obcvM3MagOW//M8KCYwlkG+ioyon3f54Mk+kLo4sr+CIh8yyHJfgv7jhdNgvyihCqEQlYespg/zEEWpupq5FXnfFdY/ky1g+BF/fr+F3jQC8xDl9zDRlFdR1c4dSzoAqTIOTBiJ5BplEEv2n22HzarU/E8GcMs373SRPHv2QKwPfRZ4WMVHT7+VLtbGydVAevgdHmWvX73PnF8syzpGBMWJzBtrHSmZ/SXX+mRhQfn437Yc=~-1~-1~-1',
    #     'bm_sz': 'C42504332ED82836F4ACD60681E9BB89~YAAQrtlraFWAB7WCAQAAUTAexRBgMhMHcORseX+1nzEMfVwLlvo10u6e+cbMnd2DFPCQIFmKq62HyQkv8njCq0aYuCtxjpLUTnuVpLki4wn2Sds5zGlQ3WVxQnMx41NZAUIzV2JuHYcO3jy4EtU7gE6kJ5FfIKaagNufYgOwyGMNCkFahjG0guzstORDNITDHPWEDFtoF279xPAZxmBRQGHYOYswlHW4MYNM4ARUKElUoWkPDpuOd9JdOnqq3ccQqS8q9xsa7oaf6wR3Ie3ADkFxjok80OMUcvup+7lzcswx0GTd7Qn6Ng==~3749187~4407878',
    #     '_hjIncludedInSessionSample': '0',
    #     '_hjSession_216130': 'eyJpZCI6Ijk5MjhlM2M3LWJlZjUtNGFlZC1iNDNmLTk1MjYwNjc5OTkzNSIsImNyZWF0ZWQiOjE2NjExNjQ0Nzg5NzAsImluU2FtcGxlIjpmYWxzZX0=',
    #     '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7IlVzZXIgSWQiOiI3NmQ1NGI3MS1hODVlLTQ5MzAtYTQwYS00MTRmYWNmMDdjM2QifSwidXNlcklkIjoiMjE2MTMwIn0=',
    #     'wt3_eid': '%3B289941511384204%7C2166041346800004667%232166116447900714268',
    #     'wt_fa_s': 'start~1|1692700479239#',
    #     'hbus_sessionId': 'bd11c21f-591b-4352-aa57-852840495505%7C1661166279274',
    # }

    @staticmethod
    def prepare_urls():
        data = open("data/step_4_merchant_company_details_Hepsiburada.json", encoding="utf-8").read()
        data = json.loads(data)
        urls = []
        for row in data[:10]:
            urls.append(row['p_url'])

        urls = list(set(urls))
        return urls

    def start_requests(self):
        urls = self.prepare_urls()
        for url in urls:
            req = scrapy.Request(url, callback=self.continues,
                                 cookies=self.cookies, dont_filter=True, headers=self.headerss)
            yield req
            req.cb_kwargs["url"] = url

        # TODO Step 4 e ait json çıktısını okut ve içindeki ilk 10 ürünün linkine git ordan

    def continues(self, response, **kwargs):  # Sku ve listingId alındı
        url = kwargs["url"]

        listingId = response.xpath("//input[@name='listingid']/@value").get()
        merchantId = response.xpath("//input[@name='sku']/@value").get()

        self.output.append({
            "listingId": listingId,
            "merchantId": merchantId,
        })

        with open(f"data/step_5_Hepsiburada.json", "w", encoding="utf-8") as f:
            json.dump(self.output, f, ensure_ascii=False)

        req = scrapy.Request(url,
                             callback=self.parse, dont_filter=True, headers=self.headerss)

        yield req

    def parse(self, response, **kwargs):
        pass

    def close(self, spider, reason):
        # with open(f"data/step_5_{self.name}_{self.today}.json", "w", encoding="utf-8") as f:
        #     json.dump(self.output, f, ensure_ascii=False)
        pass

process = CrawlerProcess()
process.crawl(crawl)
process.start()

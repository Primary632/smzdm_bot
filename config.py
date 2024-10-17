"""
请求头
"""
DEFAULT_HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'zhiyou.smzdm.com',
        'Referer': 'https://www.smzdm.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        }


"""
调试用 COOKIE
"""
TEST_COOKIE = 'device_id=213070643316962025978917306646d7b9e35af001e1a364363f2188cb; homepage_sug=c; r_sort_type=score; smzdm_id=1015618475; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221015618475%22%2C%22first_id%22%3A%2218aed8d9c56c5c-0ab11d76e27fbf-26031e51-1327104-18aed8d9c571106%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fpost.smzdm.com%2Fju%2Fae6l2qn%2F%22%7D%2C%22%24device_id%22%3A%2218aed8d9c56c5c-0ab11d76e27fbf-26031e51-1327104-18aed8d9c571106%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNTQxNjAxMzAxMjIyLTBkYzY2ZDI0NzM3NjlmOC0yNjAwMWU1MS0xMzI3MTA0LTE5MTU0MTYwMTMxMTZiMCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjEwMTU2MTg0NzUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221015618475%22%7D%7D'
SMZDM_COOKIE = 'device_id=213070643316962025978917306646d7b9e35af001e1a364363f2188cb; homepage_sug=c; r_sort_type=score; __ckguid=KW52Ro7G8yGUvSXKcxqGlo6; footer_floating_layer=0; ad_date=17; ad_json_feed=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221015618475%22%2C%22first_id%22%3A%2218aed8d9c56c5c-0ab11d76e27fbf-26031e51-1327104-18aed8d9c571106%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2F%22%7D%2C%22%24device_id%22%3A%2218aed8d9c56c5c-0ab11d76e27fbf-26031e51-1327104-18aed8d9c571106%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNTQxNjAxMzAxMjIyLTBkYzY2ZDI0NzM3NjlmOC0yNjAwMWU1MS0xMzI3MTA0LTE5MTU0MTYwMTMxMTZiMCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjEwMTU2MTg0NzUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221015618475%22%7D%7D; _zdmA.uid=ZDMA.f63zld0nPo.1729156851.2419200; _zdmA.vid=*; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A2%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%5D; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1729156851; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1729156851; HMACCOUNT=AB3FA1331BD3C6E9; _zdmA.time=1729156851672.0.https%3A%2F%2Fwww.smzdm.com%2F; sess=BA-1RkUOYsbSIjZaYyEGMK9ijqmZtDYk7mHK%2BSATqLYvThQ314x2yS9rVQoZh6mKZCcLvkiSqTkP2wbIHGGsEgzGVbVK%2FkO6lFgUL3QjWC12pIBrTkl1plR3C%2BC; user=user%3A1015618475%7C1015618475; smzdm_id=1015618475'


"""
调试用 SERVERCHAN_SECRETKEY
"""
SERVERCHAN_SECRETKEY = ''

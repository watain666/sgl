API_URL = "https://rent.591.com.tw/home/search/rsList"

HEADERS = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'connection': "keep-alive",
    'dnt': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
}

CONDITIONS = {
    'is_new_list': '1',
    'type': '1',
    'kind': '1',               # 類型 整層
    'searchtype': '1',         # 照縣市
    'regionid': '1',           # 台北市
    'rentprice': '0,20000',    # 0-20000元
    'patternMore': '1,2,3',    # 1-3房
    'area': '10,40',           # 坪數
    'option': 'cold',          # 有冷氣
    'hasimg': '1',             # 有照片
    'not_cover': '1',          # 非頂加
    #'other': 'pet,cook',       # 可寵, 開伙
}

WEB_URL_FORMAT_STR = "https://rent.591.com.tw/rent-detail-{}.html"

PARSE_INTERVAL_IN_SECONDS = 900

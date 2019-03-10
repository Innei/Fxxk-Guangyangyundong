# -*- coding: utf-8 -*- 
# 第一行必须有，否则报中文字符非ascii码错误

import urllib.parse
import hashlib
import requests
import json
AK = 'bnbA5OGDjdxCtODwC8cEUIIWCSvuyirn'
url = 'http://api.map.baidu.com/directionlite/v1/walking?origin=27.925212,120.712985&destination=27.932401,120.713758&ak=' + AK
# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak

# queryStr = '/directionlite/v1/walking?origin=40.01116,116.339303&destination=39.936404,116.452562&ak=' + AK
#
# # 对queryStr进行转码，safe内的保留字符不转换
# encodedStr = urllib.parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
#
# # 在最后直接追加上yoursk
# rawStr = encodedStr + 'YMc6MiwkNGUh6TBX0qZafqjtBv1QB269'
#
# # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
# # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
# sn = hashlib.md5(urllib.parse.quote_plus(rawStr).encode('utf-8')).hexdigest()
# print(sn)

r = requests.session()
r = r.get(url)
j = json.loads(r.content)
with open('direction.json','w+',encoding='utf-8') as f:
    f.write(json.dumps(j,ensure_ascii=False,indent=2))
print((j["result"]["routes"][0]["distance"]))


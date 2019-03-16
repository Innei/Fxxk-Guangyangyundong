import requests
import json

url = "https://api.guangyangyundong.com/api/graphql/query"
page = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
}
proxies = {
    'http': 'socks5://127.0.0.1:1080'
}
while page < 2000:
    data = {
        'query': '''{
  university(id:3) {
	  kcalConsumptionRanking (pageSize:10 pageNumber:''' + str(page) + '''){
      pagesCount
      data{
      studentId
      studentName
      avatarUrl
      kcalConsumption
      }
    }
  }
}
'''
    }
    r = requests.post(url, data=data, headers=headers,proxies=proxies).content
    r = json.loads(r)

    with open('get_name.json', 'a+', encoding='utf-8') as file:
        file.write(json.dumps(r, indent=2, ensure_ascii=False))
    page += 1

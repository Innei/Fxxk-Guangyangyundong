import requests
import json

url = "https://api.guangyangyundong.com/api/graphql/query"
id = input()
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
}
data = {
    'query': '''
     {
  runningActivity(id: ''' + id + ''') {
    distance
    costTime
    endedAt
    qualifiedDistance
    qualifiedCostTime
    kcalConsumed
    qualified
    isValid
    isVerified
    runningSport {
      name
    }
    data {
      longitude
      latitude
      isNormal
      locationType
      stepCount
      distance
      acquisitionTime
    }
  }
}
'''
}
r = requests.post(url, data=data,headers=headers).content
r = json.loads(r)
print('id = ', id, r, '\n')
with open('/Volumes/mac专用/get_runningpath4.json', 'a+', encoding='utf-8') as file:
    file.write('id = ' + str(id))
    file.write(json.dumps(r, indent=2, ensure_ascii=False))

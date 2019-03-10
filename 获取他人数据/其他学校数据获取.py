import requests
import json

url = "https://api.guangyangyundong.com/api/graphql/query"

data = {
    'query': '''
     {
  areaSports(universityId: 1) {
    id
    name
    qualifiedCostTime
    acquisitionInterval
    isEnabled
    imgUrl
    participantNum
    universityId
  }
}
'''
}
r = requests.post(url, data=data).content
r = json.loads(r)
print(r, '\n')

data = {
    'query': '''
     {
  runningSports(universityId:1,isEnabled: true,isMan:true) {
    acquisitionInterval
    participantNum
    id
    name
    isEnabled
    qualifiedDistance
    qualifiedCostTime
    imgUrl
    stepThreshold
  }
}
'''
}
r = requests.post(url, data=data).content
r = json.loads(r)
print(r, '\n')

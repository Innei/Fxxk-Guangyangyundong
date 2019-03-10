import requests
import json

url = "https://api.guangyangyundong.com/api/graphql/query"
id = 100
while id < 200:
    data = {
        'query': '''
     {
  student(id: ''' + str(id) + ''') {
    accuRunningActivityCount(timeRange: CURRENT_WEEK)
    accuAreaActivityCount(timeRange: CURRENT_WEEK)
    qualifiedRunningActivityCount(timeRange: CURRENT_WEEK)
    qualifiedAreaActivityCount(timeRange: CURRENT_WEEK)
    signInCount(timeRange: CURRENT_WEEK)
    runningActivityTimeCosted(timeRange: CURRENT_WEEK)
    areaActivityTimeCosted(timeRange: CURRENT_WEEK)
    runningActivityKcalConsumption(timeRange: CURRENT_WEEK)
    areaActivityKcalConsumption(timeRange: CURRENT_WEEK)
    runningActivities(startDate: "2018-11-04", endDate: "2019-03-08") {
      data {
        id
        runningSportId
        costTime
        distance
        kcalConsumed
        qualified
        startTime
        sportDate
        endedAt
        isValid
        isVerified
        runningSport {
          name
        }
      }
    }
    areaActivities(startDate: "2019-03-04", endDate: "2019-03-08") {
      data {
        id
        areaSportId
        location {
          name
          latitude
          isEnabled
          latitude
          longitude
          radius
          addr
        }
        areaSport {
          name
        }
        costTime
        kcalConsumed
        qualified
        isValid
        isVerified
        startTime
        sportDate
        endedAt
      }
    }
  }
}
'''
    }
    r = requests.post(url, data=data).content
    r = json.loads(r)
    print('id = ' , id ,r)
    with open('/Volumes/mac专用/get_sportdata.json', 'a+', encoding='utf-8') as file:
        file.write('id = ' + str(id))
        file.write(json.dumps(r, indent=2, ensure_ascii=False))
    id = id + 1

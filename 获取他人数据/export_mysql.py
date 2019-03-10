import requests
import json
import MySQLdb
url = "https://api.guangyangyundong.com/api/graphql/query"

Loginfo = {'USER': 'root', 'PSWD': '123456', 'HOST': 'localhost', 'PORT': 3306}
# Python 连接MySQL
conn = MySQLdb.connect(host=Loginfo['HOST'], user=Loginfo['USER'], passwd=Loginfo['PSWD'], port=Loginfo['PORT'],
                       charset='utf8')
datalist = [] # python 列表

id = 47000
while id < 47001:
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
    print('id = ', id, r)
    with open('/Volumes/mac专用/get_sportdata.json', 'a+', encoding='utf-8') as file:
        file.write('id = ' + str(id))
        file.write(json.dumps(r, indent=2, ensure_ascii=False))
    id = id + 1
    datalist.append(r)
    for dict in datalist:
        print(dict)
    for dict in datalist:
        dict[u'LOCAL'] = dict[u'LOCAL'].replace('\r\n', '\\r\\n').replace("'s", "\\'s")  # 将字段中的特殊：回车换行以及's 转换，方便形成sql语句
        sql = "insert into db1.s1 (mobile,NAME,LOCAL,CreateTime,id) values('%s','%s','%s','%s','%s');" % (
        dict[u'mobile'], dict[u'NAME'], dict[u'LOCAL'], str(dict[u'CreateTime']), dict[u'id'])
        print(sql)
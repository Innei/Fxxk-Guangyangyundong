import requests
import time
import json
import random
from math import radians, cos, sin, asin, sqrt
url = 'https://api.guangyangyundong.com/'
millis = int(round(time.time() * 1000))  # 获取时间截
r = requests.session()
start_time = int(time.time())

# 全局变量
distance = 0
longitude = 120.7071
latitude = 27.917151
lon1 = 120.7071
lat1 = 27.917151
lon2 = 120.7071
lat2 = 27.917151
stepCount = 0
targetFinishedTime = 0

# start
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; MX4 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
    'Authorization': 'eyJhbGciOiJIUzUxMiIsInppcCI6IkRFRiJ9.eNqqViouTVKyUrI0NDE3UtJRSq0oULIyNDW1NDWzNLIw01Eqys9JLVayio6tBQAAAP__.DGeoPI2m56rXKxVJ5GKxW2KYzJ_GRZW8yfV3gLUNdSLQfOQhbUX1IAc4DEiQLT_VLL__moSqhR0hOuy1_0pcTT',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'startTime': millis,
    'runningSportId': 20,  # 跑步模式
    'studentId': 47580,
}

js = r.post(url + 'api/runningActivities/start',
            data=data, headers=headers).content
js = json.loads(js)
id = js["id"]  # 获取当前运动id

print(id)


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000

# running activity data post

def anti_activity():  # 回走函数
    global longitude, latitude, lat1, lon1, lat2, lon2, stepCount, distance, start_time, targetFinishedTime
    if distance >= 1000: # 1000m 结束
        return
    rand = round(random.randint(1, 100) / 100) / 4200   # 引入随机值
    lon2 = lon1 + pow(-1, round(0, 1)) * round(random.randint(1, 100) / 100) / 1000000  # 左右偏移
    lat2 = lat1 - rand

    distance = distance + haversine(lon1, lat1, lon2, lat2)  # 总距离
    distance_per = haversine(lon1, lat1, lon2, lat2)
    stepCount_per = distance_per / 0.6
    stepCount = distance_per / 0.6 + stepCount
    activity_data = {
        "distancePerStep": 2.4 - random.randint(10, 60) / 100,  # 每秒走了多少步
        "locationType": 1,  # 根据高德api 应返回1 为GPS定位
        "stepCountCal": stepCount,  # 比总步数小一点 未证实
        "longitude": longitude,  ## 经纬度
        "activityId": id,  # id唯一值
        "latitude": latitude,
        "stepCount": stepCount,  # 总步数
        "isNormal": 'true',  # 未证实
        "distance": distance,  # 距离累加 end应返回最后一个distance
        "stepPerSecond": 3.5 - random.randint(100, 200) / 10000,  # 平均速度
    }
    with open('/Users/yinys/Sites/map.html', 'a+', encoding='utf-8') as file:
        file.write('[\'' + str(lon1) + '\', \'' + str(lat1) + '\'],\n')
    lon1 = lon2
    lat1 = lat2

    print("当前经纬度", longitude)
    print(latitude)
    print("总距离", distance)
    print("每次位移差", distance_per)
    print('总步数', stepCount)
    print("每次步数", stepCount_per)
    print("每秒走多少步", activity_data["distancePerStep"])
    print("平均速度", activity_data["stepPerSecond"])

    return



def activity():
    global longitude, latitude, lat1, lon1, lat2, lon2, stepCount, distance, start_time, targetFinishedTime
    if distance >= 1000:
        targetFinishedTime = int(time.time()) - start_time
        return
    rand = random.randint(1, 100000) / 100000000
    lon2 = lon1 + rand  # 引入随机值
    lat2 = lat1 + rand

    distance = distance + haversine(lon1, lat1, lon2, lat2)  # 总距离
    distance_per = haversine(lon1, lat1, lon2, lat2)
    stepCount_per = distance_per / 0.6
    stepCount = distance_per / 0.6 + stepCount
    activity_data = {
        "distancePerStep": 2.4 - random.randint(10, 60) / 100,  # 每秒走了多少步
        "locationType": 1,  # 根据高德api 应返回1 为GPS定位
        "stepCountCal": stepCount,  # 比总步数小一点 未证实
        "longitude": longitude,  # 经纬度
        "activityId": id,  # id唯一值
        "latitude": latitude,
        "stepCount": stepCount,  # 总步数
        "isNormal": 'true',  # 未证实
        "distance": distance,  # 距离累加 end应返回最后一个distance
        "stepPerSecond": 2.0 - random.randint(100, 200) / 10000,  # 平均速度
    }
    lon1 = lon2
    lat1 = lat2
    print("当前经纬度", longitude)
    print(latitude)
    print("总距离", distance)
    print("每次位移差", distance_per)
    print('总步数', stepCount)
    print("每次步数", stepCount_per)
    print("每秒走多少步", activity_data["distancePerStep"])
    log = r.post(url + 'api/runningActivityData',
                 headers=headers, data=activity_data).content
    log = json.loads(log)
    print(log)


# end activity
def end():
    global distance,targetFinishedTime, stepCount
    end_time = int(time.time()) - start_time  # 间隔时间
    end_data = {

        "targetFinishedTime": targetFinishedTime,  # 预测是目标完成时间
        "costTime": end_time,
        "distance": distance,  # 最后一次activity的距离
        "stepCount": stepCount,  # 步数？？
        "id": id,
    }

    end_running = r.post(url + 'api/runningActivities/end',
                         data=end_data, headers=headers).content
    end_running = json.loads(end_running)
    print(end_running)


n = 0
while n < 10:
    activity()
    n = n + 1
    rand_time = random.randint(100, 500) / 100
    print(rand_time)
    time.sleep(rand_time)

end()

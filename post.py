import requests
import time
import json
import random
from math import radians, cos, sin, asin, sqrt, pow
url = 'https://api.guangyangyundong.com/'
millis = int(round(time.time() * 1000))  # 获取时间截
r = requests.session()
start_time = int(time.time())

# 全局变量
distance = 0
longitude = 120.70645
latitude = 27.917463
lon1 = 120.70645
lat1 = 27.917463
lon2 = 120.70645
lat2 = 27.917463
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

# end activity


def end():
    global distance, targetFinishedTime, stepCount
    time.sleep(random.randint(2, 3))  # 模拟停止动作
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
    exit(0)  # 退出


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
    if distance >= 1000:
        targetFinishedTime = int(time.time()) - start_time
        end()  # 1000m 结束 计算用时
        return
    rand = round(random.randint(1, 100) / 100) / 4200   # 引入随机值
    lon2 = lon1 + pow(-1, random.randint(0, 1)) * \
        round(random.randint(1, 100) / 100) / 1000000  # 左右偏移
    lat2 = lat1 - rand

    distance = round(distance + haversine(lon1, lat1, lon2, lat2))  # 总距离
    distance_per = haversine(lon1, lat1, lon2, lat2)
    stepCount_per = distance_per / 0.6
    stepCount = round(distance_per / 0.6 + stepCount)
    activity_data = {
        # 每秒走了多少步
        "distancePerStep": round(2.4 - random.randint(10, 60) / 100, 1),
        "locationType": 1,  # 根据高德api 应返回1 为GPS定位
        "stepCountCal": stepCount - random.randint(2, 8),  # 比总步数小一点 未证实
        "longitude": lon1,  # 经纬度
        "activityId": id,  # id唯一值
        "latitude": lat1,
        "stepCount": stepCount,  # 总步数
        "isNormal": 'true',  # 未证实
        "distance": distance,  # 距离累加 end应返回最后一个distance
        # 平均速度
        "stepPerSecond": round(3.5 - random.randint(100, 200) / 1000, 1),
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
    print("平均速度", activity_data["stepPerSecond"])
    log = r.post(url + 'api/runningActivityData',
                 headers=headers, data=activity_data).content
    log = json.loads(log)
    print(log)
    return


def activity():
    global longitude, latitude, lat1, lon1, lat2, lon2, stepCount, distance, start_time, targetFinishedTime
    if distance >= 600:  # 如果大于630米要转弯 我觉得返回跑比较好 差不多这个点
        anti_activity()
        # targetFinishedTime = int(time.time()) - start_time
        return
    rand = random.randint(1, 100000) / 100000000
    lon2 = lon1 + pow(-1, random.randint(0, 1)) * \
        round(random.randint(1, 100) / 100) / 1000000  # 左右偏移 # 引入随机值
    lat2 = lat1 + rand

    distance = round(distance + haversine(lon1, lat1, lon2, lat2))  # 总距离
    distance_per = haversine(lon1, lat1, lon2, lat2)
    stepCount_per = distance_per / 0.6
    stepCount = round(distance_per / 0.6 + stepCount)
    activity_data = {
        # 每秒走了多少步
        "distancePerStep": round(2.4 - random.randint(10, 60) / 100, 1),
        "locationType": 1,  # 根据高德api 应返回1 为GPS定位
        "stepCountCal": stepCount - random.randint(2, 8),  # 比总步数小一点 未证实
        "longitude": lon1,  # 经纬度
        "activityId": id,  # id唯一值
        "latitude": lat1,
        "stepCount": stepCount,  # 总步数
        "isNormal": 'true',  # 未证实
        "distance": distance,  # 距离累加 end应返回最后一个distance
        # 平均速度
        "stepPerSecond": round(3.5 - random.randint(100, 200) / 1000, 1),
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


n = 0
while n < 90:
    activity()
    n = n + 1
    rand_time = random.randint(300, 400) / 100
    print('sleep ', rand_time, ' s\n')
    time.sleep(rand_time)  # 睡眠然后再次提交数据
end()

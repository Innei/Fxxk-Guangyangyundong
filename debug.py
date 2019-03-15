# Repo: fxxk-guangyangyundong
# By: yiny
# Date: 2019-03-07 19:27:21
#
#
# - 小数处理

import time
import random
from math import radians, cos, sin, asin, sqrt, pow
import os
from multiprocessing import Process

millis = int(round(time.time() * 1000))
start_time = int(time.time())
distance = 0
stepCount = 0
targetFinishedTime = 0
act_frequency = 0
longitude = 120.70645
latitude = 27.917463
lon1 = 120.70645
lat1 = 27.917463
lon2 = 120.70645
lat2 = 27.917463
f = open('/Users/yinys/Sites/map.html', 'w+')
f.write('''
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <title>绘制大地线</title>
    <style>
    html,
    body,
    #container {
      width: 100%;
      height: 100%;
    }
    </style>
    <script src="https://webapi.amap.com/maps?v=1.4.13&key=26681d50e598e838359e3bf4194c4669"></script>
    <script type="text/javascript" src="https://cache.amap.com/lbs/static/addToolbar.js"></script>
</head>
<body>
<div id="container"></div>
<script>
    var map = new AMap.Map('container', {
        resizeEnable: true,
        center: [120.7071, 27.917151],
        zoom: 100
    });
    var lineArr = [
    ''')
f.close()


def upload():
    print('Run child process %s (%s)...' % ("upload", os.getpid()))
    time.sleep(0.2)
    print("Success")


def log_print(distance_per, stepCount_per, activity_data):
    print("当前经纬度", lon1)
    print("         ", lat1)
    print("总距离", distance)
    print("每次位移差", distance_per)
    print('总步数', stepCount)
    print("每次步数", stepCount_per)
    print("每秒走多少步", activity_data["distancePerStep"])
    print("设定平均速度", activity_data["stepPerSecond"])
    print("实际平均速度", distance / (int(time.time()) - start_time + 0.0000001 + distance_per / activity_data[
        "stepPerSecond"]))
    print("当前用时", (int(time.time()) - start_time))
    print('等待', distance_per / activity_data["stepPerSecond"], 's\n')
    #time.sleep(distance_per / activity_data["stepPerSecond"])
    #Process(target=upload).start()

    return


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
    print(end_data)
    print(end_data["distance"] / end_data["targetFinishedTime"])
    exit(0)


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


def anti_activity():  # 回走函数
    global longitude, latitude, lat1, lon1, lat2, lon2, stepCount, distance, start_time, targetFinishedTime, act_frequency
    if distance >= 1000:
        targetFinishedTime = int(time.time()) - start_time
        with open('/Users/yinys/Sites/map.html', 'a+') as f:
            f.write(''' ];
            var polyline = new AMap.Polyline({
                path: lineArr,            // 设置线覆盖物路径
                strokeColor: '#3366FF',   // 线颜色
                strokeOpacity: 1,         // 线透明度
                strokeWeight: 2,          // 线宽
                strokeStyle: 'solid',     // 线样式
                strokeDasharray: [10, 5], // 补充线样式
                geodesic: true            // 绘制大地线
            });
            polyline.setMap(map);
        </script>
        </body>
        </html>''')
        end()  # 1000m 结束
        return
    rand = round(random.randint(70, 100) / 100) / 4200 / 3  # 引入随机值
    lon2 = lon1 + pow(-1, random.randint(0, 1)) * round(random.randint(1, 100) / 100) / 1000000  # 引入随机值
    lat2 = lat1 + rand
    act_frequency = act_frequency + 1  # 次数加1
    print(act_frequency)
    distance = round(distance + haversine(lon1, lat1, lon2, lat2))  # 总距离
    distance_per = haversine(lon1, lat1, lon2, lat2)
    stepCount_per = distance_per / 0.6
    stepCount = round(distance_per / 0.6 + stepCount)
    activity_data = {
        "distancePerStep": round(2.4 - random.randint(10, 60) / 100, 2),  # 每秒走了多少步
        "locationType": 1,  # 根据高德api 应返回1 为GPS定位
        "stepCountCal": 0,  # 比总步数小一点 未证实
        "longitude": round(lon1, 6),  ## 经纬度
        "activityId": id,  # id唯一值
        "latitude": round(lat1, 6),
        "stepCount": stepCount,  # 总步数
        "isNormal": 'true',  # 未证实
        "distance": distance,  # 距离累加 end应返回最后一个distance
        "stepPerSecond": round(3.5 - random.randint(0, 200) / 1000, 2),  # 平均速度
    }
    with open('/Users/yinys/Sites/map.html', 'a+', encoding='utf-8') as file:
        file.write('[\'' + str(lon1) + '\', \'' + str(lat1) + '\'],\n')
    lon1 = lon2
    lat1 = lat2
    log_print(distance_per, stepCount_per, activity_data)
    return


def activity():
    global longitude, latitude, lat1, lon1, lat2, lon2, stepCount, distance, start_time, targetFinishedTime, act_frequency
    if distance >= 470:  # 如果大于630米要转弯 我觉得返回跑比较好 差不多这个点
        anti_activity()
        # targetFinishedTime = int(time.time()) - start_time
        return
    if act_frequency == 0:
        # 第一次提交
        first_post_data = {
            "distancePerStep": 0.0,  # 每秒走了多少步
            "locationType": 1,  # 根据高德api 应返回1 为GPS定位
            "stepCountCal": 0,  # 比总步数小一点 未证实
            "longitude": round(longitude,6),  ## 经纬度
            "activityId": id,  # id唯一值
            "latitude": round(latitude,6),
            "stepCount": stepCount,  # 总步数
            "isNormal": 'true',  # 未证实
            "distance": distance,  # 距离累加 end应返回最后一个distance
            "stepPerSecond": 0.01,  # 平均速度
        }
        log_print(0, 0, first_post_data)
        act_frequency = act_frequency + 1
        return
    rand = round(random.randint(70, 100) / 100) / 4200 / 3
    lon2 = lon1 + pow(-1, random.randint(0, 1)) * round(random.randint(1, 100) / 100) / 1000000  # 引入随机值
    lat2 = lat1 + rand
    act_frequency = act_frequency + 1  # 次数加1
    print(act_frequency)
    distance = round(distance + haversine(lon1, lat1, lon2, lat2))  # 总距离
    distance_per = haversine(lon1, lat1, lon2, lat2)
    stepCount_per = distance_per / 0.6
    stepCount = round(distance_per / 0.6 + stepCount)
    activity_data = {
        "distancePerStep": round(2.4 - random.randint(10, 60) / 100, 2),  # 每秒走了多少步
        "locationType": 1,  # 根据高德api 应返回1 为GPS定位
        "stepCountCal": 0,  # 未知
        "longitude": round(lon1,6),  ## 经纬度
        "activityId": id,  # id唯一值
        "latitude": round(lat1,6),
        "stepCount": stepCount,  # 总步数
        "isNormal": 'true',  # 未证实
        "distance": distance,  # 距离累加 end应返回最后一个distance
        "stepPerSecond": round(3.5 - random.randint(0, 200) / 1000, 2),  # 平均速度
    }
    with open('/Users/yinys/Sites/map.html', 'a+', encoding='utf-8') as file:
        file.write('[\'' + str(lon1) + '\', \'' + str(lat1) + '\'],\n')
    lon1 = lon2
    lat1 = lat2

    log_print(distance_per, stepCount_per, activity_data)
    return


def closef():
    with open('/Users/yinys/Sites/map.html', 'a+') as f:
        f.write(''' ];
    var polyline = new AMap.Polyline({
        path: lineArr,            // 设置线覆盖物路径
        strokeColor: '#3366FF',   // 线颜色
        strokeOpacity: 1,         // 线透明度
        strokeWeight: 2,          // 线宽
        strokeStyle: 'solid',     // 线样式
        strokeDasharray: [10, 5], // 补充线样式
        geodesic: true            // 绘制大地线
    });
    polyline.setMap(map);
</script>
</body>
</html>''')


n = 0
while n < 90 * 4:
    activity()
    n = n + 1
    # rand_time = random.randint(300, 400) / 100
    # print('sleep ', rand_time, ' s\n')
    # time.sleep(rand_time)  # 睡眠然后再次提交数据
closef()

import requests
import re
import json
import time
from random import randint
from math import radians, cos, sin, asin, sqrt, pow
from multiprocessing import Process

api = 'https://api.guangyangyundong.com/'
r = requests.session()


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


class Running:
    def __init__(self, studentId, token):
        self._millis = int(round(time.time() * 1000))  # 获取时间截
        self._start_time = int(time.time())
        self._distance = 0
        self._longitude = 120.70645
        self._latitude = 27.917463
        self._lon1 = 120.70645
        self._lat1 = 27.917463
        self._lon2 = 120.70645
        self._lat2 = 27.917463
        self._stepCount = 0
        self._targetFinishedTime = 0
        self._act_frequency = 0
        self.stuId = studentId

        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; MX4 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
            'Authorization': token,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self._data = {
            # 每秒走了多少步
            "distancePerStep": round(2.4 - randint(10, 60) / 100, 1),
            "locationType": 1,  # 根据高德api 应返回1 为GPS定位
            "stepCountCal": 0,  # 比总步数小一点 未证实
            "longitude": round(self._lon1, 6),  # 经纬度
            "activityId": id,  # id唯一值
            "latitude": round(self._lat1, 6),
            "stepCount": self._stepCount,  # 总步数
            "isNormal": 'true',  # 未证实
            "distance": self._distance,  # 距离累加 end应返回最后一个distance
            # 平均速度
            "stepPerSecond": round(3.5 - randint(0, 200) / 1000, 1),
        }

        def _factoryData(self, id, distancePerStep=round(2.4 - randint(10, 60) / 100, 1), longitude=round(self._lon1, 6), latitude=round(self._lat1, 6), stepPerSecond=round(3.5 - randint(0, 200) / 1000, 1)):
            return {
                "distancePerStep": distancePerStep,
                "locationType": 1,  # 根据高德api 应返回1 为GPS定位
                "stepCountCal": 0,  # 比总步数小一点 未证实
                "longitude": longitude,  # 经纬度
                "activityId": id,  # id唯一值
                "latitude": latitude,
                "stepCount": self._stepCount,  # 总步数
                "isNormal": 'true',  # 未证实
                "distance": self._distance,  # 距离累加 end应返回最后一个distance
                # 平均速度
                "stepPerSecond": stepPerSecond,
            }
        """ 开始一次运动

        @return: void
        """

        def startRunning(self):
            data = {
                'startTime': self._millis,
                'runningSportId': 20,  # 跑步模式
                'studentId': self.stuId,
            }
            js = r.post(api + 'api/runningActivities/start',
                        data=data, headers=self._headers).content

            js = json.loads(js)
            self._id = js["id"]  # 获取当前运动id
            print('Activity ID is ', self._id)

            for i in range(200):
                self._activity_process()

        def endRunning(self):
            targetFinishedTime = int(time.time()) - self._start_time
            time.sleep(randint(2, 3))
            end_time = int(time.time()) - self._start_time
            data = {
                "targetFinishedTime": targetFinishedTime,  # 预测是目标完成时间
                "costTime": end_time,
                "distance": self._distance,  # 最后一次activity的距离
                "stepCount": self._stepCount,  # 步数？？
                "id": self._id,
            }
            activity_info = r.post(api+'api/runningActivities/end',
                                   data=data, headers=self._headers).content
            print(json.loads(activity_info))
            exit(0)  # 退出

            """ 获取此次运动 id

            :@return: ID
            """

        def getId(self):
            return self._id

        def _activity_process(self):
            if self._distance >= 530:  # 如果大于630米要转弯 我觉得返回跑比较好 差不多这个点
                self._factoryData(False)
                return
            if self._act_frequency == 0:
                self._post(self._firstPostData())
                return
            else:
                self._factoryDistance()

        def _firstPostData(self):
            return self._factoryData(self._id, 0, self._longitude + pow(-1, randint(
                0, 1)) * round(randint(1, 100) / 100) / 1000000, self._latitude + randint(1, 100) / 100 / 4200 / 300, 0.1)

        def _post(self, data):
            log = r.post(api+'api/runningActivityData',
                         headers=self._headers, data=data).content
            log = json.loads(log)
            print(log)
            self._act_frequency += 1
            return

        def _log_print(distance_per, stepCount_per, activity_data):
            print("当前经纬度", self._lon1)
            print("         ", self._lat1)
            print("总距离", self._distance)
            print("每次位移差", distance_per)
            print('总步数', self._stepCount)
            print("每次步数", stepCount_per)
            print("每秒走多少步", activity_data["distancePerStep"])
            print("设定平均速度", activity_data["stepPerSecond"])
            print("实际平均速度", self._distance / (int(time.time()) - self._start_time + 0.0000001 + distance_per / activity_data[
                "stepPerSecond"]))
            print("当前用时", (int(time.time()) - self._start_time))
            print('等待', distance_per / activity_data["stepPerSecond"], 's\n')
            time.sleep(distance_per / activity_data["stepPerSecond"])
            return

        def _factoryDistance(self, follow=True):
            rand = round(randint(85, 100) / 100) / 4200 / 3
            self._lon2 = self._lon1 + pow(-1, randint(0, 1)) * \
                round(randint(1, 100) / 100) / 1000000  # 引入随机值
            self._lat2 = self._lat1 + rand if follow else self._lat1 - rand

            if not follow and self._distance >= 1000:
                self.endRunning()

            self._act_frequency += 1
            print(self._act_frequency)
            _distance_per = haversine(
                self._lon1, self._lat1, self._lon2, self._lat2)
            _stepCount_per = _distance_per / 0.6
            self._distance = round(
                self._distance + haversine(self._lon1, self._lat1, self._lon2, self._lat2))  # 总距离
            self._stepCount = round(
                _distance_per / 0.6 + self._stepCount)
            self._lon1, self._lat1 = self._lon2, self._lat2
            data = self._factoryData(self._id)
            self._log_print(_distance_per, _stepCount_per, data)
            self._post(data)

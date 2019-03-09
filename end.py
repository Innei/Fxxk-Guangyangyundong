import requests
import json
url = 'https://api.guangyangyundong.com/'
r = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; MX4 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
    'Authorization': 'eyJhbGciOiJIUzUxMiIsInppcCI6IkRFRiJ9.eNqqViouTVKyUrI0NDE3UtJRSq0oULIyNDW1NDWzNLIw01Eqys9JLVayio6tBQAAAP__.DGeoPI2m56rXKxVJ5GKxW2KYzJ_GRZW8yfV3gLUNdSLQfOQhbUX1IAc4DEiQLT_VLL__moSqhR0hOuy1_0pcTT',
    'Content-Type': 'application/x-www-form-urlencoded'
}

end_data = {

    "targetFinishedTime": 0,  # 预测是目标完成时间
    "costTime": 50,
    "distance": 300,  # 最后一次activity的距离
    "stepCount": 455,  # 步数？？
    "id": 562794,
}

end_running = r.post(url + 'api/runningActivities/end',
                     data=end_data, headers=headers).content
#end_running = json.loads(end_running)
print(end_running)
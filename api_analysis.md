# Fxxk-Guangyangyundong

温州大学的小兄弟你们还好吗，这个api其实挺好搞得

```
{
	"startTime":1551860831865,  //时间截
	"runningSportId":	18,  // 18对应快走，19对应慢跑，20对应快跑
	"studentId":	47xxx,  // 应该是本人唯一值
}

// response start
{
	
	"id": 5457xx,  // 后面的activity id 唯一值
	"runningSportId": 18,  // 快走id
	"endRunningSportId": null,
	"studentId": 47580,
	"distance": null,
	"stepCount": null,
	"costTime": null,
	"speed": null,
	"stepPerSecond": null,
	"distancePerStep": null,
	"targetFinishedTime": null,
	"startTime": 1551860832272,  // 当前服务器时间截(毫秒) 13位
	"kcalConsumed": null,
	"qualified": null,
	"isValid": null,
	"isVerified": null,
	"qualifiedDistance": 4000,
	"qualifiedCostTime": 3360,
	"minCostTime": null,
	"endedAt": null,
	"endedBy": null

}

// activitydata
{
	"distancePerStep": 0.0,
	"locationType": 2,
	"stepCountCal": 0,
	"longitude": 120.xxxx,
	"activityId": 551760,
	"latitude": 27.9xxxxx, //坐标
	"stepCount": 0,
	"isNormal": true,
	"distance": 0,
	"stepPerSecond": 0.0,
	
}

// response data
{

	"statusMsg": "数据提交成功",
	"obj": {
		"id": 64822721, // 随机值
		"activityId": 545712, // start返回唯一值id
		"acquisitionTime": 1551860832729, //当前服务器时间截(毫秒) 13位
		"stepCount": 0,
		"stepCountCal": 0,
		"distance": 0,
		"distancePerStep": 0.0,
		"stepPerSecond": 0.0,
		"longitude": 120.707197,
		"latitude": 27.916996,
		"locationType": 4,
		"isNormal": true

	}
}


// end request
{
	"targetFinishedTime":0,
	"costTime"	:141,  // 秒
	"distance":	0, // 米
	"stepCount"	:0, 
	"id":545712, // 一次运动 唯一值
}
// response
{
	"id": 545712,
	"runningSportId": 18,
	"endRunningSportId": 18,
	"studentId": 47580,
	"distance": 0,
	"stepCount": 0,
	"costTime": 141,
	"speed": 0.0,
	"stepPerSecond": 0.0,
	"distancePerStep": 0.0,
	"targetFinishedTime": 0,
	"startTime": 1551860832000,
	"kcalConsumed": 4,
	"qualified": false,
	"isValid": true,
	"isVerified": false,
	"qualifiedDistance": 4000,
	"qualifiedCostTime": 3360,
	"minCostTime": 0,
	"endedAt": 1551860975504,
	"endedBy": null
}
```


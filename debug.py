from multiprocessing import Process

data = {

    "distance": 0,  # 距离累加 end应返回最后一个distance

}


def upload(**kwargs):
    print(kwargs)


Process(target=upload, kwargs=data).start()

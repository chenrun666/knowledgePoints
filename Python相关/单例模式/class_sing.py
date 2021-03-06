# 这种单例模式在使用多线程的时候会存在问题
class Singleton(object):

    def __init__(self, *args, **kwargs):
        import time
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


import threading


def task(arg):
    obj = Singleton.instance()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()

# a = Singleton.instance()
# b = Singleton.instance()
#
# print(a is b)

# 解决方法： 加锁

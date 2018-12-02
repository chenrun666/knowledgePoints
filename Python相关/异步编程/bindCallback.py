import time
import asyncio

now = lambda: time.time()


async def do_some_work(x):
    print("Waiting: ", x)
    return f"Done after {x}s"


# 回调函数的最后一个参数是future
def callback(future):
    print("Callback: ", future.result())


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)

task.add_done_callback(callback)
loop.run_until_complete(task)

print("TIME: ", now() - start)
print(task.result())  # 获取任务返回结果

"""
Waiting:  2
Callback:  Done after 2s
TIME:  0.00030684471130371094
"""

# 补充：
# 回调函数需要多个参数，通过偏函数导入
import functools


def callback(t, future):
    print("Callback: ", t, future.result())


task.add_done_back(functools.partial(callback, 2))

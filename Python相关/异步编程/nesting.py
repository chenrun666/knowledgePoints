"""
嵌套协程
"""

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("Waiting: ", x)

    await asyncio.sleep(x)
    return f"Done after {x}s"


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print("Task ret: ", task.result())


start = now()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print("Time: ", now() - start)

# 补充：
# 如果使用的是asyncio.gather创建协程对象，那么await的返回值就是协程运行的结果
"""
results = await asyncio.gather(*tasks)

for result in results:
    print("Task ret: ", result)
"""


##########################################################################################
# 不在main协程函数里处理结果，直接返回await的内容，那么最外层的run_until_complete将会返回main协程的结果
async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    return await asyncio.gather(*tasks)


start = now()

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main())

for result in results:
    print("Task ret : ", result)


##########################################################################################
# 或者返回asyncio.wait方式挂起协程
async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    return await asyncio.wait(tasks)


start = now()

loop = asyncio.get_event_loop()
done, pending = loop.run_until_complete(main())

for task in done:
    print("Task ret: ", task.result())


##########################################################################################
# 也可以使用asyncio的as_completed方法
async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    for task in asyncio.as_completed(tasks):
        result = await task
        print(f"Task ret: {result}")


start = now()

loop = asyncio.get_event_loop()
done = loop.run_until_complete(main())
print("Time: ", now() - start)

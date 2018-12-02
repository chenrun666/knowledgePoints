"""
使用async可以定义协程对象，使用await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数可以让出控制权。
协程遇到await，事件循环将会挂起该协程，执行别的协程，知道其他的协程也挂起或者执行完毕，在进行下一个协程的执行。
使用asyncio.sleep函数来模拟IO操作。
"""

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("Waiting: ", x)
    await asyncio.sleep(x)
    return f"Done after {x}s"


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print("Task ret: ", task.result())
print("Time: ", now() - start)

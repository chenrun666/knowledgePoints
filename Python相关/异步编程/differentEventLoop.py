"""
不同线程的事件循环
事件循环用于注册协程，而有的协程需要动态的添加事件循环中。
一个简单的方式是使用多线程，当前线程创建一个事件循环，然后在新创建一个线程，在新线程中启动事件循环。
当前线程不会被block
"""
import time
import asyncio
from threading import Thread

now = lambda: time.time()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    print(f"More work {x}")
    time.sleep(x)
    print(f"Finished more work {x}")


start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print(f"Time: {time.time() - start}")

new_loop.call_soon_threadsafe(more_work, 6)
new_loop.call_soon_threadsafe(more_work, 3)

"""
启动上述代码之后，当前线程不会被block，新线程中会按照顺序执行call_soon_threadsafe方法注册的more_work方法，
后者因为time.sleep操作是同步阻塞的，因此运行完毕more_work需要大致6 + 3
"""

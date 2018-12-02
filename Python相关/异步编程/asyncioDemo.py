"""
event_loop: 事件循环：程序开启一个无限循环，程序员会把一些函数
注册到事件循环上。当满足事件发生的时候，调用响应的协程函数

coroutine 协程： 协程对象，指一个使用async关键字定义的函数，他的
调用不会立即执行函数，而是返回一个协程对象。协程对象需要注册到事件
循环，有事件循环调用

task任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程
进一步封装，其中包含了任务的各种状态

future：代表将来执行或没有执行的任务的结果。他和task没有本质的区别
"""
import time
import asyncio

now = lambda: time.time()


async def do_some_work(x):
    print("Waiting: ", x)


start = now()

coroutine = do_some_work(2)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print("TIME: ", now() - start)

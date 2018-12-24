# 1， 进程，线程，协程的区别？
"""
    进程，计算机中资源分配的最小单位
    线程，计算机cpu调度的最小单元。一个进程中可以创建多线程，进程用于维护一个空间，线程则在此空间进行工作
    协程，在计算机中不存在。是有开发者认为创造的，也可以成为"微线程"。单纯的协程无法提高性能。
        - 协程 + IO切换，充分利用线程的使用率。不让线程闲着。
"""

# 2， GIL锁？（全局解释器锁）
"""
    保证一个进程中同时只有一个线程可以被CPU调度。
    计算型操作（利用cpu）： 多进程。
               IO型操作： 多线程， 协程
    
    应用：
        爬虫：进程 + 协程。
"""

# 3， GIL锁可以保证数据安全吗？
"""
Lock, RLock, Condition, Event
"""

# 4, IO多路复用？
"""
select， poll， epoll

    - 帮助开发者监听多个IO句柄 是否发生变化（连接，收发部署）。
        sk1 = socket.socket()
        sk1.bind(..., 8080)
        sk.listen(5)
        
        sk2 = socket.socket()
        sk2.bind(..., 8888)
        sk2.listen()
        
        while True:
            rlist, w, e = select.select([sk1, sk2], [], [], 0.5)
            for sk in rlist:
                if sk == sk1:
                    conn, addr = sk.accept()
                    conn.send("你好")
                else:
                    # 客户端发来消息
                    data = sk.recv()
                    
    - 实现IO多路复用：
        win： select 个数最多1024；轮询一个一个看
        linux：poll 轮询检测。（水平触发）
               epoll 通知 （边缘触发）

    应用场景：
        wsgiref， socket
        uwsgi, socket+IO多路复用
        nginx，IO多路复用
"""

# 5，生产者消费模型
"""

"""




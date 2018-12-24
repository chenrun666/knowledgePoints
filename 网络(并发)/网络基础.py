"""
IP： 网络层
TCP/UDP：传输层
HTTP，RTSP，FTP：应用层协议

应用层
表示层
会话层

传输层

网络层

数据链路层

物理层
"""

# 三次握手，四次挥手
# 1， 第一次，client将标志syn置为1，随机产生一个seq=J，并将数据包发送给Server
# Client进入SYN_SENT状态，等待Server确认
# 2， 第二次握手：Server收到数据包后由标志位SYN=1知道Client请求连接。
# Server将标志位SYN和ACK都置为1， ack=J+1，随机产生一个seq=K，并将数据包发送给Client确认请求连接。
# 3， 第三次握手：Client收到确认后，检查ACK时候为J+1，并将该数据包发送给Server，Server检查ack时候为K+1，
# ACK是否为1，如果正确则连接成功，Client和Server进入established状态

# 四次挥手
# 1， Client发送一个FIN后，用来关闭Client到Server的数据发送，Client进入FIN_WAIT_1状态。
# 2， Server收到FIN后，发送一个ACK给Client，确认序号为+1，Server进入CLOSE_WAIT状态
# 3， Server发送一个FIN，用来关闭Server到Client的数据发送，Server进入LAST_ACK状态。
# 4， Client收到FIN后，Client进入TIME_WAIT状态，接受发送一个ACK给Server，确认序号为收到序号+1，Server
# 进入CLOSED状态，完成


# 什么是arp协议？

# 进程池和线程池

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor  # (进程池和线程池)

# 黏包现象
""""
    缓冲区 + 连续发送数据包
    struct模块实现数据包
"""

# B/S和C/S架构

"""
请求头：
    - User-Agent
    - referer
    - accept
    - cookies
    - content-type application/json www-urlencode / form
    - host
    - connection: keepalive 保持连接状态
    
响应头：
    - location：让用户重定向到指定url
    - set-cookies, 给浏览器设置cookie
    
响应体：
    
"""

# websocket
"""

"""

x = [[1, 2, 3], [4], [5, 6, 7], [8, 9]]

b = [j for i in x for j in i]
print(b)

x = {"a": 1}
y = {"b": 2}


def foo(**kwargs):
    return kwargs


print(foo(**x, **y))


def foo1(*args):
    return {k: v for i in args for k, v in i.items()}


print(">>>", foo1(x, y))

import os


def print_directory_contents(sPath):
    parents = os.listdir(sPath)
    for parent in parents:
        child = os.path.join(sPath, parent)
        if os.path.isdir(child):
            print_directory_contents(child)
        else:
            print(child)


print_directory_contents("/Users/chenrun/面试/知识点/Python相关/python基础")

import random

li = [i for i in range(10)]
li.reverse()
print(li)
random.shuffle(li)
print(li)


def int2oct(num):
    after = oct(num)
    print(after)


int2oct(8)

a0 = dict(zip(("a", "b", "c", "d"), (1, 2, 3, 4)))
a1 = range(10)  # 生成器range(10)
a2 = [i for i in a1 if i in a0]  # []
a3 = [a0[s] for s in a0]  # [1,2,3,4]
a4 = [i for i in a1 if i in a3]  # [1,2,3,4]
a5 = {i: i * i for i in a1}  # {0:0, 1:1, 2:4....}
a6 = [[i, i * i] for i in a1]  # [[0, 0], [1, 1], [2, 4]]


def print_file(sPath):
    parents = os.listdir(sPath)
    for parent in parents:
        child = os.path.join(sPath, parent)
        if os.path.isdir(child):
            print_file(child)
        else:
            print(child)


dic_english = {}

with open("../Python相关/python基础/english.txt", "r", encoding="utf-8") as f:
    content = f.read()
    for eng in content:
        if eng not in dic_english:
            dic_english[eng] = 0
        else:
            dic_english[eng] += 1

a = sorted(dic_english, key=lambda x: dic_english[x], reverse=True)

b = {s: dic_english[s] for s in a}
count = 1
for k, v in b.items():
    print(k, v)
    count += 1
    if count >= 10:
        break

print(b)
#
# with open("../Python相关/python基础/english.txt") as file:
#     for line in file:
#         print(line)

import linecache


print(">>>>>>>>>>>>")
for i in range(1, 6):
    text = linecache.getline("../Python相关/python基础/english.txt", i)
    print(text)



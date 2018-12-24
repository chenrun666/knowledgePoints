# WebSocket协议（服务器像客户端主动推送消息）
"""
    - 基于TCP实现的协议。
    - 连接之后不断开
    - 连接之后需要进行握手
        - 获取客户发送过来的随机字符串：Sec-WebSocket-kwy: ***
        - *** + magicstr -> base64(b64.encode(hashlib.sha1()))
        - 返回给浏览器： 设置响应头：Sec-WebSocket-Accept: 加密后的值
    - 握手通过之后，进行收发数据（加密）
        - 127： 2 + 8字节  MASK（4字节） + 数据
        - 126： 2 + 2字节  MASK（4字节） + 数据
        - 125： 2字节      MASK（4字节） + 数据
    - 返回数据进行加密。
"""




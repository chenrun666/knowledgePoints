def consumer():
    r = ""

    while True:
        n = yield r
        print("consumer -- > n: %s" % n)

        if not n:
            break

        print("cosumer -- > 结束：%s" % n)

        r = "200 OK"


def product(func):
    func.send(None)  # 启动生成器，遇到yield停止
    h = 0

    while h < 5:
        h += 1
        print("produce ---> %s" % h)

        s = func.send(h)
        print("produce consumer return %s" % s)

    func.close()


c = consumer()
product(c)

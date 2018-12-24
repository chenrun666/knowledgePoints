def count(num):
    def wrapper(func):
        def inner():
            for i in range(num):
                func()

        return inner

    return wrapper


@count(3)
def foo():
    print(123)


foo()


def timer(func):
    def inner():
        func()

    return inner


@timer
def foo1():
    print("ABCD")


foo1()

# 装饰器的应用场景
"""
    - flask路由系统
    - django用户登陆
    - django csrf token  from django.views.decorators.csrf import csrf_protect,csrf_exempt
"""

for i in range(10):
    pass

print(i)  # python的作用域，python是以函数为作用域的


def wrapper(i):
    def inner():
        return i

    return inner


func_list = []

for i in range(10):
    func_list.append(wrapper(i))

print(func_list[0]())
print(func_list[1]())
print(func_list[2]())


def num():
    return (lambda x: i * x for i in range(4))


print([m(2) for m in num()])





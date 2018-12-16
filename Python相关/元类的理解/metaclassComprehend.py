# class objectCreator(object):
#     pass
#
#
# my_object = objectCreator()
# print(my_object)  # 可以打印一个类，因为他其实就是一个对象
#
#
# def echo(obj):  # 可以将类作为参数传给函数
#     print(obj)
#
#
# echo(objectCreator)
#
# objectCreator.new_attribute = "foo"  # 可以增加属性
# print(hasattr(objectCreator, "new_attribute"))
#
# objectCreatorMirror = objectCreator  # 可以赋值给你个变量
# print(objectCreatorMirror())

#
# def choose_class(name):
#     if name == "foo":
#         class Foo(object):
#             pass
#
#         return Foo
#     else:
#         class Bar(object):
#             pass
#
#         return Bar
#
#
# MyClass = choose_class("foo")
# print(MyClass)  # 返回是类，不是类的实例
#
# print(MyClass())  # 类的创建

# MyShinyClass = type("MyShinyClass", (), {})
# print(MyShinyClass)
#
# print(MyShinyClass())

# 1, 构建Foo类
# class Foo(object):
#     bar = True


#
# Foo = type("Foo", (), {"bar": True})


# class FooChild(Foo):
#     pass

# FooChild = type("FooChild", (Foo,), {})


# 3， 为FooChild类增加方法如果Python没有找到__metaclass__，他就会在模块层中寻找__metaclass__，并尝试做同样的操作。
# def echo_bar(self):
#     print(self.bar)
#
#
# FooChild = type("FooChild", (Foo,), {"echo_bar": echo_bar})
# print(hasattr(FooChild, "echo_bar"))
#
# my_foo = FooChild()
# my_foo.echo_bar()


# 1，
# class UpperAttrMetaClass(type):
#     def __new__(cls, name, bases, dic):
#         # 获取传入的属性值
#         attrs = ((name, value) for name, value in dic.items() if not name.startswith("__"))
#         # 将属性值变成大写，转换成字典
#         uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#
#         return type.__new__(cls, name, bases, uppercase_attr)
#
#
# # python3之后必须这样写
# class Foo(metaclass=UpperAttrMetaClass):
#     bar = "bip"
#
#
# f = Foo()
# print(hasattr(Foo, 'bar'))  # False
# print(hasattr(Foo, 'BAR'))  # True

# 单例模式
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instacne"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
print(s1 is s2)

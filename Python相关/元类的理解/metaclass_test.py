class MetaClassTest(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs["__FuncTest__"] = []
        for k, v in attrs.items():
            if "Chen_" in k:
                attrs["__FuncTest__"].append(k)
                count += 1
        attrs["__FuncCount__"] = count

        return type.__new__(cls, name, bases, attrs)


class MainTest(object, metaclass=MetaClassTest):

    def get_data(self, callback):
        if hasattr(self, callback):
            result = getattr(self, callback)()
            print(result, "执行完毕～～～")

    # 以后只要每次扩展Chen_开头的函数，就会自动执行。
    def Chen_Run(self):
        return "Chenrun"

    def Chen_Peng(self):
        return "ChenPeng"


def run():
    obj = MainTest()
    for func in range(obj.__FuncCount__):
        obj.get_data(callback=obj.__FuncTest__[func])


if __name__ == '__main__':
    run()

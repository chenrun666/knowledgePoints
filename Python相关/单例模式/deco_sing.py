def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)

        return _instance[cls]

    return _singleton


@singleton
class A(object):
    a = 1

    def __int__(self, x=0):
        self.x = x


a1 = A()
a2 = A()

print(a1 is a2)

class Singleton(type):
    def __init__(self, *args, **kwargs):
        print("__init__")
        self._instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__")
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance


class Foo(metaclass=Singleton):
    pass


foo1 = Foo()
foo2 = Foo()

print(Foo.__dict__)
print(foo1 is foo2)

# __init__
# __call__
# __call__

# {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Foo' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None,
# '_instance': <__main__.Foo object at 0x102a034e0>}

# True
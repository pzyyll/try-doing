# class Singleton(object):
#     _instance = None
#     def __new__(klass, *args, **kwargs):
#         if not klass._instance:
#             klass._instance = object.__new__(klass, *args, **kwargs)
#         return klass._instance


# class Foo(Singleton):
#     def __init__(self):
#         print('init Foo.')


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Python2
class Foo(object):
    __metaclass__ = Singleton

    def __init__(self):
        print('myclass.')

z = Foo()
z1 = Foo()
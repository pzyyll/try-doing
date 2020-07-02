from importall import *

class A(object):
    def __init__(self):
        self._tableFunc = {
            1: self._fun,
        }

    def _fun(self):
        pass

a = A()
del a.__dict__
del a

objgraph.show_backrefs(objgraph.by_type('A') , filename=ogpath('c04.png'), max_depth=10)
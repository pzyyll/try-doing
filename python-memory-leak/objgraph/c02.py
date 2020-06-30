from importall import *

class A(object):
    def __init__(self, owner):
        self.owner = owner

class B(object):
    def __init__(self):
        self.a = A(self)
        self.c = C()
        self.c1 = C()

class C(object):
    pass

b = B()

del b

objgraph.show_backrefs(objgraph.by_type('A')+objgraph.by_type('B')+objgraph.by_type('C') , filename=ogpath('c02.png'))
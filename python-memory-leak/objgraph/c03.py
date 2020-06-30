from importall import *

class A(object):
    def __init__(self, owner):
        self.owner = owner
        self.owner.setCb(self.cb)

    def cb(self):
        pass

class B(object):
    def setCb(self, cb):
        self.cb = cb

b = B()
a = A(b)

objgraph.show_backrefs(objgraph.by_type('A')+objgraph.by_type('B')+objgraph.by_type('C') , filename=ogpath('c03-01.png'),max_depth=10)

del a
del b

objgraph.show_backrefs(objgraph.by_type('A')+objgraph.by_type('B')+objgraph.by_type('C') , filename=ogpath('c03.png'))
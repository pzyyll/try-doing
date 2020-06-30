import objgraph, gc
from ogpath import ogpath

gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)

class A(object):
    pass

class B(object):
    pass

a = A()
b = B()

a.b = b
b.a = a

del a
del b

objgraph.show_backrefs(objgraph.by_type('A')+objgraph.by_type('B'), filename=ogpath('c01.png'))

print 'start gc.'
gc.collect()
print 'end gc.'
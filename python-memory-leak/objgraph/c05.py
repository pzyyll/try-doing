from importall import *

class A(object):
    def fun(self):
        try:
            1/0
        except :
            import sys
            exc_info = sys.exc_info()
            sys.excepthook(*exc_info)
            #del exc_info

a = A()
a.fun()

del a

objgraph.show_backrefs(objgraph.by_type('A') , filename=ogpath('c05.png'), max_depth=10)
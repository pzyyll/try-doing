import objgraph
from ogpath import ogpath

x = []
y = [x, [x], dict(x=x)]

objgraph.show_refs([y], filename=ogpath('ot0.png'))
objgraph.show_backrefs([y], filename=ogpath('ot1.png'))

objgraph.show_refs([x], filename=ogpath('ot2-0.png'))
objgraph.show_backrefs([x], filename=ogpath('ot2.png'))

objgraph.show_most_common_types()

# class A(object):
#     pass

# class B(object):
#     pass

# a = A()
# b = B()
# a.b = b
# b.a = a

# objgraph.show_refs([a], filename=ogpath('zsample-graph.png'))
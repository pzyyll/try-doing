import objgraph as objg
from ogpath import ogpath


class MyBigFatObject(object):
    pass

def comps(_cache={}):
    _cache[42] = dict(foo=MyBigFatObject(), bar=MyBigFatObject())

    x = MyBigFatObject()


objg.show_growth()
comps()
objg.show_growth()

print 1, objg.by_type('MyBigFatObject')

import random
objg.show_chain(
    objg.find_backref_chain(random.choice(objg.by_type('MyBigFatObject')), objg.is_proper_module),
    filename=ogpath('chain.png'))


import node as sn

x = sn.Symbol('x')
y = sn.Symbol('y')
z = sn.Symbol('z')

def post_traversal(expr,fn):
    return fn(expr,tuple(post_traversal(o,fn) for o in expr.operands))

from functools import singledispatch
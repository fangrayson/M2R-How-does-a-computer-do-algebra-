#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:31:10 2019

@author: aishy
"""

def post_traversal(expr,fn):
    if (isinstance(expr, Symbol) or isinstance(expr, Numberclass) or isinstance(expr, Number)):
        return fn(expr, 0)
    else:
        return fn(expr,tuple(post_traversal(o,fn) for o in expr.operands))

from functools import singledispatch
@singledispatch
def diff(node,doperands):
    pass
      
@diff.register(Add)
def _(node,doperands):
    return doperands[0]+doperands[1]

@diff.register(Sub)
def _(node,doperands):
    return doperands[0]-doperands[1]

@diff.register(Mul)
def _(node,doperands):
    return doperands[0]*node.operands[1]+node.operands[0]*doperands[1]

@diff.register(Div)
def _(node,doperands):
    return (doperands[0]*node.operands[1]-node.operands[0]*doperands[1])/(node.operands[1]**2)

@diff.register(Pow)
def _(node,doperands):
    return node.operands[1] * doperands[0] * (node.operands[0]**(node.operands[1]-1))

@diff.register(Neg)
def _(node,doperands):
    return -doperands[0]

@diff.register(Number)
def _(node, doperands):
    return 0

@diff.register(Symbol)
def _(node, doperands):
    if node == x:
        return 1
    return 0

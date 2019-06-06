#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:31:10 2019

@author: aishy
"""
 
import node as sn

def diff(expr, symbol):
    return post_traversal(expr, diff_visitor)
    


def post_traversal(expr,fn):
    '''if (isinstance(expr, Symbol) or isinstance(expr, Numberclass) or isinstance(expr, Number)):
        return fn(expr, tuple())
    else:'''
    return fn(expr,tuple(post_traversal(o,fn) for o in expr.operands))

from functools import singledispatch
@singledispatch
def diff_visitor(node,doperands):
    pass
      
@diff_visitor.register(sn.Add)
def _(node,doperands):
    return doperands[0]+doperands[1]

@diff_visitor.register(sn.Sub)
def _(node,doperands):
    return doperands[0]-doperands[1]

@diff_visitor.register(sn.Mul)
def _(node,doperands):
    return doperands[0]*node.operands[1]+node.operands[0]*doperands[1]

@diff_visitor.register(sn.Div)
def _(node,doperands):
    return (doperands[0]*node.operands[1]-node.operands[0]*doperands[1])/(node.operands[1]**2)

@diff_visitor.register(sn.Pow)
def _(node,doperands):
    return node.operands[1] * doperands[0] * (node.operands[0]**(node.operands[1]-1))

@diff_visitor.register(sn.Neg)
def _(node,doperands):
    return -node

@diff_visitor.register(sn.Number)
def _(node, doperands):
    return 0

    @diff_visitor.register(sn.Symbol)
    def _(node, doperands):
        if node == symbol:
            return 1
        return 0

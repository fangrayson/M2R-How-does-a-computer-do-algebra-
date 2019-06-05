#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:31:10 2019

@author: aishy
"""

def post_traversal(expr,fn):
    return fn(expr,tuple(post_traversal(o,fn) for o in expr.operands))


from functools import singledispatch
@singledispatch
def diff(node,doperands):
    if (isinstance(node,Symbol)==True and node!=x) or isinstance(node,Numberclass)==True:
        return 0
    elif node==x:
        return 1
    


    
@diff.register(Add)
def _(node,doperands):
    return doperands[0]+doperands[1]

@diff.register(Sub)
def _(node,doperands):
    return doperands[0]-doperands[1]

@diff.register(Mul)
def _(node,doperands):
    return doperands[0]*Node.operands[1]+Node.operands[0]*doperands[1]

@diff.register(Div)
def _(node,doperands):
    return (doperands[0]*Node.operands[1]-Node.operands[0]*doperands[1])/(Node.operands[1]**2)

@diff.register(Pow)
def _(node,doperands):
    return 

@diff.register(Neg)
def _(node,doperands):
    return -doperands[0]
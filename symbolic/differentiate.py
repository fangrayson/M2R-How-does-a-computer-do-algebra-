#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:31:10 2019

@author: aishy
"""
 
import node as sn
import visitor as vi

x = sn.Symbol('x')
y = sn.Symbol('y')
z = sn.Symbol('z')

from functools import singledispatch
def diff(expr, symbol):
    if isinstance(expr, sn.Numberclass):
        return 0
    
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
        return -doperands[0]
    
    @diff_visitor.register(sn.Terminal)
    def _(node, doperands):
        if node == symbol:
            return 1
        else:
            return 0
        
    @diff_visitor.register(sn.Log)
    def _(node, doperands):
        return doperands[0] / node.operands[0]
    
    @diff_visitor.register(sn.Exp)
    def _(node, doperands):
        return doperands[0] * node
    
    @diff_visitor.register(sn.Sin)
    def _(node, doperands):
        return doperands[0] * sn.cos(node.operands[0])
    
    @diff_visitor.register(sn.Cos)
    def _(node, doperands):
        return doperands[0] * sn.sin(node.operands[0])
        
    return vi.post_traversal(expr, diff_visitor)


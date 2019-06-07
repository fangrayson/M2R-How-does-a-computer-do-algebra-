#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:00:17 2019

@author: aishy
"""

from numbers import Number as Numberclass


class Node: 
    
    def parenthesize(self,other):
        if self.priority > other.priority:
            return '(' + str(other.name)+ ')'
        else:
            return str(other.name)

    def __add__(self, other):
        if isinstance(other, Numberclass):
            other=Number(other)
        return Add(self,other)
    
    def __radd__(self,other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Add(self,other)
    
    def __sub__(self, other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Sub(self, other)
    
    def __rsub__(self, other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Sub(other, self)
    
    def __mul__(self, other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Mul(self, other)
    
    def __rmul__(self, other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Mul(self, other)
    
    def __truediv__(self, other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Div(self, other) 
    
    def __rtruediv__(self, other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Div(other, self)
    
    def __pow__(self, other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Pow(self, other)
    
    def __rpow__(self, other):
        if isinstance(other,Numberclass):
            other=Number(other)
        return Pow(other, self)
    
    def __neg__(self):
        return Neg(self)


    
class BinaryOperator(Node):
    def __init__(self, a, b):
        self.operands = (a,b)
        self.name = self.parenthesize(self.operands[0]) + " " + self.symbol\
        + " " + self.parenthesize(self.operands[1])
    
    def __str__(self):
        return self.parenthesize(self.operands[0]) + " " + self.symbol\
    + " " + self.parenthesize(self.operands[1])

    
class UnaryOperator(Node):
    def __init__(self, c):
        self.operands = (c,)
        self.name = self.symbol+self.parenthesize(self.operands[0])
        
    def __str__(self):
        return self.symbol+self.parenthesize(self.operands[0])
    

class Neg(UnaryOperator):
    symbol = "-"
    priority = 3
 
    
class Terminal(Node):
    def __init__(self):
        self.operands = (())
    priority = 7
    
    
    
class Symbol(Terminal):
    def __init__(self, name):
        self.name = name
        self.operands = (())
    
    
class Number(Terminal):
    def __init__(self, value):
        self.name = value
    

        
class Add(BinaryOperator):
    symbol = '+'
    priority = 1
    
                    
class Sub(BinaryOperator):
    symbol = "-"
    priority = 1
    
        
class Mul(BinaryOperator):
    symbol = "*"
    priority = 4
    
        
class Div(BinaryOperator):
    symbol = "/"
    priority = 5
    
    
class Pow(BinaryOperator):
    symbol = "**" 
    priority = 6
    
    

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

    
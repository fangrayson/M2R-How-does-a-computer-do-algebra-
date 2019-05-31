#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:42:28 2019

@author: aishy
"""

class Node: 
    pass
""" def parenthesize(self,other):
        if self.priority>other.priority:
            return '('+str(other)+')'
        else:
            return str(other)"""
    
    
#class Operator(Node):
    
'''class UnitaryOperator(Node):
    def __init__(self, a):
        self.operands = (a)
        
    def __str__(self):
        return str(self.operands[0])

class UnaryMinus(UnitaryOperator):
    symbol = "-"'''

    
class BinaryOperator(Node):
    def __init__(self, a, b):
        self.operands = (a,b)
    
    def __str__(self):
        return str(self.operands[0]) + " " + self.symbol\
    + " " + str(self.operands[1])
    
class Symbol(Node):
    def __init__(self, name):
        self.name = name
        
        
class Add(BinaryOperator):
    symbol = '+'
    def __add__(self, other):
        return Add(self,other)
                
   
    
    
class Sub(BinaryOperator):
    symbol = "-"
    
    
    def __sub__(self, other):
        return Sub(self, other) 
   
    
class Mul(BinaryOperator):
    symbol = "*"
    
    
    def __mul__(self, other):
        return Mul(self, other)

    
class Div(BinaryOperator):
    symbol = "/"
    
    
    def __div__(self, other):
        return Div(self, other) 

    
class Pow(BinaryOperator):
    symbol = "**"  
    
    
    def __pow__(self, other):
        return Pow(self, other)
    
    
    
x = Symbol('x').name
y = Symbol('y').name
z = Symbol('z').name    

    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:00:17 2019

@author: aishy
"""

class Node: 
    
<<<<<<< HEAD
    
=======
    def parenthesize(self,other):
        if self.priority > other.priority:
            return '(' + str(other.name)+ ')'
        else:
            return str(other.name)
>>>>>>> b6ac402033133b14c7317ab4c396346091143139
        
    def __add__(self, other):
        return Add(self.name,other.name)
    def __radd__(self,other):
        return Add(other.name,self.name)
    
    def __sub__(self, other):
        return Sub(self.name, other.name)
    
    def __mul__(self, other):
        return Mul(self.name, other.name)
    
<<<<<<< HEAD
    def __truediv__(self, other):
=======
    def __trudiv__(self, other):
>>>>>>> b6ac402033133b14c7317ab4c396346091143139
        return Div(self.name, other.name) 
    
    def __pow__(self, other):
        return Pow(self.name, other.name)
    
    def __neg__(self):
        return Neg(self.name)


    
class BinaryOperator(Node):
    def __init__(self, a, b):
        self.operands = (a,b)
    
    def __str__(self):
        return str(self.operands[0]) + " " + self.symbol\
    + " " + str(self.operands[1])
    
<<<<<<< HEAD
    def parenthesize(self,other):
        if self.priority > other.priority:
            return '(' + str(other.name)+ ')'
        else:
            return str(other.name)
    
=======
>>>>>>> b6ac402033133b14c7317ab4c396346091143139
    
    

    
class UnitaryOperator(Node):
    def __init__(self, a):
        self.operands = (a)
        
    def __str__(self):
        return self.symbol+str(self.operands[0])

class Neg(UnitaryOperator):
    symbol = "-"
    priority = 3
    
    
class Symbol(Node):
    def __init__(self, name):
        self.name = name
        
        
class Add(BinaryOperator):
    symbol = '+'
    priority = 1
    def __init__(self, a, b):
        self.operands = (a,b)
        self.name = str(self.operands[0]) + " " + self.symbol + " " + str(self.operands[1])

                    
class Sub(BinaryOperator):
    symbol = "-"
    priority = 2
    def __init__(self, a, b):
        self.operands = (a,b)
        self.name = str(self.operands[0]) + " " + self.symbol + " " + str(self.operands[1])
    
        
class Mul(BinaryOperator):
    symbol = "*"
    priority = 4
    def __init__(self, a, b):
        self.operands = (a,b)
        self.name = str(self.operands[0]) + " " + self.symbol + " " + str(self.operands[1])
    
        
class Div(BinaryOperator):
    symbol = "/"
    priority = 5
    def __init__(self, a, b):
        self.operands = (a,b)
        self.name = str(self.operands[0]) + " " + self.symbol + " " + str(self.operands[1])
    
    
class Pow(BinaryOperator):
    symbol = "**" 
    priority = 6
    def __init__(self, a, b):
        self.operands = (a,b)
        self.name = str(self.operands[0]) + " " + self.symbol + " " + str(self.operands[1])
    
    
   
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

    
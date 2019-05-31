#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:38:27 2019

@author: aishy
"""

class Node: 
     
class Operator(Node):
    
class UnitaryOperator(Operator):
    def __init__(self, a):
        self.operands = (a)
        
    def __str__(self):
        return str(self.operands[0])

class UnaryMinus(UnitaryOperator):
    symbol = "-"

    
class BinaryOperator(Operator):
    def __init__(self, a, b):
        self.operands = (a,b)
        
    def __str__(self):
        return str(self.operands[0]) + " " + symbol + " " + str(self.operands[1])
        
        
class Add(BinaryOperator):
    symbol = "+"
    def __add__(self, other):
        return Add(self, other)

class Sub(BinaryOperator):
    symbol = "-"
    def __sub__(self, other):
        return Sub(self, other)
    
class Mul(BinaryOperator):
    symbol = "x"
    def __mul__(self, other):
        return Mul(self, other)
    
class Div(BinaryOperator):
    symbol = "/"
    def __div__(self, other):
        return Div(self, other)
    
class Pow(BinaryOperator):
    symbol = "^"
    def __pow__(self, other):
        return Pow(self, other)
    
    
    
    
    
    
    
    
    
    
    
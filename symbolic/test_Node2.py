#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:42:28 2019

@author: aishy
"""
import pytest
class Node:
    #def __init__(self):
    #    pass
    def __add__(self, other):
        return print(Add(self, other))
    
#def __add__(self, other):
        #return print(Add(self,a , b))
#    return print(Add(self, other))
        #return "HELLOOOO" (this was just a test)
#def __sub__(self, other):
#    return print(Sub(self, other))
#def __mul__(self, other):
#    return print(Mul(self, other))
#def __div__(self, other):
#    return print(Div(self, other))
#def __pow__(self, other):
#        return print(Pow(self, other))
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
        return str(self.operands[0]) + " " + self.symbol + " " + str(self.operands[1])
    
class Symbol(Node):
    def __init__(self, name):
        self.name = name
        
        
class Add(BinaryOperator):
    symbol = '+'
    
class Sub(BinaryOperator):
    symbol = "-"
    
class Mul(BinaryOperator):
    symbol = "*"
    
class Div(BinaryOperator):
    symbol = "/"
    
class Pow(BinaryOperator):
    symbol = "**"  
    
    
x = Symbol('x').name
y = Symbol('y').name
z = Symbol('z').name

def test_symbol_1(): # testing the Symbol class works
    assert x == 'x'
""" PASSED """
def actual_addition(a, b):
    if (type(a) == str) or (type(b) == str):
        return a + " + " + b
    return a + b
def test_addition_1(): #testing that simple addition works
    assert x + y == actual_addition(x, y)
""" FAILED """
def test_addition_2(): #testing that addition is symmetric
    assert x + y == actual_addition(y, x)
""" FAILED """

    
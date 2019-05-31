#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:38:27 2019

@author: aishy
"""

class Node: 
    def parenthesize(self,other):
        if self.priority>other.priority:
            return '('+str(other)+')'
        else:
            return str(other)
    
    
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
        return self.parenthesize(self.operands[0]) + " " + self.symbol\
    + " " + self.parethesize(self.operands[1])
    
        
        
class Add(BinaryOperator):
    symbol = "+"  
    priority=1
    
class Sub(BinaryOperator):
    symbol = "-"
    priority=2
    
class Mul(BinaryOperator):
    symbol = "*"
    priority=3
    
class Div(BinaryOperator):
    symbol = "/"
    priority=4
    
class Pow(BinaryOperator):
    symbol = "^"  # potentially use "**" here
    priority=5    
    
    
    
    
    

    
    
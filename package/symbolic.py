#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:38:27 2019

@author: aishy
"""

class Node: 
    pass
     
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
    
        
        
class Add(BinaryOperator):
    symbol = "+"  
    
class Sub(BinaryOperator):
    symbol = "-"
        
class Mul(BinaryOperator):
    symbol = "*"
  
class Div(BinaryOperator):
    symbol = "/"
  
class Pow(BinaryOperator):
    symbol = "^"  # potentially use "**" here
        
    
    
    
    
    

    
    
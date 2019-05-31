#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:38:27 2019

@author: aishy
"""

class Node: 
<<<<<<< HEAD
     def __init__(self):
         pass
#class Operator(Node):
    
'''class UnitaryOperator(Node):
=======
     
class Operator(Node):
    
class UnitaryOperator(Operator):
>>>>>>> 47a21062897d9770489a747b213de00b87496180
    def __init__(self, a):
        self.operands = (a)
        
    def __str__(self):
        return str(self.operands[0])

class UnaryMinus(UnitaryOperator):
<<<<<<< HEAD
    symbol = "-"'''

    
class BinaryOperator(Node):
    def __init__(self, a, b):
        self.operands = (a,b)
        
   # def __str__(self):
 #       return str(self.operands[0]) + " " + symbol + " " + str(self.operands[1])
    
=======
    symbol = "-"

    
class BinaryOperator(Operator):
    def __init__(self, a, b):
        self.operands = (a,b)
        
    def __str__(self):
        return str(self.operands[0]) + " " + symbol + " " + str(self.operands[1])
>>>>>>> 47a21062897d9770489a747b213de00b87496180
        
        
class Add(BinaryOperator):
    symbol = "+"
<<<<<<< HEAD
        
    def __add__(self, other):
        return Add(self,other)
    
    
def __str__(self):
    return str(self.operands[0]) + " " + symbol + " " + str(self.operands[1])

"""class Sub(BinaryOperator):
    def __init__(self, a, b):
        self.symbol = "-"
        
=======
    def __add__(self, other):
        return Add(self, other)

class Sub(BinaryOperator):
    symbol = "-"
>>>>>>> 47a21062897d9770489a747b213de00b87496180
    def __sub__(self, other):
        return Sub(self, other)
    
class Mul(BinaryOperator):
<<<<<<< HEAD
    def __init__(self, a, b):
        self.symbol = "*"
        
=======
    symbol = "x"
>>>>>>> 47a21062897d9770489a747b213de00b87496180
    def __mul__(self, other):
        return Mul(self, other)
    
class Div(BinaryOperator):
<<<<<<< HEAD
    def __init__(self, a, b):
        self.symbol = "/"
        
=======
    symbol = "/"
>>>>>>> 47a21062897d9770489a747b213de00b87496180
    def __div__(self, other):
        return Div(self, other)
    
class Pow(BinaryOperator):
<<<<<<< HEAD
    def __init__(self, a, b):
        self.symbol = "^"  # potentially use "**" here
        
    def __pow__(self, other):
        return Pow(self, other)"""
=======
    symbol = "^"
    def __pow__(self, other):
        return Pow(self, other)
>>>>>>> 47a21062897d9770489a747b213de00b87496180
    
    
    
    
    
    
    
    
    
    
    
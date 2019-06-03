import pytest
# IMPORTING NODE DOESN'T WORK?

class Node: 
    
    def parenthesize(self,other):
        if self.priority > other.priority:
            return '(' + str(other.name)+ ')'
        else:
            return str(other.name)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Add(self.name,other)
        return Add(self.name,other.name)
    def __radd__(self,other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Add(other, self.name)
        return Add(self.name,other.name)
    
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Sub(self.name, other)
        return Sub(self.name, other.name)
    def __rsub__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Sub(other, self.name)
        return Sub(other, self.name)
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Mul(self.name, other)
        return Mul(self.name, other.name)
    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Mul(other, self.name)
        return Mul(other, self.name)
    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Div(self.name, other)
        return Div(self.name, other.name) 
    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Div(other, self.name)
        return Div(other, self.name)
    def __pow__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Pow(self.name, other)
        return Pow(self.name, other.name)
    def __rpow__(self, other):
        if type(other) == int or type(other) == float:
            self.priority = 0
            return Pow(other, self.name)
        return Pow(other, self.name)
    def __neg__(self):
        return Neg(self.name)


    
class BinaryOperator(Node):
    def __init__(self, a, b):
        self.operands = (a,b)
    
    def __str__(self):
        return str(self.operands[0]) + " " + self.symbol\
    + " " + str(self.operands[1])

    
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

    
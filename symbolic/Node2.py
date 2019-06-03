
class Node: 
    
    def __add__(self, other):
        return Add(self,other)
    def __radd__(self,other):
        return Add(other,self)
    
    def __sub__(self, other):
        return Sub(self, other)
    
    def __mul__(self, other):
        return Mul(self, other)
    
    def __div__(self, other):
        return Div(self, other) 
    
    def __pow__(self, other):
        return Pow(self, other)
    
    def __neg__(self):
        return Neg(self)

""" def parenthesize(self,other):
        if self.priority>other.priority:
            return '('+str(other)+')'
        else:
            return str(other)"""
    
    

    
class BinaryOperator(Node):
    def __init__(self, a, b):
        self.operands = (a,b)
    
    def __str__(self):
        return str(self.operands[0]) + " " + self.symbol\
    + " " + str(self.operands[1])
    
#class Operator(Node):
    
class UnitaryOperator(Node):
    def __init__(self, a):
        self.operands = (a)
        
    def __str__(self):
        return self.symbol+str(self.operands[0])

class Neg(UnitaryOperator):
    symbol = "-"
    
    
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

    
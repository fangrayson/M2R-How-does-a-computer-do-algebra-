import pytest
#import symbolic
import sympy as sy
x = sy.Symbol('x')

# IN FUTURE: THIS WILL ALL BE PASSED DOWN FROM THE symbolic.py PACKAGE
class Node: 
    pass
     
class Operator(Node):
    pass
    
class UnitaryOperator(Operator):
    def __init__(self, a):
        self.operands = (a)
        
    def __str__(self):
        return str(self.operands[0])

class UnaryMinus(UnitaryOperator):
    symbol = "-"
       
#THIS WILL BE THE ACTUAL TEST
def actual_unary_minus(x):
    return  -x

def test_func():
    assert UnaryMinus(x) == actual_unary_minus(x)

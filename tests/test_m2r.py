#Example of a test
#Go onto 
#import symbolic.py
#Seems to be an indentation error in test_m2r.py
#def actual_unary_minus(x):
#    return  -x

#def test_func(x):
#    assert symbolic.UnaryMinus(x) == actual_unary_minus(x)
#Keep getting the error "No module named 'symbolic'"
import pytest
# Decided to copy and paste the classes and adjusted a bit,
# becuase the package needs to be in the same directory or something?

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
       
def actual_unary_minus(x):
    return  str(-x)

def test_func():
    x =  1
    assert UnaryMinus(x) == actual_unary_minus(x)
#Keep getting the error "No module named 'symbolic'"
    
#FIRST ERROR: may need to add "pass" or an empty indentation block
# don't think can have an empty class cus it keeps going weird
    
#SECOND ERROR: "fixture x not found"
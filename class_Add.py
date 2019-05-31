class Node:
    pass
x=symbol('x') 
class BinaryOperator(Node):
    def __init__(self,a,b):
        self.operands=(a,b)
    def __str__(self):
        return str(self.operands[0])+" "+self.symbol+" "+str(self.operands[1])
class Add(BinaryOperator):
    symbol='+'
    def __add__(self,other):
        return Add(self,other)
    def __radd__(self,other):
        return Add(self,other)
       
    



    

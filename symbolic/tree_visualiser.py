
import node as sn

from graphviz import Digraph


x = sn.Symbol('x')
y = sn.Symbol('y')
z = sn.Symbol('z')

def post_traversal(expr,fn):
    return fn(expr,tuple(post_traversal(o,fn) for o in expr.operands))



from functools import singledispatch
@singledispatch
def visitor_function(expr,voperands):
    dot=Digraph(comment='Abstract Syntax Tree')
    count=0
    
    @visitor_function.register(sn.Operator)
    def _(expr,child_node_names):
        count+=1
        node_name="N%d"%count
        dot.node(node_name,expr.symbol)
        for n in child_node_names:
            dot.edge(node_name,n)
        return node_name
    
    @visitor_function.register(sn.Terminal)
    def _(expr,child_node_names):
        node_name=str(expr.name)
        dot.node(node_name,expr.name)
        return node_name
        
    return dot.source
        
        
        
    
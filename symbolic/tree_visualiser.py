import node as sn
import visitor as vi
from graphviz import Digraph

x = sn.Symbol('x')
y = sn.Symbol('y')
z = sn.Symbol('z')

'''def high_tree_maker(expr):
    def tree_maker(expr):
        dot=Digraph(comment='Abstract Syntax Tree for ' + str(expr))
        tree = tree_visualiser(expr)
        #return dot.source
    print(dot.source)'''
    #FAILED ATTEMPT TO CREATE A FUNCTION THAT PRINTS OUT THE DIGRAPH CODE

dot = Digraph(comment='Abstract Syntax Tree')

def tree_visualiser(expr):
    vi.count = 0
    from functools import singledispatch
    @singledispatch
    def tree_visitor(expr,child_node_names):
        pass

    @tree_visitor.register(sn.Operator)
    def _(expr,child_node_names):
        vi.count+=1
        node_name="N%d" %vi.count
        dot.node(node_name,expr.symbol)
        for n in child_node_names:
            dot.edge(node_name,n)
        return node_name

    @tree_visitor.register(sn.Terminal)
    def _(expr,child_node_names):
        vi.count+=1
        node_name="N%d" %vi.count
        dot.node(node_name,expr.name)
        return node_name
    return vi.post_traversal(expr, tree_visitor)
    
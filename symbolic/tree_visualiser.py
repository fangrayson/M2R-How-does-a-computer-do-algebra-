import node as sn
import visitor as vi
from graphviz import Digraph

x = sn.Symbol('x')
y = sn.Symbol('y')
z = sn.Symbol('z')

dot=Digraph(comment='Abstract Syntax Tree')

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
    
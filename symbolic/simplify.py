
def post_traversal(expr,fn):
    return fn(expr,tuple(post_traversal(o,fn) for o in expr.operands))


from functools import singledispatch
@singledispatch
def simpl(Node,operands):
    


    
@simpl.register(Add)
def _(Node,operands):
    return Node.operands[0]+Node.operands[1]
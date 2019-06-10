import node as sn #not entirely sure if needed, definitely will be needed later
count = 0
def post_traversal(expr,fn):
    return fn(expr,tuple(post_traversal(o,fn) for o in expr.operands))

""" STILL TO DO:
    1. Define "evaluate", a visitor function that will replace symbols with an input value
    2. Define a visitor function (that only visits a finite number of times) that checks if
        (expr_1) + (expr_2) can be 'simplified' i.e. basic simplification of numbers
        i.e. check x + 1 + x + 2 against x + 1 + 2 + x
        i.e. the rhs is x + 2, check if 2 + x will cause a simplification
"""
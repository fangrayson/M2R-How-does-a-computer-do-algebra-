#Example of a test
#Go onto 
def actual_unary_minus(x):
    return  -x

def test_func(x):
    assert symbolic.UnaryMinus(x) == actual_unary_minus(x)
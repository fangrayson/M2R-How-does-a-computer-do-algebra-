""" IMPORTING SYMBOLIC & ADDING A DIRECTORY TO SEARCH PATH """
import os
newdirectory = os.path.abspath("..")
import sys
if (str(newdirectory) in sys.path)==False:
    sys.path += [str(newdirectory)]
import symbolic.node as sn
x = sn.Symbol('x')
y = sn.Symbol('y')
z = sn.Symbol('z')
##############################################################################
""" SYMBOL CLASS TEST """
def test_symbol_notation():
    assert str(x) == 'x'
""" UNARY MINUS TEST """
def test_unary_minus():
    assert str(-x) == '-x'
""" BINARY OPERATIONS TEST """
def test_addition_symbol_add_symbol():
    assert str(x + y) == 'x + y'
def test_addition_symbol_add_int():
    assert str(x + 2) == 'x + 2'
def test_addition_symbol_add_symbol_add_symbol():
    assert str(x + y + z) == 'x + y + z'
def test_multiplication_symbol_mul_symbol():
    assert str(x + y) == 'x * y'
def test_multiplication_symbol_mul_int():
    assert str(x * 2) == '2 * x'
def test_multiplication_symbol_mul_symbol_mul_symbol():
    assert str(x * y * z) == 'x * y * z'
def test_bidmas_1():
    assert str(x + y * z) == 'x + y * z'
def test_bidmas_2():
    assert str((x+y)*z) == '(x + y) * z'
def test_bidmas_3():
    assert str((x + y - 1)/(x * 2)) == '(x + y - 1) / (2 * x)'
def test_bidmas_4():
    assert str(x + y - 1/(x * 2)) == 'x + y - 1 / (x * 2)'
def test_bidmas_5():
    assert str(x + y - (1/x) + 2) == 'x + y - 1 / x + 2'
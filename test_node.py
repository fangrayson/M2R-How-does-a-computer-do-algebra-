# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:14:01 2019

@author: Fan
"""
import symbolic.node as sn
x = sn.Symbol('x')
y = sn.Symbol('y')
z = sn.Symbol('z')

def test_symbol_notation():
    assert x.name == 'x'
""" PASSED """

def test_addition_symbol_add_symbol():
    assert (x + y).name == 'x + y'

def test_addition_symbol_add_int():
    assert (x + 2).name == 'x + 2'
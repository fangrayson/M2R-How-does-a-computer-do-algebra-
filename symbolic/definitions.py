#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:35:38 2019

@author: aishy
"""

import node
from sympy import Symbol

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')


def __add__(self, other):
        return Add(self,other)        
    
def __sub__(self, other):
    return Sub(self, other)    
    
def __mul__(self, other):
    return Mul(self, other)
    
def __div__(self, other):
    return Div(self, other)    
    
def __pow__(self, other):
    return Pow(self, other)  

def __unaryminus__(self):
    return UnaryMinus(self)

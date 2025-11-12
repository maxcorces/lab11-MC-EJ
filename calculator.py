# https://github.com/maxcorces/lab11-MC-EJ
# Partner 1: Max Corces
# Partner 2: Elijah Joseph

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):

    if a < 0:
        raise ValueError("square_root() domain error: a must be non-negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a,b)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero: denominator 'a' is 0")
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("invalid base: 'a' must be > 0 and != 1")
    if b <= 0:
        raise ValueError("invalid argument: 'b' must be > 0")
    return math.log(b, a)

def exp(a, b):
    return a ** b





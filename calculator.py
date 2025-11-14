# https://github.com/maxcorces/lab11-MC-EJ
# Partner 1: Max Corces
# Partner 2: Elijah Joseph

import math

def square_root(a):
    if a < 0:
        raise ValueError("Square Root Of Negative Number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division By Zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Math Domain Error")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


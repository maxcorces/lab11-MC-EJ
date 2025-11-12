# https://github.com/maxcorces/lab11-MC-EJ
# Partner 1: Max Corces
# Partner 2: Elijah Joseph

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division By Zero")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Math Domain Error")
    return math.log(b, a)

def exp(a, b):
    return a ** b


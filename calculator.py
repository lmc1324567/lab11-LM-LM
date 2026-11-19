# https://github.com/lmc1324567/lab11-LM-LM
# Partner 1: Leon Merchel Czubek
# Partner 2: Leon Merchel Czubek (worked alone)
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base")
    if b <= 0:
        raise ValueError("Invalid argument")
    return math.log(b, a)


def exp(a, b):
    return a ** b

# def func1(x):
#     return str(x) + "n^3 + "
#
# def func2(x):
#     return str(x) + "n^2 + "
#
# def func3(x):
#     if x == 1:
#         return "n + "
#     return str(x) + "n + "
#
# def poly(list, func1, func2, func3):
#     first = func1(list[0])
#     second = func2(list[1])
#     third = func3(list[2])
#     fourth = str(list[3])
#
#     return first + second + third + fourth
#
# print(poly([3,2,1,4], func1, func2,func3))

import math

def clear(x,y):
    return 0

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def exponent(x,y):
    return x ** y

def remainder(x,y):
    return x % y

def sqrt(x,y):
    return math.sqrt(x)

def calculator(x, y, func):
    return func(x,y)

print(calculator(2, 3, exponent))


"""
Function Review
You can treat functions as objects and arguments
Make a function and use it as an argument (a, b, func)
In the large function write return func(a,b)
"""
def add(a,b):
    return a + b

def calculate(a,b,func):
    return func(a,b)

print(calculate(5,10, add))

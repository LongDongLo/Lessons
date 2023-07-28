"""
Recursions
All recursions are inside functions
Parameters are when functions are defined
Arguments are when functions are called

"""

def factorial(n):
    print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))


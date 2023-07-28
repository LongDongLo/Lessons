# Local Variables Versus Global Variable
# Local Variable: Only exists within an environment like an if statement
# Global Variable: Always exists
"""
def test():
    return 7 # giving test() a value

def test1(x):
    a = 1
    x = x + a
    return x

def test2(x, y, z):
    peee = x + y
    list = z
    print(peee)
    print(list)

list = [1,2,3,4,5,6,9]

test2(45, 24, list)
"""

input1 = float(input("Enter a number: "))
input2 = input("Enter an operation (+, -, x, ÷)")
input3 = float(input("Input another number: "))

def add(x, y):
    sum = x + y
    print(sum)

def sub(x, y):
    dif = x - y
    print(dif)

def mul(x, y):
    prod = x * y
    print(prod)

def div(x, y):
    quo = x / y
    print(quo)

if input2 == "+":
    add(input1, input3)
elif input2 == "-":
    sub(input1, input3)
elif input2 == "x":
    mul(input1, input3)
elif input2 == "÷":
    div(input1, input3)
else:
    print("Sorry that is not an option")

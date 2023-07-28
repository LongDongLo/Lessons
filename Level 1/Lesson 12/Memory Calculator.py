input1 = float(input("Enter a number: "))
input2 = input("Enter an operation (+, -, x, ÷): ")
input3 = float(input("Input another number: "))

again = 0

def add(x, y):
    sum = x + y
    print(sum)
    return sum

def sub(x, y):
    dif = x - y
    print(dif)
    return dif

def mul(x, y):
    prod = x * y
    print(prod)
    return prod

def div(x, y):
    quo = x / y
    print(quo)
    return quo

if input2 == "+":
    answer = add(input1, input3)
elif input2 == "-":
    answer = sub(input1, input3)
elif input2 == "x":
    answer = mul(input1, input3)
elif input2 == "÷":
    answer = div(input1, input3)
else:
    print("Sorry that is not an option")

    while again == 0:
        input2 = int(input("Enter an operation (+, -, x, ÷): "))
        input3 = float(input("Input another number: "))

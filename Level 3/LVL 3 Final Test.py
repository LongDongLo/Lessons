import random
import math

def randomDimensions(V):
    min = V
    for i in range(10000):
        x = random.randint(1, math.ceil(math.sqrt(V)))
        y = V / int(x) ** 2
        A = x ** 2 + 4*x*y
        if A < min:
            min = A
    return min

print("The minimum area of cardboard needed is", randomDimensions(1000), "cm^2" )

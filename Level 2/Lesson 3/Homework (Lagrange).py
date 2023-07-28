import math

def num_squares(x):
    dict = {}
    for i in range(math.ceil(math.sqrt(x))):
        dict[i] = (i+1)**2
        print(dict)
    if x in dict.values():
        return 1
    for i in dict:
        checker = dict[i]
        if x - checker in dict.values():
            return 2
    while x % 4 == 0:
        x = x / 4
    if x % 8 == 7:
        return 4
    else:
        return 3

print(num_squares(7))

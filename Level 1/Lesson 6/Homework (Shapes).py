"""
print out

O O O O O
X X X X X
O O O O O
X X X X X
O O O O O

and

*
* *
* * *
* * * *
* * * * *

using for loops
"""

x = 0

for i in range(5):
    if i > 0:
        print()
    if i % 2 == 0:
        for i in range(5):
            print("O ", end="")
    elif i % 2 == 1:
        for i in range(5):
            print("X ", end="")

for i in range(2):
    print()

for i in range(5):
    for i in range(1+x):
        print("* ",end="")
    print()
    x = x + 1

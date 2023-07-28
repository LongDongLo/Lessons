"""
Create 2 randomly generated lists of 3 integers from 1-10 and check if they have the same integers (excluding order).
"""

from random import randint

switch = 0

while switch == 0:
    list1 = []
    list2 = []

    for i in range(3):
        list1.append(randint(1, 3))

    for i in range(3):
        list2.append(randint(1, 3))

    print(list1, list2)

    if list1 == list2:
        print("THE LISTS HAVE THE EXACT SAME VALUES!!!!!")
        print("THE LISTS HAVE THE EXACT SAME VALUES!!!!!")
        print("THE LISTS HAVE THE EXACT SAME VALUES!!!!!")
    elif sorted(list1) == sorted(list2):
        print("THE LISTS HAVE THE SAME VALUES!!!")
    else:
        print("The lists do not have the same values")

    print()

    choice = input("Do you wanna generate more lists? (y or n): ")

    if choice == "n":
        switch = 1

    print()

"""
Name: Will Li Luo
Date: March 1, 2022
Description: Variable Assignment
"""

# Variable Definition
protagonist = "Jim"
road = "path"
choice2 = "small cave"
amount = 2
colour = "yellow"
pots = 3
fun = "mush"
gi = "rooms"

# The Story of Jim
print("     Once upon a time, there was a simple lad named", protagonist, ".")
print(protagonist, "wanted to go on an adventure, so he set of into the mountains with determination.")
print("So, he began his journey, and soon ran into a crossroad with", amount, "pathways.")
print("On the left, there was a narrow path riddled with", colour, fun + gi, "and on the right, there was a", choice2, "that seemed to lead somewhere.")
choice = input(str(protagonist) + " had to make a choice. Would he take the left " + str(road) + " or the right " + str(road) + "? (l or r): ")

if choice == "r":
    print("")
    print("     Eventually", protagonist, "decided to go into the", choice2, ".")
    print("After a few sharp turns, he began to see a clear path leading to an opening in the cave.")
elif choice == "l":
    print("")
    print("     In the end,", protagonist, "decided to take the", colour, fun + gi, "- ridden", road, ".")
print("The", road, "continued on and led into a wonderful clearing of flat moss and", colour, fun + gi, ".")
print("It was getting dark, and", protagonist, "had to make some food and set up camp.")
print("First he set up his personal tent, then went to pick some", colour, fun + gi, "to make mushroom stew.")

amount = int(input("How many " + fun + gi + " should " + str(protagonist) + " pick? "))
print("")
print(protagonist, "ended up picking", amount, "mushrooms.")
print("However, he only had", pots, "cooking pots that together fit two thirds of the", fun + gi, ".")
print(protagonist, "had", (amount/3), fun + gi, "left.")
capacity = amount / 3
if capacity >= 7:
    capacity = " satisfied"
elif capacity < 1:
    capacity = "n empty"
elif capacity < 7:
    capacity = " not so full"
print("So,", protagonist, "quickly went to sleep with a" + str(capacity), "stomach, preparing for the day to come.")
print("")
print("The end")



"""
Make two lists of Strings, which one of them has the magicians’ names and the other has their own
corresponding spells they can cast. Create a function to prints all the magician casting their own
spells in the format: Adam casts Fireball

Functions are required

spell[1] = wizard[1]

inputs for the lists is allowed

Make a list of guys and randomly genereate what spells they can cast, or maybe they're a muggle
"""
import random

wiz = []

def fire(x):
    print(x + "casts fireball")

def ice(x):
    print(x + "casts freeze spell")

def thunder(x):
    print(x + "casts lightning strike")

def kill(x):
    print(x + "casts instakill")

def list():
    add = input("What would you like to name this wizard? ")
    wiz.append(add)

number = int(input("How many wizards would you like to create? "))

for i in range(number):
    list()

print("And now to reveal each wizard's hidden special move!")

print(list[random.randint(0, number)])
print(list[random.randint(0, number)])
print(list[random.randint(0, number)])

fire(list[random.randint(0, number)])
ice(list[random.randint(0, number)])
thunder(list[random.randint(0, number)])
kill(list[random.randint(0, number)])





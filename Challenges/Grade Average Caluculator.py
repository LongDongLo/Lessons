# Grade Average Calculator

counter = 0
choice = 0
sum = 0

print("Hello there! Would you like to know your overall average grade? ")
print("Simply input number grades from 0-100, and I will do the rest!")
print("")
while choice != "no":
    counter = counter + 1
    grade = int(input("Enter grade #" + str(counter) + ": "))
    print("")
    choice = input("Would you like to input another grade? (yes or no): ")
    sum = sum + grade

print("Your average grade is", sum / counter)
finalgrade = sum / counter
print("")
if finalgrade > 100:
    print("Whoa! Is that even a grade?")
elif finalgrade >= 95:
    print("Wow! You're really smart!")
elif finalgrade >= 90:
    print("Not too shabby!")
elif finalgrade >= 84:
    print("You can do it! Keep on going :D")
elif finalgrade >= 75:
    print("Keep working hard :)")
elif finalgrade >= 67:
    print("Almost there! Work to do your best.")
elif finalgrade >= 50:
    print("Just made it past!")
elif finalgrade < 50:
    print("You failed :(  maybe next time!")

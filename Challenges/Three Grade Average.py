# Grade Average Calculator

print("Hello there! Would you like to know your overall average grade? ")
print("Simply input up to three number grades from 0-100, and I will do the rest!")
print("")
grade1 = int(input("Grade #1: "))
grade2 = int(input("Grade #2: "))
choice = input("Would you like to input another grade? (yes or no): ")

if choice == "yes":
    grade3 = int(input("Grade #3: "))
    print("Your average grade is", (grade1 + grade2 + grade3)/3)
    finalgrade = (grade1 + grade2 + grade3)/3

if choice == "no":
    print("Your average grade is", (grade1 + grade2)/2)
    finalgrade = (grade1 + grade2)/2

print("")
if finalgrade > 94:
    print("Wow! You're really smart!")
elif finalgrade <= 94:
    print("You can do it! Keep on going :D")


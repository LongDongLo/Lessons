# In your car class, add a function 'tune'.
# This function will ask the user how much they want the topSpeed to increase by.
# Then read user input and increase the topSpeed.
# Make an appropriate adjustment to the value of the car, how much increase is your decision.
# Also, damaged cars cannot be tuned.

class Car:
    def __init__(self, topSpeed, damaged, value):
        self.topSpeed = topSpeed
        self.damaged = damaged
        self.value = value
    def tune(self, increase):
        if damaged == "False" or damaged == "false" or damaged == "f":
            for i in range(increase):
                self.value = self.value + 8
            return "Your car is now worth $" + str(self.value)
        else:
            return "Sorry, we cannot tune damaged cars"

topSpeed = input("What is the top speed of your car? ")
damaged = (input("Your car is damaged (True/False) "))
# if damaged == "False" or damaged == "false" or damaged == "f":
value = int(input("What is the value of your car? "))
car = Car(topSpeed, damaged, value)
increase = int(input("How much would you like to increase your cars top speed? "))
print(car.tune(increase))


# Add functions and more food options
# Make it more simplified
# e.g. make functions that give change and update inventory

stock1 = 20
stock2 = 15
stock3 = 12
price1 = 6.5
price2 = 6.75
price3 = 7.25
switch = 0
number1 = 0
number2 = 0
number3 = 0

def num():
    x = int(input("How many would you like? "))
    print()
    return x

def out():
    print("Oh no, we don't have any of those left!")

def less():
    x = int(input("Sorry, it looks like we have " + str(stock1) + " of those left. How many would you like to purchase instead? "))
    return x

def price(a,b,c,d,e,f,g):
    g = a * d + b * e + c * f
    print("Great choice! That will be $" + str(g))
    return g

def change(a,b):
    x = a - b
    y = float(input("Oops! It looks like you still need to pay $" + str(x) + ". How much more will you pay? "))
    b = b + y
    return b

while stock1 + stock2 + stock3 > 0:
    print("HELLO THERE! Welcome to Frank's Fantastic Food Truck!")
    print("1. Deep Fried Butter (x" + str(stock1) + " in stock), 2. Deep Fried Butter on a Stick (x" + str(stock2) + " in stock), 3. Extra Deep Fried VEGAN Margarine Bites (x" + str(stock3) + " in stock).")
    while switch == 0:
        choice = int(input("What would you like to buy? "))
        print()
        if choice == 1:
            if stock1 <= 0:
                out()
            else:
                number1 = num()
                while number1 > stock1:
                    number1 = less()
            stock1 = stock1 - number1
        elif choice == 2:
            if stock2 <= 0:
                out()
            else:
                number2 = num()
                while number2 > stock2:
                    number2 = less()
            stock2 = stock2 - number2
        else:
            if stock3 <= 0:
                out()
            else:
                number3 = num()
                while number3 > stock3:
                    number3 = less()
            stock3 = stock3 - number3
        choice1 = input("Would you like to buy anything else? (yes or no): ")
        if choice1 == "no":
            choice = 0
            switch = 7

    if choice == 1:
        price = price(number1, number2, number3, price1, price2, price3, price)
    elif choice == 2:
        price = price(number1, number2, number3, price1, price2, price3, price)
    else:
        price = price(number1, number2, number3, price1, price2, price3, price)

    print()
    pay = float(input("How much will you be paying? "))

    while pay < price:
        pay = change(price, pay)
    change = pay - price
    if change < 0.01:
        change = 0.00
    switch = 0
    print()
    print("Your change comes to $" + str(change))
    print("Please come again!")
    print()
print("Sorry, we're closed!")

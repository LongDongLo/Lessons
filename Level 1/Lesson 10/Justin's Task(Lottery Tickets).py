import random
winning_ticket = []
youwon = 0
print("Hello there! You have entered the virtual lottery, where dreams are big and tickets are free!")
ticketnumber = int(input("How many tickets would you like the buy?: "))
for i in range(6):
    count = i + 1
    win = int(input("What should the #" + str(count) +" number (<100) of the winning lottery number be?: "))
    winning_ticket.append(win)
print(winning_ticket)
for i in range(ticketnumber):
    list = []
    for i in range(6):
        list.append(random.randint(1, 99))
    print(list)
    if list == winning_ticket:
        youwon = youwon + 1
if youwon > 0:
    print("YOU WON THE LOTTERY!!!")
elif youwon == 0:
    print("Sorry, no winners today")

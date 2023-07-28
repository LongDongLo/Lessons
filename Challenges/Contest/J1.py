S = input("Amount of small treats recieved: ")
M = input("Amount of medium treats recieved: ")
L = input("Amount of large treats recieved: ")
h = 1 * int(S) + 2 * int(M) + 3 * int(L)
if h > 9:
    print("Happy")
else:
    print("Sad")

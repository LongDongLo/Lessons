def ninetyNine(line1,line2,line3,line4,line5):
    for i in range(5):
        if i == 0:
            line = line1
            startingValue = line[0]
            playerHand = [line[1],line[2],line[3]]
            startingValue += playerHand.pop(max(playerHand))
            startingValue += line[0]
            

        # elif i == 1:
        # elif i == 2:
        # elif i == 3:
        # elif i == 4:


ninetyNine(
    (65, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"),
    (74, "A", 2, 9, "T", 9, 7, "A", 9, 8, "A"),
    (55, "A", "K", "Q", "J", "T", "A", "K", "Q", "J", "T"),
    (59, "A", "T", "K", "A", "Q", "A", "T", 7, 9, 4),
    (70, "T", "Q", 9, 9, "A", "Q", "J", "K", "Q", "T")
)

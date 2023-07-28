# Liar's Dice
"""
def mode(x):
    counter = 0
    num = x[0]
    for i in x:
        frequency = x.count(i)
        if(frequency > counter):
            num = i
            counter = frequency


    return num, frequency

def liarsDice(x):
    totalList = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            totalList.append(x[i][j])
    oneCount = totalList.count(1)
    while 1 in totalList:
        totalList.remove(1)
    answer = mode(totalList)[0]
    finalAnswer = [mode(totalList)[1] + oneCount, answer]

    return finalAnswer

print(liarsDice([[2, 2, 4, 5, 6], [3, 4, 4, 5, 6], [6, 4, 5, 1, 4]]))
"""

# Tic Tac Toe











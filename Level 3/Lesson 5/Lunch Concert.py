# Lunch Concert
global friendList
friendList = []
N = int(input())

for i in range(N):
    nLine = input()
    temp = []
    temp = nLine.split()
    temp2 = []
    for i in temp:
        temp2.append(int(i))
    friendList.append(temp2)

def walkingSum(c):
    sumTime = 0

    for i in range(N):
        distance = abs(abs(c - friendList[i][0]) - friendList[i][2])
        speed = friendList[i][1]
        time = speed*distance
        sumTime += time

    return sumTime

positionList = []

for i in range(len(friendList)):
    positionList.append(friendList[i][0])

megaList = []

for i in range(min(positionList),max(positionList)):
    megaList.append(walkingSum(i))

print(min(megaList))


# c = Distance along Field
# Order: [Friend Position, Speed (S/m), Hearing Range]

# Write a function that takes an integer argument, c.
# Then the function will return the sum of walking times
# of everyone to get within hearing range of position c.




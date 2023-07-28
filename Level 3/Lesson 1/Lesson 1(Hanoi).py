# Tower of Hanoi
import autopy
import time


def startingRings(ringNumber):
    towerA = []
    for i in range(ringNumber):
        towerA.append(ringNumber-i)
    return towerA


towerA = startingRings(3)  #  How many rings do you want?
towerB = []
towerC = []


def dragBlock(start, end):
    if start and end:
        if start[-1] < end[-1]:
            # moveMouse(start,end)
            end.append(start[-1])
            start.remove(start[-1])
            print("A:", towerA)
            print("B:", towerB)
            print("C:", towerC)
            print()
        else:
            # moveMouse(end,start)
            start.append(end.pop(-1))
            print("A:", towerA)
            print("B:", towerB)
            print("C:", towerC)
            print()
    elif start and not end:
        # moveMouse(start,end)
        end.append(start[-1])
        start.remove(start[-1])
        print("A:", towerA)
        print("B:", towerB)
        print("C:", towerC)
        print()
    elif not start and not end:
        print("The two lists are empty")

    elif not start:
        dragBlock(end, start)


# def recursive(n, source, dest, aux):
#     if n == 1:
#         print("move disk from", source, "to", dest)
#         return
#     recursive(n-1, source, aux, dest)
#     print("moveddisk from", source, "to", dest)
#     recursive(n-1, aux, dest, source)


def inputs(moves):
    for i in range(len(moves)):
        if moves[i][0] == 1:
            argument1 = towerA
        elif moves[i][0] == 2:
            argument1 = towerB
        elif moves[i][0] == 3:
            argument1 = towerC

        if moves[i][1] == 1:
            argument2 = towerA
        elif moves[i][1] == 2:
            argument2 = towerB
        elif moves[i][1] == 3:
            argument2 = towerC

        moveMouse(argument1, argument2)
        dragBlock(argument1, argument2)


def moveGenerator(tower):
    bigList = []
    if len(tower) % 2 == 1:
        for i in range(2**len(tower)):
            if i % 3 == 1:
                appendedList = [1,3]
            elif i % 3 == 2:
                appendedList = [1,2]
            elif i % 3 == 0:
                appendedList = [2,3]
            bigList.append(appendedList)
        return bigList

    elif len(tower) % 2 == 0:
        for i in range(2**len(tower)-1):
            if i % 3 == 1:
                appendedList = [1,3]
            elif i % 3 == 2:
                appendedList = [2,3]
            elif i % 3 == 0:
                appendedList = [1,2]
            bigList.append(appendedList)
        return bigList


def moveMouse(start,end):
    for i in range(2):
        if i == 0:
            condition = start
        elif i == 1:
            condition = end
        if condition == towerA:
            autopy.mouse.move(600,550)
            time.sleep(0.1)
            autopy.mouse.click()
            time.sleep(0.1)
        elif condition == towerB:
            autopy.mouse.move(800,550)
            time.sleep(0.1)
            autopy.mouse.click()
            time.sleep(0.1)
        elif condition == towerC:
            autopy.mouse.move(1000,550)
            time.sleep(0.1)
            autopy.mouse.click()
            time.sleep(0.1)


time.sleep(3)
inputs(moveGenerator(towerA))

# Homework: get autoclicker to work on here


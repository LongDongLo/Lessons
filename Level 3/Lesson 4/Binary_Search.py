rangeLow = 0.1
rangeHigh = 6.5
recursionDepth = 0


def getHeight(base):
    return (45-base**2)/(4*base)


def getVolume(base, height):
    return base * base * height


def findMax(range0, range1):
    print("A")
    global recursionDepth
    recursionDepth += 1
    average = (range1 + range0)/2
    tempLeft = getVolume(average, getHeight(average)) - getVolume(range0, getHeight(range0))
    tempRight = getVolume(average, getHeight(average)) - getVolume(range1, getHeight(range1))

    if recursionDepth > 10:
        print(getVolume(average, getHeight(average)))
        return getVolume(average, getHeight(average))
    elif tempLeft > tempRight:
        ("tempLeft is greater than tempRight")
        findMax(average, range1)
    elif tempRight > tempLeft:
        findMax(range0, average)


findMax(rangeLow,rangeHigh)


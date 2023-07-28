"""
def missingNumFind(x):
    setS = set(range(1, max(x)+1))
    print(setS.difference(x).pop())

missingNumFind([1,4,2,4])

"""
def listOverlap(x,y):
    setA = []
    for i in range(len(x)):
        setAppendA = set(range(min(x[i]), max(x[i])+1))
        for j in range(len(y)):
            setAppendB = set(range(min(y[i+j]), max(y[i+j])+1))
            setA.append([min(setAppendA.intersection(setAppendB)), max(setAppendA.intersection(setAppendB))])
    print(setA)

listOverlap([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])


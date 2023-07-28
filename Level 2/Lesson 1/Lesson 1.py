"""
Tuples are like lists, but uneditable
Tuples are created with x = (), but technically don't need the (), just the ,
Tuple packing is creating tuples without parentheses
You can unpack by saying x, y , z = tuple(which equals 1, 2, 3)
This assigns the three cariables with those values
You can change a tuple into a list to edit it then change it back
You can use the command tuple.count(100) to find out how many of a certain item there is in a tuple
Tuple.index(100) gives you the first index of the chosned value
"""
"""
def helper(a):
    temp = 0
    tempTuple = ()
    for i in a:
        if max(i) >= temp:
            temp = max(i)
            tempTuple = i
    return tempTuple

def tupleFinder(a):
    finalList = []
    num = helper(a)
    while len(a) > 0:
        finalList.append(helper(a))
        a.remove(helper(a))
    print(finalList)
    return num

x = tupleFinder([(4,5,5,7),(1,3,7,4),(19,4,5,3),(1,2)])
print(x)
"""


def personal_profile(n):
    totalList = []
    for i in range(n):
        list = []
        for i in range(5):
            add = input()
            list.append(add)
        converter = tuple(list)
        totalList.append(converter)
    totalList.sort(key=lambda x:x[1])
    return totalList

print(personal_profile(2))

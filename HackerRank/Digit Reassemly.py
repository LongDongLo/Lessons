def digitR(inputList):
    finalList = []
    appendList = []
    for i in range(5):
        multiple = inputList[i*2+1]
        edit = str(inputList[i*2])
        for j in range(len(edit) - multiple + 1):
            listAppend = edit[j: j + multiple]
            appendList.append(int(listAppend))
        finalList.append(appendList)
        appendList = []
    for i in range(len(finalList)):
        print(sum(finalList[i]))

testCase = [1325678905, 2,
    54981230845791, 5,
    4837261529387456, 3,
    385018427388713440, 4,
    623387770165388734, 11
]

(digitR(testCase))

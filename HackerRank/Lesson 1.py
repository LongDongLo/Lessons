# Scrap Paper for Contest 2
def binarySlicing(num):
    num = num[:1] + num[2:]
    return num

num = bin(245)
print(num)
num = binarySlicing(num)
print(num)

tester = str(1000000)
print(list(tester))

tester = tester[:0] + tester[0+1:]
print(tester)

tester = 12

tester = bin(tester)
print(tester)

tester = "10101111"
deleteIndex = 1
tester = tester[: deleteIndex] + tester[deleteIndex + 1:]
print(tester)

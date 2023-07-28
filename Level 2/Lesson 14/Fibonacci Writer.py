import os

print(os.getcwd())

writingfile = open("fibonacci.txt", "w")
value1 = 0
value2 = 1
value3 = 0

writingfile.write(str(value1) + "\n")
writingfile.write(str(value2) + "\n")

for i in range(48):
    value3 = value1 + value2
    writingfile.write(str(value3) + "\n")
    value1 = value2
    value2 = value3

writingfile.close()



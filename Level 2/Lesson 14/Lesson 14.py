myfile = open("example1.txt", "r")  # r means reading file
print(myfile.readline())
print(myfile.readline())
myfile.close()  # remember to close

myfile = open("L14_exercise1.txt", "r")
print(int(myfile.readline())+int(myfile.readline())+int(myfile.readline()))
myfile.close()

writingfile = open("newfile.txt", "w")  # w means writing file
writingfile.write("I am tired" + "\n")  # \n starts new lines
writingfile.write("when will it end")
writingfile.close()

# Classes and Objects
class Students:
    mark = 100
    grade = 9
    favClass = "Gym"
    def __init__(self, mark, grade):
        self.mark = mark
        self.grade = grade
    def fail(self):
        self.mark = 40
    def canGraduate(self):
        if self.mark >= 60 and self.grade >= 12:
            print("This student can graduate")
        else:
            print("This student cannot graduate")

class Cars:
    def __init__(self, topSpeed, color, age, value, damaged):
        self.topSpeed = topSpeed
        self.color = color
        self.age = age
        self.value = value
        self.damaged = damaged

    def crash(self):
        self.damaged = True
        self.value -= (self.value/10)

lambo = Cars(300,"white",2,700000,False)
print(lambo.value)
print(lambo.damaged)
lambo.crash()
print(lambo.value)
print(lambo.damaged)

# winson = Students(99, 7) # (mark, grade)
# print(winson.mark)
# print(winson.grade)
#
# will = Students(grade = 10, mark = 98) # if unsure of argument order
# print(will.mark)
# print(will.grade)


# will = Students()
# print(will.mark)
# will.mark -= 10
# print(will.mark)
# will.fail()
# print(will.mark)
#
# justin = Students()
# justin.grade = 7
# print(justin.grade)
#
# harry = Students()
# harry.favClass = "none"
# print(harry.favClass)
#
# someGuy = Students()
# someGuy.mark = 61
# someGuy.grade = 13
# someGuy.canGraduate()




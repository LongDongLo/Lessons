"""
    1. Question 1:
Given a list containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the list.
Example 1:
Input: [3,0,1]
Output: 2
Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""
# 1
"""
switch = 0
switch2 = 0
added = 0
userlist = []
consecutivelist = []
comparison = 0
counter = 0

while switch == 0:
    listdigit = int(input("What number would you like to add to the list: "))
    userlist.append(listdigit)
    choice = input("Would you like to enter another digit? (y or n): ")
    if choice == "n":
        switch = 1

for i in range(max(userlist) + 1):
    consecutivelist.append(i)

userlist = sorted(userlist)

while switch2 == 0:
    if userlist[comparison] == consecutivelist[comparison]:
        comparison = comparison + 1
        counter = counter + 1
    else:
        switch2 = 1
print(userlist)
print(consecutivelist)
print("The missing number is", comparison)
"""
"""
    2. Question 2:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the
form [x1,y1,x2,y2,...,xn,yn].
Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
"""
# 2
"""
mainlist = []
xylist = []
count = 0

digitcount = int(input("How many numbers would you like in your list? "))
for i in range(digitcount):
    add = int(input("What number? "))
    mainlist.append(add)

n = int(input("What is the value of n? "))

xlist = mainlist[:n]
ylist = mainlist[n:len(mainlist)]

for i in range(len(xlist)):
    xylist.append(xlist[count])
    xylist.append(ylist[count])
    count = count + 1

print(xylist)
"""
"""
    3. Question 3:
Given two sorted integer lists nums1 and nums2, merge nums1 and nums2 into a single sorted list.
Example 1:
Input:
nums1 = [1,2,3]
nums2 = [2,5,6]
Output: [1,2,2,3,5,6]
Example 2:
Input:
nums1 = [1,8,9]
nums2 = [2,3,7]
Output: [1,2,3,7,8,9]
"""
"""
# 3
list1 = []
list2 = []

amount1 = int(input("How many numbers do you want in list #1? "))
for i in range(amount1):
    add = int(input("What number? "))
    list1.append(add)

amount2 = int(input("How many numbers do you want in list #2? "))
for i in range(amount2):
    add = int(input("What number? "))
    list2.append(add)
totalist = list1 + list2
print(sorted(totalist))
"""
"""
    4. Question 4:
Given a string s and a string t, check if s is subsequence of t. (Challenge: do NOT use the “in” operator)
Example 1:
Input: s = "abc", t = "habcgch"
Output: true
Example 2:
Input: s = "axc", t = "habcgch"
Output: false
"""
# 4
"""
start = 0
end = 0
counter = 0

userlist = input("What word would you like to check from? ")
subword = input("What subword do you want to check for? ")

list = userlist
for i in range(29):
    end = end + 1
    sublist = list[start:end]
    if sublist == subword:
        counter = counter + 1
    if end == len(list):
        start = start + 1
        end = start

if counter > 0:
    print("This subword is present in the word")
else:
    print("This subword in not present in the word")
"""
"""
    5. Question 5:
For your solution in Question 4, how would you modify it so it will find the last occurrence of the
subsequence efficiently and return the index of the subsequence? If the subsequence does not exist, return
-1.
Example 1:
Input: s = "abc", t = "habcgchabcd"
Output: 7
Example 2:
Input: s = "pet", t = "peter’s pet is called pettal"
Output: 22
"""
"""
# 5
start = 0
end = 0
counter = 0

userlist = input("What word would you like to check from? ")
subword = input("What subword do you want to check for? ")

list = userlist
for i in range(500):
    end = end + 1
    sublist = list[start:end]
    if sublist == subword:
        counter = counter + 1
        temp = start
    if end == len(list):
        start = start + 1
        end = start
    print(sublist)

if counter > 0:
    print("This subword is present in the word")
    print("It starts at", temp)
else:
    print("This subword in not present in the word")

"""

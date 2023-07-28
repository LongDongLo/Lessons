"""
There are multiple types of searches:
- Linear Search
- Binary Search

Notes: You can set else variables as the original variable value
Use the value i in for loops instead of count variable
"""


# Linear Search
def linear(l, x):
    index = -1
    for i in range(len(l)):
        if l[i] == x:
            index = i
            break
    return index

list1 = [1,5,2,4,3,6]


# Binary Search
def binary(l, x):
    l.sort()
    first = 0
    last = len(l) - 1
    while first <= last:
        mid = (first + last) // 2
        if l[mid] == x:
            return mid
        elif x < l[mid]:
            last = mid - 1
        elif x > l[mid]:
            first = mid + 1
    return -1

print(linear(list1, 7))

print(binary(list1, 7))




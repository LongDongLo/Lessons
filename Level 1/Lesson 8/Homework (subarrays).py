"""
Check if a subarray with 0 sum exists or not
Given an integer array, check how many subarrays have a sum of zero.
Array: [ 3, 4, -7, 3, 1, 3, 1. -4, 2, -2 ]
"""

start = 0
end = 1
counter = 0

list = [3, 4, -7, 3, 1, 3, 1, -4, 2, -2]
for i in range(45):
    end = end + 1
    sublist = list[start:end]
    if sum(sublist) == 0:
        counter = counter + 1
    if end == len(list):
        start = start + 1
        end = start + 1

print("The number of sublists with the sum of 0 is", counter)

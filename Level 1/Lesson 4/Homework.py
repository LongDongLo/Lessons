"""
Given an integer input, n, determine the Fibonacci number at the n-th position. The n can be any integer
number starting from 0 (including the 0).
The Fibonacci Number sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Example 1:
Input: n = 0
Output: 0
Explanation: The first number in the sequence is 0
Example 2:
Input: n = 1
Output: 1
Explanation: The second number in the sequence is 1
Example 3:
Input: n = 4
Output: 3
Explanation: The fifth number in the sequence is 3
"""

fibonacci = [0, 1]

num = int(input())
for i in range(num):
    fibonacci.append(fibonacci[i] + fibonacci[i + 1])

print(fibonacci[num])

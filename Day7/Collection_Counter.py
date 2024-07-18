"""https://www.hackerrank.com/challenges/collections-counter/problem"""

"""Collection Counter Problem
collections.Counter()
A counter is a container that stores elements as dictionary keys,
and their counts are stored as dictionary values.
"""
from collections import Counter
x = int(input()) #No of shoes
y = Counter(map(int, input().split()))
z = int(input()) # No of customers

total = 0
for i in range(z):
    size, rate = map(int, input().split())
    if z[size]:
        z[size] -= 1
        total += rate
print(total)
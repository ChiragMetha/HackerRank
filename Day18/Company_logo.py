"""https://www.hackerrank.com/challenges/most-commons/problem"""

"""Company logo"""
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    count = {}
    for val in s:
        if count.get(val):
            count[val] += 1
        else:
            count[val] = 1
            
    items = count.items()
    items = sorted(items, key=lambda x: (x[1], -ord(x[0])), reverse=True)
    for i in range(3):
        print(items[i][0], items[i][1])
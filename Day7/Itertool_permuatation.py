"""https://www.hackerrank.com/challenges/itertools-permutations/problem"""

"""Itertool Permutation
You are given a string S.
Your task is to print all possible permutations of size K of the string in lexicographic sorted order."""

from itertools import permutations
str1 , int1 = input().split()
for i in sorted(permutations(str1, int(int1))):
    print(''.join(i))
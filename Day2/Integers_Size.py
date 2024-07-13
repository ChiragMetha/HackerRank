"""https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem"""

"""Integers come in All sizes
Integers in Python can be as big as the bytes in your machine's memory.
There is no limit in size as there is:2**31-1(c++ int) or 2**63-1(C++ long long int).
As we know, the result of a**b grows really fast with increasing b.
Let's do some calculations on very large integers.

Task = Read four numbers a,b,c,d and print the result of a**b + c**d."""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a**b)+(c**d))

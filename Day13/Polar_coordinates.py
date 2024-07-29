"""https://www.hackerrank.com/challenges/polar-coordinates/problem"""

"""Polar coordinates
Task
You are given a complex z. Your task is to convert it to polar coordinates."""
import cmath
n = input()
print(abs(complex(n)))
print(cmath.phase(complex(n)))
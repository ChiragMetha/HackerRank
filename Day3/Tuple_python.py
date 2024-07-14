"""https://www.hackerrank.com/challenges/python-tuples/problem"""

"""Tuple Python
Given an integer n, and n space-separated integers as input,
create a tuple t, of those n integers. Then compute and print the result of hash(t)."""

if __name__ == '__main__':
    n = int(input())
    Tuple1 = map(int, input().split())
    t = tuple(Tuple1)
    print(hash(t))
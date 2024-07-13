"""https://www.hackerrank.com/challenges/python-quest-1/problem"""

"""Triangle quest
You are given a positive integer N. Print a numerical triangle of height N-1,
like the one below:
1
22
333
4444
55555
......

sample input = 5"""

for i in range(1,int(input())):
    print( int((i*(pow(10, i) - 1)) / 9 ))

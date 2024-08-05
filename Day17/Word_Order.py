"""https://www.hackerrank.com/challenges/word-order/problem"""

"""Word Order
There are 3 distinct words. Here,
"bcdef" appears twice in the input at the first and last positions.
The other words appear once each. The order of the first appearances are "bcdef",
"abcdefg" and "bcde" which corresponds to the output.

"""
from collections import Counter
n = int(input())
l1 = [input().strip() for _ in range(n)]
res = Counter(l1)
print(len(res))
print(*res.values())
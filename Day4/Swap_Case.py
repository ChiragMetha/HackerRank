"""https://www.hackerrank.com/challenges/swap-case/problem"""

"""Swap Case problem
Complete the swap_case function in the editor below.
swap_case has the following parameters:
string s: the string to modify

sample input = HackerRank.com presents "Pythonist 2"."""
def swap_case(s):
    string = ""
    for i in s:
        if i.isupper() == True:
            string += (i.lower())
        else:
            string += (i.upper())
    return string
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
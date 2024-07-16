"""https://www.hackerrank.com/challenges/find-a-string/problem"""

"""Find a string 
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left."""

def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startwith(sub_string):
            total += 1
    return total
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
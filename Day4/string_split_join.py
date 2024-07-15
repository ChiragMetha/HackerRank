"""https://www.hackerrank.com/challenges/python-string-split-and-join/problem"""

"""String split and join
a = "this is a string"
a = a.split(" ") # a is converted to a list of strings.
print(a)
['this', 'is', 'a', 'string']

return = a = "-".join(a)
print(a)
this-is-a-string 


"""
def split_and_join(line):
    a = line.split(" ")
    b = "-".join(a)
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
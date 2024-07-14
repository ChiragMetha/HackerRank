"""https://www.hackerrank.com/challenges/python-lists/problem"""

"""Python-list

sample input = Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print"""

if __name__ == '__main__':
    N = int(input())
    List=[]
    for i in range(N):

        command=input().split()
        if command[0] == "insert":
            List.insert(int(command[1]),int(command[2]))
        elif command[0] == "append":
            List.append(int(command[1]))
        elif command[0] == "pop":
            List.pop()
        elif command[0] == "print":
            print(List)
        elif command[0] == "remove":
            List.remove(int(command[1]))
        elif command[0] == "sort":
            List.sort()
        else:
            List.reverse()
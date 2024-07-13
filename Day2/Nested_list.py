"""https://www.hackerrank.com/challenges/nested-list/problem"""

"""Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students,
order their names alphabetically and print each one on a new line.

The first line contains an integer,N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

sample input = 5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""

if __name__ == '__main__':
    alist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))
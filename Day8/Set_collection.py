"""https://www.hackerrank.com/challenges/py-introduction-to-sets/problem"""

"""set of collection
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
"""

def average(array):
    my_set = set(array)
    avg = sum(my_set)/len(my_set)   
    return (avg)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
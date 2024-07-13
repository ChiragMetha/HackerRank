"""https://www.hackerrank.com/challenges/python-power-mod-power/problem"""

"""Power-Mod Power
So far, we have only heard of Python's powers. Now, we will witness them!
Powers or exponents in Python can be calculated using the built-in power function. Call the power function a**b as shown below:
pow(a,b) 

sample input = 3,4,5"""

if __name__ == '__main__':
    a=int(input())
    b=int(input())
    m=int(input())
print(pow(a,b))
print(pow(a,b,m))

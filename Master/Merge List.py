from math import factorial
t= int(input())
for i in range(t):
    a = [int(x) for x in input().strip().split(' ')]
    n=a[0]
    m=a[1]
    print(factorial(n+m)//factorial(n)//factorial(m)%(10**9+7))
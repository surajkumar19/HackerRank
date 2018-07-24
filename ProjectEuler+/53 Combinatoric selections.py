from math import factorial


def ncr(n, r):
    return l[n] / (l[r] * l[n-r])


i = 0
a, b = map(int, input().split())
l=[None]*(a+1)
l[0]= 1
l[1]=1

for x in range(2, len(l)):
    l[x] = l[x-1]* x

for x in range(1, a + 1):
    for y in range(0, x):
        if ncr(x, y) > b:
            i = i + 1

print(i)

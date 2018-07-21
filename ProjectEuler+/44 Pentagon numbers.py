import math

def pen_num(value):
    return value*(3*value-1)//2


def rev_val(val):
    x = math.sqrt(1+24*val)
    return ((x+1)/6)%1==0

x = [int(x) for x in input().split()]

ans = []

for i in range(x[1]+1, x[0]):
    a = pen_num(i)
    b = pen_num(i - x[1])

    diff = a-b
    addi = a+b


    if rev_val(diff) or rev_val(addi):
        ans.append(a)


for p in ans:
    print(p)


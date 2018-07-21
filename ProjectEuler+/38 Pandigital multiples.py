def is_panDigital(num, pan):
    num = str(num)
    num = list(num)
    num.sort()
    for i in range(pan):
        if str(i+1) != num[i]:
            return False
    return True

l = [int(x) for x in input().split()]
ans = []
for x in range(2,l[0]+1):
    s=""
    i = 1
    while len(s) < l[1]:
        s += str(x*i)
        i += 1
    if len(s) == l[1]:
        if is_panDigital(s,l[1]):
            ans.append(x)

for x in ans:
    print(x)
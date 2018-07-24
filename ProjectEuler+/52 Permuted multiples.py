import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)


def check(num, k):
    l1 = list(str(num))
    d = {}
    for x in l1:
        if x in d:
            return False
        else:
            d[x] = 1
    for i in range(2, k + 1):
        l2 = list(str(num*i))
        if len(l1) == len(l2) and compare(l1, l2):
            pass
        else:
            return False
    return True


# print(check(125874, 2))

a = [int(x) for x in input().split()]

for i in range(125873,a[0] + 1):
    if check(i, a[1]):
        # print("hai")
        for k in range(1, a[1] + 1):
            print(i * k, end=" ")
        print()

n = int(input())
arr = map(int, input().split())
d={}
for i in arr:
    if i in d:
        pass
    else:
        d[i]=1
v=list(d.keys())
v.sort()
print(v[len(v)-2])

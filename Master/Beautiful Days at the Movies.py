def rev(n):
    s=str(n)
    s=s[::-1]
    return int(s)
t=[int(x) for x in input().split()]
count=0
for i in range(t[0],t[1]+1):
    z=rev(i)
    if (i-z)%t[2]==0:
        count+=1
print(count)
    
    
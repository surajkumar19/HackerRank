
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a.sort()
# print(a)
l=[]
k=[]

# print(l)
for j in range(len(a)):
	l=[]
	l.append(a[j])
	for i in range(j+1,len(a)):
		if abs(a[j]-a[i])<=1:
			l.append(a[i])
	k.append(len(l))
print(max(k))



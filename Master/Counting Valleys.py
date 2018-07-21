n=int(input())
s=input()
i=0
s1=0
c=0
k=[]
t=''
while i <n:
	if s[i]=="U":
		p=1
	else:
		p=-1
	s1=s1+p
	k.append(s1)
	i=i+1
#print(k)
for i in range(len(k)-1):
	if k[i]<0:
		if k[i+1]>=0:
			c=c+1

print(c)

n=int(input())
s=input()
sum=0
a=[]
x=0
#s[0]
#print(s)
i=0

while i<len(s):
	if i==len(s):
			break
	z=ord(s[i])
	while z!=32:
		sum=(sum*10)+int(s[i])
		i=i+1
		if i==len(s):
			break
		z=ord(s[i])
	i+=1	
	a.insert(x,sum)
	x=x+1
	sum=0	
for i in a:	
 	sum=sum+i
#print(sum)
mean = sum/len(a)

print (mean)

a.sort()
#for i in a:	
 	#print(i)

if len(a)%2==0:
	#print("even",a[(len(a)-1)//2])
	mid=float((a[(len(a)-1)//2]+a[((len(a)-1)//2)+1])/2)
else:
	#print("odd")
	#print(a[(len(a)-1)//2])
	#print(a[((len(a)-1)//2)+1])
	mid=float(a[(len(a))//2])
median=mid
print(median)
count=1
c=0
i=0
while i< len(a):	
	if (i+1)==len(a):
			break
	#print (a[i],a[i+1])
	while a[i]==a[i+1]:
		count=count+1
		#print(a[i],a[i+1],count,i,i+1)
		i+=1
		#print(i)
		if (i+1)==len(a):
			break
	i=i+1
	#print(count)
	if c<=count:
		c=count
	count=1
#print(c)
i=0
while i< len(a):	
	if (i+1)==len(a):
			break
	#print (a[i],a[i+1])
	while a[i]==a[i+1]:
		count=count+1
		#print(a[i],a[i+1],count,i,i+1)
		i+=1
		#print(i)
		if (i+1)==len(a):
			break
	i=i+1
	#print(count)
	if count==c:
		print(a[i-1])
		break
	count=1

    
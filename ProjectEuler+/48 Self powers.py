n= int(input())
m=10**10
sum1=0
sum2=0
for i in range(1,n+1):
	sum1=(sum1%m+pow(i,i,m)%m)%m
	# print(sum1)
	
print((int)(sum1)%m)

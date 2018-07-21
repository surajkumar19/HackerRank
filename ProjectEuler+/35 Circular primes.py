
def primes(n):
	prime_number=[]
	if len(str(n))<6:
		n=n*10
	else:
		pass

	sieve=[True]*(n)
	
	for p in range(2,n):


		if sieve[p]:
			prime_number.append(p)
			for i in range(p*p,n,p):
				sieve[i]=False
	# print("abc")
	return prime_number



def prime(n):
	i=1
	j=0
	while i<=(n**(1/2)):
		if n%i==0:
			j+=1
		i+=1	
	if j==1:
		return True
	else: 
		return False

def rotate(n):
	s=len(str(n))
	#print (s)
	x=10**(s-1)
	k=(n//x)+((n%x)*10)
	#print(k)
	return k



z=int(input())
sum1=0
primemun=primes(z)[::]
for n in primemun:
	if n>=z:
		break
	#print(n)
	t=n
	flag=1
	shift=0
	if (n<10 or( '0' not in list(str(n)) and '2' not in list(str(n)) and '4' not in list(str(n)) and '6' not in list(str(n)) and '8' not in list(str(n)) and '5' not in list(str(n)))):
		n=int(str(n)[1:]+str(n)[:1])
		while (n!=t):
			
			if n not in primemun:
				flag=0
			n=int(str(n)[1:]+str(n)[:1])
		if flag==1:
			#print(t)
			sum1+=t



print(sum1)

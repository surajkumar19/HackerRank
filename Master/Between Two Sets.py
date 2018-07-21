import sys

def lcm(x,y):
	i=1
	while True:
		if (x*i)%y==0:
			return (x*i)
		else:
			i=i+1
	
def lcmset(q):
	lcm1=1
	for i in range (len(q)):
		lcm1=lcm(q[i],lcm1)
	return lcm1
def gcd(x,y):
	while y!=0:
		if x>y:
			x=x-y
		else:
			y=y-x
	return x

def gcdset(q):
	gcd1=gcd(q[0],q[1])
	for i in range(1,len(q)):
		gcd1=gcd(q[i],gcd1)
	return gcd1

# q=[16,32,96]
# print(gcdset(q))
# a=[2,3,4,5,6,7]
# print(lcmset(a))



def getTotalX(a, b):
    # Complete this function
    if max(a)>min(b):
    	return 0
    if len(a)==0 or len(b)==0:
    	return 0
    if len(a)==1 and len(b)==1:
    	if b[0]%a[0]==0:
    		c=0
    		i=1
    		while (a[0]*i)<=b[0]:
    			if b[0]%(a[0]*i)==0:
    				c=c+1
    			i=i+1
    		return c
    	else:
    		return 0
    if len(a)==1:
    	al=a[0]
    else:
    	al=lcmset(a)
    c2=0
    j=1
    c3=0
    
    while (al*j)<=min(b):
        c2=0
        for i in b:
        	if i%(al*j)==0:
        		c2=c2+1
        if c2==len(b):
        	c3=c3+1
        j+=1
    return c3




if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
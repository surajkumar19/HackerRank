def d(s):
    p=list(s)
    if p[0] not in d1:
        d1[p[0]]=p[1]
    # return d1

n= int(input())
d1={}
for i in range(n):
    s=input()
    l=s.split(" ")
    d(l)
    # print (d1)
k=input()
while k!='':
	if k in d1:
		print(k+"="+d1[k])
	else:
		print("Not found")
	k=input()

    

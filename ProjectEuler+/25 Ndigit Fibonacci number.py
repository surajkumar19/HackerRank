d={1:1,2:1,3:2}
d1={1:1,2:7}
a0=[]
t=int(input())
for i in range(t):
    n=int(input())
    a0.append(n)
n1=max(a0)
k=3
j=4
while len(str(d[j-1]))!=n1:
    d[j]=d[j-1]+d[j-2]
    if len(str(d[j]))==k:
        d1[k]=j
        k+=1
    j+=1
#print(d)
#print(d1)

j=0
for i in a0:
    print(d1[i])
    

            
           
    
            
           
    
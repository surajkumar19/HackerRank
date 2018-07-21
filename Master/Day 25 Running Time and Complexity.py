n=int(input())
for i in range(n):
    k=int(input())
    c=0
    j=1
    while j<=((k**(1/2))):
        if k%j==0:
            c+=1
        j+=1
    if c>1 or k==1:
        print("Not prime")
    else:
        print("Prime")
    
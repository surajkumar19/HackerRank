def print_rangoli(n):
    # your code goes here
    #n=int(input("n:"))
    z=(n*2)
    s='abcdefghijklmnopqrstuvwxyz'
    t=n
    l=1
    for j in range(1,(z//2)+1):
        n=t
        for i in range (z-2):
            print('-',end='')
        for k in range (j):
            print(s[n-1],end='')
            n=n-1
            #if (n+1)!=(t-1):
            if t==1:
                pass
            else:
                print('-',end='')
        n=n+1
        for k in range (1,j):
            n=n+1
            print(s[n-1],end='')
            if (k<j-1):
                print('-',end='')


        for i in range (1,z-1-l):
            if j==1:
                l=0
            print('-',end='')
        print('')

        z=z-2
    z=t*2
    q=0
    p=t
    for j in range(1,(z//2)):
        n=t
        q=q+2
        for i in range (q):
            print('-',end='')
        for k in range (p-1):
            print(s[n-1],end='')
            n=n-1
            #if (n+1)!=(t-1):
            print('-',end='')
        n=n+1
        for k in range (2,p):
            n=n+1
            print(s[n-1],end='')

            print('-',end='')

        for i in range (q-1):
            print('-',end='')
        print('')
        p=p-1

print_rangoli(int(input()))
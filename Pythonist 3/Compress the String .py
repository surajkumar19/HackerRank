s=input()
count=0
if len(s)==1:
    t=(1,int(s[0]))
    print(t)
else:
    for i in range(len(s)-1):
        # print("i=",i)
        # if i!=(len(s)):
            # print(i)
        # print(s[i],s[i+1])
        if s[i]==s[i+1] and i<=(len(s)):
            count=count+1
            # print(count)
        else:
            # print(count+1,s[i])
            t=(count+1,int(s[i]))
            print(t,'',end='')
            # print(t)
            
            count=0
        if count!=0 and i== len(s)-2:
            t=(count+1,int(s[i+1]))
            print(t)
        elif count==0 and i==len(s)-2:
            t=(1,int(s[i+1]))
            print(t)
               
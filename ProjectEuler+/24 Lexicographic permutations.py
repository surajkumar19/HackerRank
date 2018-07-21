t = int(input())
for _ in range(t):
    s = "abcdefghijklm"
    n = int(input())-1
    l=[]
    count = 0
    i = 1
    while (count != 13):
        if ((n % i) != 0):
            l.append(n % i)

        else:
            l.append(0)
        n = n // i
        i += 1

        count += 1
    # print(ss)
    # //ss=ss[-13:]
    sss = ""
    l.reverse()
    #print(l)
    try:
        for i in l:
            sss+=s[i]
            ll=list(s)
            ll.remove(s[i])
            s=''.join(ll)
    except:
        pass
    print(sss)

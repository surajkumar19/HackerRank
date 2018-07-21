if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        t=[x for x in input().split()]
        if t[0]=='insert':
        	l.insert(int(t[1]),int(t[2]))
        elif t[0]=='print':
        	print(l)
        elif t[0]=='append':
        	l.append(int(t[1]))
        elif t[0]=='remove':
        	p=t[1]
        	#print(p)
        	l.remove(int(t[1]))
        elif t[0]=='sort':
        	l.sort()
        elif t[0]=='pop':
        	l.pop()
        elif t[0]=='reverse':
        	l.reverse()
       
       
    

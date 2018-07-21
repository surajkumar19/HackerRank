t=int(input())
for _ in range(t):
	l=[]
	
	for i in range(int(input())):
		l.append([int(x) for x in input().split()])
	# print(l)
	for i in range(len(l)-1,0,-1):
		l2=[]
		for j in range(len(l[i-1])):
			if l[i-1][j]+l[i][j]>l[i-1][j]+l[i][j+1]:
				l2.append(l[i-1][j]+l[i][j])
			else:
				l2.append(l[i-1][j]+l[i][j+1])
		l=l[:i-1]
		# l.remove(i-1)
		l.append(l2)
	print(l[0][0])


		
		
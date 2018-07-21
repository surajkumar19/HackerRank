l=[]

for _ in range(0,int(input()),1):
    name = input()
    score = float(input())
    l.append([name,score])
#print(l)
l2=[]
for i in l:
    if i[1] not in l2:
        l2.append(i[1])
l2.sort()
#print(l2)
l3=[]
for i in l:
    if i[1]==l2[1]:
        l3.append(i[0])
l3.sort()
#print(l3)
for i in l3:
	print(i)
n=input()
count=0
while((n.isdigit()) and (int(n)>100000) and (int(n)<999999)):
	for i in range(len(n)-2):
	    while n[i]==n[i+2]:
	        count+=1
	        break
	while count>1:
	    print(False)
	    break
	while count<=1:
	    print(True)
	    break

	break
while ((n.isdigit() ==False)or (int(n)<100000) or (int(n)>999999)):
	print(False)
	break

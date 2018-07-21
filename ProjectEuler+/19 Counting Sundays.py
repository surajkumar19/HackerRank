# def isleapyear(n):
#     if n%400==0:
#         return True
#     elif n%100!=0 and n%4==0:
#         return True
#     else:
#         return False

# months1=[31,28,31,30,31,30,31,31,30,31,30,31]
# months2=[31,29,31,30,31,30,31,31,30,31,30,31]

t=int(input())
for _ in range(t):
	count=0
	start=[int(x) for x in input().split()]
	start2=[int(x) for x in input().split()]

	y =start[0]
	month=start[1]
	while y<=start2[0]:
		q=1
		if start[2]==1:
			m1=month
		else:
			m1=month+1

		while y<start2[0]:
			for m in range(m1,13):

			    if m==1 or m==2:
			    	if m==1:
			    		m=13
			    	if m==2:
			    		m=14
			    	y-=1
			    # h=(q+(13*(m+1)//5)+k+(k//4)+(j//4)+(5*j))%7)
			    h=(q+((13*(m+1))//5)+y+(y//4)-(y//100)+(y//400))%7
			    if m==13 or m==14:
			    	if m==13:
			    		m=1
			    	if m==14:
			    		m=2
			    	y+=1
			    if h==1:

			    	count+=1
			m1=1
			y+=1

		if start[0]==start2[0]:
			for m in range(m1,start2[1]+1):

			    if m==1 or m==2:
			    	if m==1:
			    		m=13
			    	if m==2:
			    		m=14
			    	y-=1
			    h=(q+((13*(m+1))//5)+y+(y//4)-(y//100)+(y//400))%7
			    if m==13 or m==14:
			    	if m==13:
			    		m=1
			    	if m==14:
			    		m=2
			    	y+=1
			    if h==1:
			    	count+=1
		if start[0]!=start2[0] and y==start2[0]:
			for m in range(1,start2[1]+1):

			    if m==1 or m==2:
			    	if m==1:
			    		m=13
			    	if m==2:
			    		m=14
			    	y-=1

			    h=(q+((13*(m+1))//5)+y+(y//4)-(y//100)+(y//400))%7
			    if m==13 or m==14:
			    	if m==13:
			    		m=1
			    	if m==14:
			    		m=2
			    	y+=1
			    if h==1:

			    	count+=1
			y+=1
		y+=1
	print(count)


    
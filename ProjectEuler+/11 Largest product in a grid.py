l = []
for grid_i in range(20):
   grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
   l.append(grid_t)
n=20
m=0
for i in range(n):
	for j in range (n-3):
		x=(l[i][j])*(l[i][j+1])*(l[i][j+2])*(l[i][j+3])
		# print(l[i][j],l[i][j+1],l[i][j+2],l[i][j+3])
		if m<=x:
			m=x
	# print(' ')
p=[m]
m=0

for j in range(n):
	for i in range (n-3):
		x=(l[i][j])*(l[i+1][j])*(l[i+2][j])*(l[i+3][j])
		# print(l[i][j],(l[i+1][j]),(l[i+2][j]),(l[i+3][j]))
		if m<=x:
			m=x
	# print(' ')
p.append(m)
# print(p)
m=0

for i in range(n-3):
	for j in range(n-3):
		x=(l[i][j])*(l[i+1][j+1])*(l[i+2][j+2])*(l[i+3][j+3])
		# print((l[i][j]),(l[i+1][j+1]),(l[i+2][j+2]),(l[i+3][j+3]))
		if m<=x:
			m=x
	# print(' ')
p.append(m)
# print(max(p))
for i in range(n-3):
	for j in range(3,n):
		x=(l[i][j])*(l[i+1][j-1])*(l[i+2][j-2])*(l[i+3][j-3])
		# print((l[i][j]),(l[i+1][j-1]),(l[i+2][j-2]),(l[i+3][j-3]))
		if m<=x:
			m=x
	# print(' ')
p.append(m)
print(max(p))

 
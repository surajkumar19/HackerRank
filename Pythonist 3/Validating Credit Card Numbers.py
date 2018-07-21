

def string(s):
	p='0123456789-'
	q='0123465789'
	# print(s[0])

	if int(s[0]) not in [4,5,6]:
		# print('A')
		print ('Invalid')
		return
	else:
		for i in s:
			if i not in p:
				# print('B')
				print('Invalid')
				return

		if '-'in s:
			if len(s)!=19:
				# print('C')
				print ('Invalid')
				return 
			else:
				for i in range(4,15,5):
					if s[i]!='-':
						# print('D')
						print('Invalid')
						return
			i=0
			count=0
			s1=s[:4]+s[5:9]+s[10:14]+s[15:]
			while i<len(s1)-1:
				if s1[i]==s1[i+1]:
					count+=1
					# print(count)
					if count==3:
						# print('E')
						print('Invalid')
						return
					
				else:
					count=0
					

				
				i=i+1
			# print('Z')

			print('Valid')






		else:
			if len(s)!=16:
				# print('F')
				print('Invalid')
				return
			else:
				i=0
				count=0
				while i<len(s)-1:
					if s[i]==s[i+1]:
						count+=1
						if count==3:
							print('Invalid')
							return
					else:
						count=0
					
					i=i+1
				
				# print('Y')
				print('Valid')


n=int(input())
for i in range(n):
	p=input()
	string(p)
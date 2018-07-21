import sys
def bubble_sort(l):
	swap=True
	count=0
	while swap:
		swap=False

		for i in range(len(l)-1):
			if l[i]>l[i+1]:
				l[i],l[i+1]=l[i+1],l[i]
				count=count+1
				swap=True
	return l,count

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
l1,swaps=bubble_sort(a)
s1='Array is sorted in '+str(swaps)+' swaps.'
print(s1)
print('First Element:',l1[0])
print('Last Element:',l1[-1])

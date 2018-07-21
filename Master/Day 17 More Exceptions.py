import math
class Calculator:
	def power(self,n,p):
		# k=math.pow(n,p)
		# # print('i1')
		# self.power=int(k)
		if n<0 or p<0:
			raise Exception('n and p should be non-negative')
		return int(math.pow(n,p))

    
    
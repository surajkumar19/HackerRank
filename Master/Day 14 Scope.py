	# Add your code here
    def computeDifference(self):
        l=[]

        for i in self.__elements :
        	for j in self.__elements :
        		l.append(abs(i-j))
        #print(l)
        self.maximumDifference=max(l)
        
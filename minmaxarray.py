class MinMaxArray:
	def __init__(self):
		self.__min = 0  #private_check
		self.max = 0    #public_check
		
	def get_min(self):
		return self.__min
		
	def set_min(self, new_min):
		self.__min = new_min
		
	def checkMinMax(self,given_array):
		'''for element in given_array:
			#print(element)
			if element<self.get_min():			#using getter function to access a prvate variable
				self.set_min(element)			#using setter function to set a private variable
			if element>self.max:
				self.max = element'''
				
		'''for i in range(len(given_array)):		#another way
			if given_array[i]<self.get_min():
				self.set_min(given_array[i])
			if given_array[i]>self.max:
				self.max = given_array[i]'''
		
		
		if len(given_array)==1:						#gfg way		
			self.set_min(given_array[0])
			self.max = given_array[0]
			return
			
		if given_array[0]>given_array[1]:
			self.set_min(given_array[1])
			self.max = given_array[0]
		else:
			self.set_min(given_array[0])
			self.max = given_array[1]
			
		for i in range(2,len(given_array)):		
			if given_array[i]<self.get_min():
				self.set_min(given_array[i])
			if given_array[i]>self.max:
				self.max = given_array[i]	
			
					
	
	def printMinMax(self):	
		print("The min of the array is", self.get_min())
		print("The max of the array is",self.max) 	

#A = MinMaxArray()
#A.checkMinMax([4,5,9,8,45,1,2,57,63,25,21,36,41,-5,54,-7,0])
#A.printMinMax()

B = MinMaxArray()
B.checkMinMax([4])
B.printMinMax()


#minmaxArray([4,5,9,8,45,1,2,57,63,25,21,36,41,-5,54,-7,0])

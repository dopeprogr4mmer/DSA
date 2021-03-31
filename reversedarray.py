def reverseArray(given_array):
	print("The given array is",given_array)
	#reversed_array = []
	start = 0
	end = len(given_array)-1
	while(start<end):
		#print(start,end)
		given_array[start], given_array[end] = given_array[end], given_array[start]
		#print(given_array[start],given_array[end])
		start+=1
		end-=1
		#print(start,end)
	
	
	print("The reversed array is",given_array)

reverseArray([1,5,4,7,8,0,9,6])
def findCommon(array1,array2,array3):
	return_array = []
	for element in array1:
		if (element in array2 and element in array3 and element not in return_array):
			return_array.append(element)

	if len(return_array)==0:
		return -1
	return return_array


try:
	common = findCommon([1,5,10],[6,7,100],[3,4,15,130])
	print(common)
except:
	print("Invalid input. Pass numeric values only!")

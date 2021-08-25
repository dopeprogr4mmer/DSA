def countInversions(array):
	inversion_count = 0
	temp = sorted(array)
	#flag = False
	index = 0

	if array == temp:
		return inversion_count

	value = list(reversed(temp))
	
	if array == value:
		inversion_count = len(array)//2
		return inversion_count

	while(True):
		temp_index = array.index(temp[index])
		array[index], array[temp_index] = array[temp_index], array[index]
		inversion_count += 1
		if array == temp:
			#flag = True
			return inversion_count
		index+=1



try:
	count = countInversions([5,1,4,3,2])
	print(f'Inversion Count is {count}')
except:
	print('Invalid Input. Pass Numbers only!')


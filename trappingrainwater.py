def trapping_rainwater(arr,n):
<<<<<<< HEAD
<<<<<<< HEAD
	left_arr = [None]*n
	right_arr = [None]*n
	left_arr[0] = arr[0]
	right_arr[-1] = arr[-1]
	output_arr = [None]*n
	for i in range(1,n):
		left_arr[i] = max(arr[:i])
	for j in range(n-2,-1,-1):
		right_arr[j] = max(arr[j:])
	for k in range(n):
		#print(left_arr[k], right_arr[k])
		output_arr[k] = min(left_arr[k], right_arr[k])-arr[k]
	print(left_arr, right_arr, output_arr) 
	return sum(output_arr)

def alternate(arr, n):
	left_arr = [None]*n
	right_arr = [None]*n 
	output_arr = [None]*n
	for i in range(n):
		left_arr[i] = max(arr[:i+1])
		right_arr[i] = max(arr[i:])
		output_arr[i] = min(left_arr[i], right_arr[i])-arr[i]
	print(left_arr, right_arr, output_arr)
	return sum(output_arr)

arr = [8,8,2,4,5,5,1]
n = 7
total = trapping_rainwater(arr,n)
print(total)
zeta = alternate(arr, n)
print(zeta)
=======
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
	max_index = 0
	local_index = 0
	total = 0
	for x in range(local_index+1,n-1):
		if arr[x-1]>arr[x]:
			pass
			#print(arr[x])	
		else:
			if arr[x]>=arr[local_index]:
				local_index = x
			if arr[max_index]>=arr[local_index]:
				max_index=local_index
			temp = arr[x]
			temp_list = [temp-i for i in arr[local_index:x]]
			print(temp_list)
	return total


#total = trapping_rainwater([1,1,5,2,7,6,1,4,2,3],10)
#print(total)

<<<<<<< HEAD
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05

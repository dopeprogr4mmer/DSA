def trapping_rainwater(arr,n):
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


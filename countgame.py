def count_game(arr,n):
	arr = sorted(arr)
	i = 0
	num_list = []
	while(i<len(arr)-1):
		temp_count = 1
		for j in range(i,len(arr)-1):
			if arr[j+1]==arr[j]:
				temp_count = temp_count+1
			else:
				if j==len(arr)-2 and n==1:
					num_list.append(arr[j+1])
				if temp_count==n:
					num_list.append(arr[i])
				break
		i=j+1

	print(arr,num_list)




count_game([1,1,1,2,5,4,8,5,4,-1,2,1,1,4,2,2,3,5],1)
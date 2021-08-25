def lcs(arr):
	arr = sorted(arr)
	count = 1
	subsequence = []
	#print(arr)
	i = 0
	while(i<len(arr)-1):
		#print(i,len(arr))
		temp_count=1
		temp_sequence = [arr[i]]
		for j in range(i,len(arr)-1):
			#print(i,j)
			if(arr[j+1] == arr[j]+1):
				temp_count+=1
				temp_sequence.append(arr[j+1])
				if j == len(arr)-2:
					if temp_count>=count:
						if temp_count>count:
							count=temp_count
							subsequence.clear()
						subsequence.append(temp_sequence)
			else:
				if temp_count>=count:
					if temp_count>count:
						count=temp_count
						subsequence.clear()
					subsequence.append(temp_sequence)
				
				break
		i=j+1
		
	longest_common_subsequence = [seq for seq in subsequence if len(seq)==count]
	#print(subsequence,longest_common_subsequence)

	return longest_common_subsequence,count
		

longest_common_subsequence,count = lcs([59,9,60,5,6,7,8,56,57,58,0,-1,61,-3,-4,85,23,24,-9,-8,-2])
print(longest_common_subsequence,count)


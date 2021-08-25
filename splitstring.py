def split_string(string):
	substring_list = []
	max_length = 1
	longest_string = []
	#print(len(string))
	start = 0
	while(start<len(string)-1):
		temp_string = string[start]
		for j in range(start+1,len(string)):
			#print((i,j))
			temp_string+=string[j]
			if temp_string.count('0')==temp_string.count('1'):
				substring_list.append(temp_string)
				break
		start = j+1
	return substring_list,len(substring_list)



substring_list,count=split_string('0100110101')
print(substring_list,count)
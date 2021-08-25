def count_occurence(string1,string2):
	count = 0
	occurence_index_list = []
	#print(len(string1))
	if len(string1)<=len(string2):
		if string1==string2:
			return[0]
		return -1


	if len(string1)>len(string2):
		for i in range(len(string1)-3):
			for j in range(i+4,len(string1)+1):
				#print(string1[i],string1[j-1],i,j)
				if string1[i:j] == string2:
					occurence_index_list.append(i)
					count+=1
				break

	return occurence_index_list
try:
	index_list = count_occurence('AABadAABA','AABA')
	if index_list==-1:
		print('Pattern must be longer or equal to Test String')
	else:
		if len(index_list)==0:
			print('Pattern not found')
		else:
			for index in index_list:
				print(f'Pattern found at index: {index}')
except:
	print('Invalid input')
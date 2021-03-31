def longest_repeating_subsequence(string):
	subsequence_list = []
	lrs_list = []
	max_length = 0
	if len(string)>1:
		for i in range(len(string)):
			sequence = string[i] 
			for j in range(i,len(string)):
				if j == i:
					pass
				else:
					sequence += string[j]
				if sequence in subsequence_list:
					if len(sequence)>=max_length:
						if len(sequence)>max_length:
							max_length = len(sequence)
							lrs_list.clear()
						lrs_list.append(sequence)
				else:
					subsequence_list.append(sequence)
				#print(sequence)
	#print(subsequence_list,'\n',lrs_list)
	if len(lrs_list)>0:
		return lrs_list,len(lrs_list[0])
	return 0

longest_repeating_subsequence,length = longest_repeating_subsequence('jxyrnbvntfcc')
print(longest_repeating_subsequence,length)

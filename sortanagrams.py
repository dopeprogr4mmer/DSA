def sort_anagrams(arr):
	temp = []
	sorted_list = []
	single_list = []
	for word in arr:
		z = list(word)
		z.sort()
		if z not in temp:
			temp.append(z)
			sorted_list.append([word])
		else:
			sorted_list[temp.index(z)].append(word)
	for l in sorted_list:
		if len(l)==1:
			single_list.append(l[0])
	print(sorted_list, single_list)
	return sorted_list

sort_anagrams(['abc','bcd','tea','cat','cab','eat'])


def avg_swap(arr1, arr2):
	pass





arr1 = [1, 2, 3, 4]
arr2 = [7, 8, 9, 10]
avg_swap(arr1, arr2)
def count_duplicates(string):
	count_dict = {}
	for element in string:
		count = string.count(element)
		if all([count>1, element not in count_dict.keys()]):
			count_dict[element] = string.count(element)

	return count_dict

count = count_duplicates('geeksforgeeks')
for key, value in count.items():
	print(key,value)
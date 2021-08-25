def longest_prefix_suffix(string):
	length = len(string)
	pre = 1
	post = length-1
	l = [] 
	max_prefix_length = 0
	while(pre<length and post>0):
		prefix = string[0:pre]
		postfix = string[post:length]
		#print(prefix,postfix,'ji')
		if prefix == postfix:
			if len(prefix)>=max_prefix_length:
				if len(prefix)>max_prefix_length:
					max_prefix_length = len(prefix)
					l.clear()
				l.append(prefix)
		pre += 1
		post -= 1
	print(l)
	if len(l)>0:
		return len(l[0])
	return 0



longest_string = longest_prefix_suffix('aa')
print(longest_string)
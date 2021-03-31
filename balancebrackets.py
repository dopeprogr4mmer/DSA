def balance_brackets(string):
	count = 0
	string_length = len(string)
	start = 0
	end = string_length-1
	#print(string_length//2)
	if string_length%2 == 0:
		#print(string[:string_length//2].count('{'))
		#pass
		while(start<end):
			print(string[start],string[end])
			if string[start] == string[end]:
				count+=1
			start+=1
			end-=1
	return count



reversal_count = balance_brackets('}}}}}}{}{}}}{{}}}}{}}{{{}{}{}{}}{{{{}}}{}}')
print(reversal_count)
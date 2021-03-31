def count_and_say(string):
	output_string = ''
	count = 1
	#while(start<len(string)-2):
	for i in range(len(string)-1):
		#count = 0
		if string[i+1] == string[i]:
			count = count+1
			if i == len(string)-2:
				#print(str(count)+string[i])
				output_string = output_string + str(count) + string[i]
				#print(output_string,'j')
				count = 1
		else:
			#print(str(count)+string[i])
			output_string = output_string + str(count) + string[i]
			#print(output_string,'j')
			count = 1
	if string[-1]!=string[-2]:
		output_string = output_string + str(count) + string[-1]
	#print(output_string,'k')
	return output_string



count_and_say = count_and_say('01123331')
print(count_and_say)
#code
def check_palindrome(string):
    reversed_string = ''.join(reversed(string))
    if reversed_string == string:
        return True
    return False
    
def longest_palindrome(string):
    palindrome_list = []
    max_length = 0

    if len(string)>1:
    	#return string[0]
    	for i in range(len(string)-1):
    	    temp_string = string[i]
    	    for j in range(i+1,len(string)):
    	        temp_string+=string[j]
    	        #print(temp_string)
    	        if all([check_palindrome(temp_string), len(temp_string)>=max_length]):
    	        	if len(temp_string)>max_length:
    	        		max_length = len(temp_string)
    	        		palindrome_list.clear()
    	        	palindrome_list.append(temp_string)


    if len(palindrome_list)>0: 
    	return palindrome_list
    return(string[0])
    
try:    
	longest_palindrome = longest_palindrome('125245121')
	for palindrome in longest_palindrome:
		print(palindrome,end=' ')
except:
	print('Invalid Input')
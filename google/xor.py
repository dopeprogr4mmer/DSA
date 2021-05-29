def xor(arr, n):
	sums = 0
	for i in range(n):
		sums = (sums^arr[i])
		print(sums,sums & -sums)

		print(sums)
		sums = (sums&-sums)
		print (sums)


		sum1 = 0
		sum2 = 0

		for i in range(n):
			if (arr[i]&sums)>0:
				sum1 = sum1^arr[i]
				#print(sum1)
			else:
				sum2 = sum2^arr[i]
				#print(sum2)

	#rightmost set bit
	#print(4, sum1 & -sum1)
	
	print(sum1, sum2)
	#print(4^3)

xor([1,2,1,7,3,2],5)

# Python3 program for above approach

# This function sets the values of
# *x and *y to non-repeating elements
# in an array arr[] of size n
def UniqueNumbers2(arr, n):
  sums = 0
  for i in range(0, n):
	
	# Xor all the elements of the array
	# all the elements occuring twice will
	# cancel out each other remaining
	# two unnique numbers will be xored
    sums = (sums ^ arr[i])
	
    # Bitwise & the sum with it's 2's Complement
    # Bitwise & will give us the sum containing
    # only the rightmost set bit
    sums = (sums & -sums)

    # sum1 and sum2 will contains 2 unique
    # elements elements initialized with 0 box
    # number xored with 0 is number itself
    sum1 = 0
    sum2 = 0

    # Traversing the array again
    for i in range(0, len(arr)):
	
	    # Bitwise & the arr[i] with the sum
	    # Two possibilities either result == 0
	    # or result > 0
	    if (arr[i] & sums) > 0:
	
	        # If result > 0 then arr[i] xored
	        # with the sum1
            	sum1 = (sum1 ^ arr[i])
	
	    else:
	
	        # If result == 0 then arr[i]
	        # xored with sum2
	        sum2 = (sum2 ^ arr[i])

  # Print the the two unique numbers
  print("The non-repeating elements are ",
		  sum1 ," and ", sum2)

# Driver Code
if __name__ == "__main__":

	arr = [ 2, 3, 7, 9, 11, 2, 3, 11 ]
	n = len(arr)
	
	UniqueNumbers2(arr, n)
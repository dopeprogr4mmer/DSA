def solveWordWrap(nums, k):
	#Code here
	cost = 0 
	i = 0
	length = len(nums)
	while i<=length-2:
	    z = k - nums[i]
	    #print(z,'l')
	    j = i+1
	    if j<length:
	    	#print(z, "kl")
	    	while(z>nums[j]):
	    	    z = z - nums[j] - 1
	    	    j = j+1
	    	    if j == length:
	    	        break
	    	    #print(z, 'k')
	    cost+=z
	    #print(cost,"h",nums[i])
	    i = j
	print(cost)
	return cost

solveWordWrap([6,6,7,4,4],9)


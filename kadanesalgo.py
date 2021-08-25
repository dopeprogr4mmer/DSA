import sys
#print(sys.maxsize)
def kadanes_algo(arr):
    best = arr[0]
    op = arr[0]
    for i in range(1, len(arr)):
        best = max(arr[i], arr[i]+best)
        op = max(best, op)
    print(op)
    return op

def max_product(arr):
	if len(arr)<2:
		return arr[0]

	curr_max = 1
	max_till_now = -sys.maxsize
	for i in range(len(arr)):
		curr_max *= arr[i]
		if curr_max == 0:
			curr_max = 1
		max_till_now = max(curr_max, max_till_now)

	curr_max = 1

	for i in range(len(arr)-1, -1, -1):
		curr_max *= arr[i]
		if curr_max == 0:
			curr_max = 1
		max_till_now = max(curr_max, max_till_now)

	print(max_till_now)
	return max_till_now

def subArrayExists(self,arr,n):
    ##Your code here
    #Return true or false
    set_ = set()
    sum_ = 0
    for i in range(n):
        sum_ += arr[i]
        if sum_ == 0 or sum_ in set_:
            return True
        set_.add(sum_)
    return False

def threeWayPartition(array, a, b):
	# code here 
	i = 0
	while True:
	    if array[i]<a and i<=0:
	        z = array.pop(i)
	        array.insert(0, z)
	        i+=1
	    elif array[i]>=a and array[i]<=b:
	        continue
	        #i+=1
	    else:
	    	if i<=len(array)-1:
	            z = array.pop(i)
	            array.insert(-1, z)
	        #i+=1
	    if i==len(array)-1:
	        break
	    print(i)
	print(array)
	return array


#kadanes_algo([-1,-2,-3,-4])
max_product([2, 3, -4, 5, -1, 0])
#threeWayPartition([1, 2, 3, 3, 4], 1, 2)
from itertools import combinations
def max_product_subarray(arr):
	max_product = 0
	max_product_subarray = []
	for i in range(1,len(arr)):
		arr_combinations = list(combinations(arr,i))
		#print(arr_combinations,'\n') 
		for temp_arr in arr_combinations:
			product = 1
			for element in temp_arr:
				product = product*element
			if product>max_product:
				#print(max_product_subarray,max_product)
				max_product = product
				max_product_subarray = temp_arr
	return max_product,max_product_subarray



	
max_product,max_product_subarray = max_product_subarray([2,3,4,5,-1,0])
print(max_product,max_product_subarray)
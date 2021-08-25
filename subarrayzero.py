#Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

from itertools import combinations
def subarrayZero(arr):
	if 0 in arr:
		return 'Ýes'

	for i in range(2,len(arr)):
		combinations_arr = list(combinations(arr,i))
		for temp_arr in combinations_arr:
			temp_sum = 0
			for element in temp_arr:
				temp_sum = temp_sum+element
				if temp_sum == 0:
					return 'Ýes'

	return 'No'

what = subarrayZero([4,2,-1,6,1])
print(f'What? {what}')
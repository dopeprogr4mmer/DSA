from itertools import combinations
def max_profit_subarray(price_list_array):
	start = 0
	enter_exit_point_list = []
	max_profit = 0
	while(start<len(price_list_array)-1):
		sublist = []
		for i in range(start,len(price_list_array)-1):
			#print(start,i+1,len(price_list_array))
			if price_list_array[i+1]>price_list_array[i]:
				if i+1 == len(price_list_array)-1:
					#print('hi')
					sublist.append(price_list_array[start])
					sublist.append(price_list_array[i+1])
					enter_exit_point_list.append(sublist)
					
				continue
			else:
				if i>start:
					sublist.append(price_list_array[start])
					sublist.append(price_list_array[i])
					enter_exit_point_list.append(sublist)
				break

		start = i+1
	print(enter_exit_point_list)
	if len(enter_exit_point_list)<2 and len(enter_exit_point_list)>0:
		max_profit = enter_exit_point_list[0][1] - enter_exit_point_list[0][0]
	else:
		combinations_list = list(combinations(enter_exit_point_list,2))
		print(combinations_list)
		sum_list = 0
		return_list = []
		for combination in combinations_list:
			print(combination)
			temp_sum = 0
			for listt in combination:
				print(listt)
				temp_sum += listt[1]-listt[0]
				print(temp_sum)
			if temp_sum>sum_list:
				return_list =  list(combination)
				max_profit = temp_sum

		enter_exit_point_list = return_list
		
	print(enter_exit_point_list,max_profit)


#max_profit_subarray([10,22,5,75,65,80])

def subset(k,l):
	for elem in l:
		#print(elem)
		if elem not in k:
			return False
	return True

#print(subset([1,2,3,4],[1,2,6]))

def find3Numbers(arr, X):
    # Your Code Here
    combinations_list = list(combinations(arr,3))
    #print(combinations_list)
    for element in combinations_list:
    	#print(element)
    	total = 0
    	for i in element:
    		#print(i)
    		total = total + i
    		#print(total)
    		if total == X:
    			return True
    return False

#print(find3Numbers([1,4,45,6,10,8],13))

def trapping_rain_water(block_length_list):
 	start = 0
 	maxima = block_length_list[start] 
 	local_maxima = 0
 	total = 0
 	while(start<len(block_length_list)-2):
 		t = []
 		for i in range(start+1,len(block_length_list)):
 			if block_length_list[i]<block_length_list[i-1]:
 				t.append(block_length_list[i])
 			else:
 				if block_length_list[i]>local_maxima:
 					local_maxima = block_length_list[i]
 					print(local_maxima,"hi")
 				if local_maxima>=maxima:
 					maxima = local_maxima
 					print(maxima,"hi again")
 					#t = [block_length_list[i]-elem for elem in t]

 				#if block_length_list[]
 				print('k',block_length_list[start],block_length_list[i])
 				temp_local_maxima = min(block_length_list[start],block_length_list[i])
 				print(maxima,'g')
 				t = [temp_local_maxima-elem for elem in t]
 				total = total + sum(t)
 				print(t,total)
 				break
 		start = i
 		print(start,'sd')

 	print(total)

#trapping_rain_water([3,0,0,5,0,4])


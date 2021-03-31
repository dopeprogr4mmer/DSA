def merge_interval(interval_list):
	print('hello world')
	i = 0
	interval_list = sorted(interval_list, key=lambda x: x[0])
	#print(interval_list)
	while(i<len(interval_list)-1):
		if interval_list[i][1]<interval_list[i+1][0]:
			pass
		else:
			interval_list[i][0] = min(interval_list[i][0],interval_list[i+1][0])
			interval_list[i][1] = max(interval_list[i][1],interval_list[i+1][1])

			del(interval_list[i+1])
			i=i-1
		i+=1
	return(interval_list)	


merged_intervavls = merge_interval([[1,2],[5,6],[4,7],[9,10],[3,5]])
print(merged_intervavls)
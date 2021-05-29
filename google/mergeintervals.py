def merge_interval(arr):
	if len(arr)==1:
		return arr
	arr.sort()
	print(arr)
	l = []
	i = 1
	#print("hi")
	while(True):
		if arr[i][0]<=arr[i-1][1]:
			arr[i-1][1] = max(arr[i][1], arr[i-1][1])
			arr.pop(i)
			print(arr)
		else:
			i+=1
		if i==len(arr):
			break
		#i+=1
		#continue
	print(arr)


merged_intervavls = merge_interval([[1,2],[5,6],[4,7],[7,10],[3,5]])
print(merged_intervavls)
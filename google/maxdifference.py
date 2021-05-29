def max_D(arr, n):
	maxA = [0]*n
	minA = [0]*n
	minA[0] = arr[0]
	maxA[n-1] = arr[n-1]
	for i in range(1,n):
		minA[i] = min(arr[i], minA[i-1])
	for j in range(n-2, -1, -1):
		maxA[j] = max(arr[j], maxA[j+1])
	i, j = 0, 0, 
	maxD = -1
	while(j<n and i<n):
		if minA[i]<maxA[j]:
			maxD = max(maxD, j-1)
			j+=1
		else:
			i+=1
	print(maxD)




arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
max_D(arr, len(arr))
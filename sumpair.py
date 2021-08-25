def sumPair(array,N):
	count = 0
	for i in range(len(array)-1):
		for j in range(i+1,len(array)):
			if array[i]+array[j] == N:
				count+=1

	return count

count = sumPair([1,1,1,1],2)
print(count)


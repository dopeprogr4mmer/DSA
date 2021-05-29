def zero_sum(arr):
	output = []
	s = set()
	for i in range(len(arr)-1):
		for j in range(i+1, len(arr)):
			x = arr[i] + arr[j]
			if x in s:
				output.append((arr[i], arr[j], x))
			else:
				s.add(x)

	return output

def zero_sum_alternative(arr):
	output = []
	n = len(arr)
	arr.sort()
	for i in range(n-1):
		x = arr[i]
		l = i+1
		r = n-1
		while(l<r):
			z = x + arr[l] + arr[r]
			if z==0:
				output.append((x,arr[l],arr[r]))
				l+=1
				r-=1
			elif z<0:
				l+=1
			else:
				r-=1

	return output



if __name__ == '__main__':
	arr = [0, -1, 2, -3, 1]
	output = zero_sum_alternative(arr)
	if output!=[]:
		for triplet in output:
			print(triplet)
	else:
		print("No such triplet found!")

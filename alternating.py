def alternating(array):
	for i in range(len(array)-1):
		if i%2==0 and array[i]>0:
			for j in range(i+1,len(array)):
				if array[j]<=0:
					array.insert(i,array[j])
					del(array[j+1])
					break
		if i%2==1 and array[i]<0:
			for j in range(i+1,len(array)):
				if array[j]>=0:
					array.insert(i,array[j])
					del(array[j+1])
					break		
	return array

alternating_array = alternating([-1,-5,2,-3,4,5,-6,0,15,418,-59,36,48,-111,548,658,9874,5478,6223,-54])
print(alternating_array)

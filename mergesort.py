def merge(list1,list2):
	m,n = len(list1),len(list2)
	C,i,j = [],0,0
	while i+j<m+n:
		if i==m:
			C.append(list2[j])
			j+=1
		elif j==n:
			C.append(list1[i])
			i+=1
		elif list1[i]<=list2[j]:
			C.append(list1[i])
			i+=1
		elif list2[j]<list1[i]:
			C.append(list2[j])
			j+=1
	return C

#merge([1,5,7,11],[2,3])

def merge_sort(Array,left,right):
	if right-left <= 1:
		return Array[left:right]
	else:
		mid = (right+left)//2

		L = merge_sort(Array,left,mid)
		R = merge_sort(Array,mid,right)

		return merge(L,R)

sorted_array = merge_sort([1,6,6,6,7,17,9,2,11,52,-1,0,0,0,68,95,12,0,3,-77],0,20)
print(sorted_array)
<<<<<<< HEAD
<<<<<<< HEAD
def max_diference(matrix):
	m = len(matrix)
	n = len(matrix[0])
	arr = []
	for i in range(m):
		for j in range(i,n):
			print(matrix[i][j])
			arr.append(matrix[i][j])

	k = len(arr)
	l = [None]*k
	r = [None]*k
	o = [None]*k

	for i in range(k):
		#print(i)
		l[i] = min(arr[:i+1])
		r[i] = max(arr[i:])
		o[i] = r[i] - l[i]

	print(l, r)

	return max(o)




mat = [[ 1, 2, -1, -4, -20 ],
       [ -8, -3, 4, 2, 1 ],
       [ 3, 8, 6, 1, 3 ],
       [ -4, -1, 1, 7, -6 ],
       [ 0, -4, 10, -5, 1 ]]


m = max_diference(mat)
#print(m)
=======
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
def minJump(n,array):
    element_position = 1
    jump_count = 0
    while(element_position<n):
        element_position += array[element_position-1]
        jump_count+=1
        if element_position>=n:
            return jump_count
       
   
   
if __name__ == "__main__":
    min_jump = minJump(6,[1, 4, 3, 2, 6, 7])
<<<<<<< HEAD
    print(min_jump)
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
    print(min_jump)
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05

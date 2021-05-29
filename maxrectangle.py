def max_rectangle(arr):
	point_a = point_b = point_c = point_d = arr[0][0]
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if arr[i][j] == 1:
				#point_a = point_b = arr[i][j]
				for x in range(i,len(arr)):
					for y in range()

arr = [[0, 1, 1, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 0, 0]]

if __name__ == '__main__':
	max_rectangle(arr)

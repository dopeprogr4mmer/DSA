def max_rectangle(arr):
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			print(arr[i][j])

arr = [[0, 1, 1, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 0, 0]]

if __name__ == '__main__':
	max_rectangle(arr)

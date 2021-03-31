def max_diff(arr):
	max_val = 0
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			for x in range(i+1,len(arr)):
				for y in range(j+1,len(arr[0])):
					if max_val<arr[x][y]-arr[i][j]:
						max_val = arr[x][y]-arr[i][j]

	print(max_val)




arr = [[1, 2, -1, -4, -20 ],
       [ -8, -3, 4, 2, 1 ], 
       [ 3, 8, 6, 1, 3 ],
       [ -4, -1, 1, 7, -6 ],
       [ 0, -4, 10, -5, 1 ]]

if __name__ == '__main__':
	max_diff(arr)
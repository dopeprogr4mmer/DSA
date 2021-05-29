import math
from pprint import pprint
def transpose(matrix, i):
	for x in range(i):
		for y in range(x,i):
			matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
	#rotate_rows(matrix, i)
	#pprint(matrix)
	return matrix

def rotate_cols(matrix, i):
	#print('hi')
	for x in range(i):
		a, b = 0, i-1
		while(b>a):
			#print(matrix[a][x], matrix[b][x])
			matrix[a][x], matrix[b][x] = matrix[b][x], matrix[a][x]
			a+=1
			b-=1
	#pprint(matrix)
	#rotate_cols(matrix, i)
	return matrix

def rotate_rows(matrix, i):
	#print('hi')
	for x in range(i):
		a, b = 0, i-1
		while(b>a):
			#print(matrix[x][a], matrix[x][b])
			matrix[x][a], matrix[x][b] = matrix[a][x], matrix[b][x]
			a+=1
			b-=1

	return matrix

def print_matrix(matrix):
	print()
	print(f'Matrix rotated 90 degrees anticlockwise')
	pprint(matrix)

def rotate90(matrix, i):
	pprint(matrix)
	matrix = transpose(matrix, i)
	#matrix = rotate_rows(matrix, i)
	matrix = rotate_cols(matrix, i)
	print_matrix(matrix)

def alternate(matrix, n):
	y = n-1
	for i in range(n//2):
		#temp = ['?']*(n)
		#print(temp)
		for j in range(i,n-1-i):
			#print(n-1-i)
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][n-1-i]
			#print(matrix[j][n-1-j])

			matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
			matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
			matrix[n-1-j][i] = temp

	pprint(matrix)



matrix = [[1, 51, 61, 71, 81, 91,55, 15],
		  [2, 59, 1, 1, 1, 1, 90, 0],
          [4, 0, 30, 1, 1, 80, 1, 1],
          [5, 2, 20, 26, 72, 0, 1, 0],
          [7, 1, 1, 212, 29, 0, 1, 0],
          [8, 1, 75, 2, 42, 28, 2, 0],
          [9, 84, 1, 1, 1, 62, 111, 1],
          [10, 11, 12, 13, 14, 25, 26, 17]]

alternate(matrix, len(matrix))

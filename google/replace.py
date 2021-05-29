from pprint import pprint
def check(matrix, i, j, l=[]):
	print(i, j, matrix[i][j])
	if (i<1 or j<1 or i>6 or j>6):
		return False
	if matrix[i][j]!=0 or (i,j) in l:
		return False
	else:
		print('hi')
		neighbors = [(i,j-1), (i,j+1), (i-1,j), (i+1,j)]
		for x in neighbors:
			if matrix[x[0]][x[1]]==0:
				l.append(x)
				if check(matrix, x[0], x[1], l):
					for z in l:
						matrix[z[0]][x[1]] = 'i'
		return True

def forward(matrix):
	pprint(matrix)
	for i in range(8):
		for j in range(8):
			if matrix[i][j] == 0:
				check(matrix, i, j, [])
	pprint(matrix)


def XS(matrix):
	for i in range(8):
		for j in range(8):
			if matrix[i][j] == 0:
				if not (i>0 and j>0 and i<7 and j<7):
					matrix[i][j] = 'x'
	pprint(matrix)
	forward(matrix)


	#pprint(matrix)



matrix = [[0, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 0, 0, 0, 1, 0],
          [1, 0, 1, 0, 0, 1, 0, 0],
          [1, 1, 1, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 1, 1, 0],
          [1, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1, 1, 1, 1]]

XS(matrix)
from collections import deque
from  pprint import pprint
def validate(i, j, m, n):
	if i>m or j>n or i<0 or j<0:
		return False
	return True


def floodfill(matrix, m, n, k):
	q = deque()
	for i in range(m):
		for j in range(n):
			if matrix[i][j]==k:
				#print("ji")
				q.append([i, j])
				#matrix[i][j]=3 
				while q:
					#print("ji",i)
					z = q.popleft()
					x, y = z[0], z[1]
					matrix[x][y] = 3
					#pprint(matrix)
					neighbours = [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]
					for neighbour in neighbours:
						a, b = neighbour[0], neighbour[1]
						if validate(a, b, m-1, n-1):
							#print(m, n)
							if matrix[a][b] == 2:
								q.append([a, b])
				return matrix

def floodFill(image, sr, sc, newColor):
	R, C = len(image), len(image[0])
	color = image[sr][sc]
	if color == newColor: 
		return image
	def dfs(r, c):
		if image[r][c] == color:
			image[r][c] = newColor
		if r >= 1: 
			dfs(r-1, c)
		if r+1 < R: 
			dfs(r+1, c)
		if c >= 1: 
			dfs(r, c-1)
		if c+1 < C: 
			dfs(r, c+1)
		
	dfs(sr, sc)
	return image



matrix = [[1, 1, 1, 1, 1, 1, 1, 1],
		  [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]




if __name__ == '__main__':
	try:
		print("To be filled:")
		pprint(matrix)
		m = len(matrix)
		n = len(matrix[0])
		filled_matrix=floodFill(matrix, 3, 1, 2)
		print()
		print("Filled Matrix:")
		pprint(filled_matrix)
	except Exception:
		errorno = 50159747054
		print(f"Hey Phantom, there's a {errorno: #x} error")

from pprint import pprint
def minimum_insertions(string):
	n = len(string)
	#print("hello")
	rev = "".join(list(string)[::-1])
	#print(rev)
	grid = [[0 for i in range(n+1)] for j in range(n+1)]

	for x in range(n+1):
		for y in range(n+1):
			#print("hello")
			if x==0 or y==0:
				grid[x][y] = 0
				#pprint("df")
			elif string[x-1] ==  rev[y-1]:
				#print("d")
				grid[x][y] = grid[x-1][y-1] + 1
			else:
				grid[x][y] = max(grid[x][y-1], grid[x-1][y])

	#pprint(grid)
	count = n - grid[n][n]
	#print(count)
	return count


if __name__ == '__main__':
	try:
		string = 'babcde'
		count=minimum_insertions(string)
		print(count)
	except Exception:
		errorno = 50159747054
		print(f"Hey Phantom, there's a {errorno: #x} error")
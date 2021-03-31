def is_safe(x,y,maze):
	limit_x, limit_y = len(maze), len(maze[0])
	#print(x,y)
	if x>=0 and y>=0 and x<limit_x and y<limit_y and maze[x][y]!=1:
		return True
	return False

def print_solution(sol,maze):
	for i in range(len(sol[0])):
		for j in range(len(sol[1])):
			if maze[i][j] == 1:
				print(1,end = '    ')
			else:
				print(sol[i][j],end='    ')
		print()
		print()


def solve_maze(start,end,maze,sol):
	x,y  = start[0], start[1]
	if maze[end[0]][end[1]] == 1:
		#print("Way blocked. Can't reach target")
		return False
	if start == end:
		sol[x][y] = 'o'
		print_solution(sol,maze)
		return True

	if is_safe(x,y,maze):
		if sol[x][y] == 'o':
			return False
		sol[x][y] = 'o'
		for i in reversed(range(x-1,x+2)):
			for j in reversed(range(y-1,y+2)):
				#print(i,j,'test')
				if i+j in [x+y-1,x+y+1] and solve_maze([i,j],end,maze,sol):
					return True

		sol[i][j] = 0
		#print("Way blocked. Can't reach target")
		return False
		

	
	#print(sol)
	#print_solution(sol)

	

maze = [[0, 1, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0]]

sol = [['.' for j in i] for i in maze]


if __name__ == '__main__':
	solution = solve_maze([0,0],[6,6],maze,sol)
	if not solution:
		print("Lane Blocked. Can't exit trap!")
"""
A program to check if a horse can reach a given target in a m x n board
"""

def neighbours(current_position,grid):
	"""
	function to find possible moves from a given block
	"""
	nx = current_position[0]
	ny = current_position[1]
	possible_moves = []
	temp = [(nx-2,ny-1),(nx-2,ny+1),(nx+2,ny-1),(nx+2,ny+1),(nx-1,ny-2),(nx-1,ny+2),(nx+1,ny-2),(nx+1,ny+2)]
	for move in temp:
		if not(move[0]<0 or move[1]<0 or move[0]>grid[0]-1 or move[1]>grid[1]-1 or move == current_position):
			possible_moves.append(move)
	
	return possible_moves


def explore(target,start,grid):
	"""
	function to move the horse around dthe block
	""" 
	assert not (target[0]<0 or target[1]<0 or start[0]<0 or start[1]<0 or grid[0]<0 or grid[1]<0)
	tx, ty = target[0], target[1]
	marked = [[0 for i in range(grid[1])]
	                for n in range(grid[0])]
	queue = [start]
	while queue!= []:
		current_position = queue.pop()
		for possible_move in neighbours(current_position,grid): 
			a = possible_move[0]
			b = possible_move[1]
			if possible_move == target:
				return "Horse at Target"
			if not marked[a][b]:
				marked[a][b] = 1
				queue.insert(0,possible_move)
	
	return "Cannot reach target"


print(explore((1,0),(0,0),(3,3)))



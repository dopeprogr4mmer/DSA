#from collections import deque
"""
def is_safe(maze, pos):
	x, y = pos[0], pos[1]
	if x<len(maze) and y<len(maze[0]):
		if maze[x][y] == 1:
			return True


def rat_in_a_maze(maze, pos=(0,0), direction=[]):
	#pos = q.pop()
	#print('ni',pos, maze)
	if pos == (len(maze)-1, len(maze[0])-1):
		if is_safe(maze, pos):
			#print('hi')
			return "".join(direction)

	x, y = pos[0], pos[1]
	possible=[(x+1,y),(x,y+1)]
	for path in possible:
		#print(path)
		if is_safe(maze, path):
			#print('l')
			maze[x][y]=2
			if possible.index(path)==0:
				direction.append('D')
			else:
				direction.append('R')
			pos = path
			if rat_in_a_maze(maze, pos, direction):
				#print('ji')
				return "".join(direction)
			direction.pop()
		#return False
	return False
	"""

class Solution:
    #def findPath(self, m, n):
        # code here
    def is_safe(self, maze, pos):
	    x, y = pos[0], pos[1]
	    if x<len(maze) and y<len(maze[0]):
	    	if maze[x][y] == 1:
	    		return True
	    return False


    def findPath(self, maze, n, pos=(0,0), direction=[], l=[]):
    	#pos = q.pop()
    	#print('ni',pos, maze)
    	#print(pos)
    	if maze[0][0] == 0:
    		return -1
    	x, y = pos[0], pos[1]
    	if (x, y) == (n-1, n-1):
    		if self.is_safe(maze, pos):
    			#print('hi')
    			z = "".join(direction)
    			if z not in l:
    				l.append(z)
    
    	#x, y = pos[0], pos[1]
    	possible=[(x+1,y),(x,y-1),(x,y+1)]
    	for path in possible:
    		#print(possible)
    		if self.is_safe(maze, path):
    			print(path)
    			maze[x][y]=2
    			if possible.index(path)==0:
    				direction.append('D')
    			else:
    				direction.append('R')
    			pos = path
    			self.findPath(maze, n, pos, direction)
    				#print('ji')
    				#return True
    			maze[x][y]=1
    			direction.pop()
    		#return False 
    	x = self.findPath([[0,0],[0,0]], 2)
    	return l if len(l)>0 else -1

	

maze = [[1, 0, 0, 0],
        [1, 1, 0, 1], 
        [1, 1, 0, 0],
        [0, 1, 1, 1]]

#q = deque()
#q.append((0,0))
s = Solution()
sol = s.findPath(maze, 4)
print(sol)
""" author: @phantom 05-07-2021"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check(cell, grid):
            #print(cell)
            i = cell[0]
            j = cell[1]
            if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]!=1:
                return False
            #print('k')
            return True

        minutes = 0
        current_level = []
        next_level = []
        #queue = [(0,0)]
        count = 0
        rotten = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #print('k')
                if grid[row][col]==2:
                    current_level.append((row, col))
                    count += 1
                if grid[row][col]==1:
                    #print(row, col, count)
                    count+=1
        
        if current_level == []:
            #print('l')
            if count>0:
                return -1
            return 0

        while len(current_level)!=0:
            current_cell = current_level.pop(0)
            #print(current_cell)
            rotten+=1
            x = current_cell[0]
            y = current_cell[1]
            grid[x][y]=2
            adjacent_cells = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            for cell in adjacent_cells:
                if check(cell, grid):
                    if cell not in next_level and cell not in current_level:
                        next_level.append(cell)
            if len(current_level)==0 and len(next_level)!=0:
                minutes+=1
                current_level, next_level = next_level, current_level
        
        #print(rotten, count, minutes)
        if rotten!=count:
            return -1
        print(minutes)
        return minutes

s = Solution()
s.orangesRotting([[1,2,1,1,2,1,1]])
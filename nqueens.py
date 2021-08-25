def print_board(board):
	for row in board:
		for square in row:
			if square == 'Q':
				print(square, end="    ")
			else:
				print('-', end = '    ')
		print()
		print()

def is_unallocated(board,row,col):
	if board[row][col] == 0:
		return True

def update_board(board,row,col):
	temp_i, temp_j = row, col
	for i in range(row,len(board)):
		for j in range(len(board)):
			if board[i][j] == 0:
				if i == row or j == col:
					board[i][j] = row+1
			if i == temp_i+1 and j == temp_j+1:
				if board[i][j] == 0:
					board[i][j] = row+1
				temp_i, temp_j = i, j
	for i in range(len(board)):
		for j in range(len(board)):
			if i+j == row+col and is_unallocated(board,i,j):
				board[i][j] = row+1
	#print(board)

def undo_board(board,row):
	#print(row,"ündo")
	for i in range(len(board)):
		if board[row][i] == 'Q':
			board[row][i] = 0
		for j in range(len(board)):
			if board[i][j] == row+1:
				board[i][j] = 0
	#print_board(board)


def is_safe(board,row,col):
	if board[row][col] == 0:
		update_board(board,row,col)

		return True
	return False

def nqueens(board,row=0):
	#print(row)
	global soln_count
	for col in range(len(board)):
		#print(row,col,'hj')
		if is_safe(board,row,col):
			board[row][col] = 'Q'
			if row == len(board)-1:
				print(f'Solution {soln_count}')
				print_board(board)
				print()
				print()
				print()
				soln_count+=1	  #for all solutions
				#return True      #for a single solution
			else:
				extend_soln = nqueens(board, row+1)
			'''if extend_soln:
				return True
			else:'''     		  #for all solutions
			undo_board(board,row)
	return False


board = [[0 for j in range(8)] for i in range(8)]	
soln_count = 1
nqueens(board)
#print_board(board)
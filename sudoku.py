def print_board(board):
	for row in board:
		for number in row:
			print(number, end = '    ' )
		print()
		print()
		#print()



def is_safe(board, row, col, number):
	#number = board[row][col]
	if not board[row][col] == 0:
		return False
	start_row = (row//3)*3
	end_row = start_row+3
	start_col =(col//3)*3
	end_col = start_col+3
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][col] == number or board[row][j] == number:
				return False
	for i in range(start_row,end_row):
		for j in range(start_col,end_col):
			if board[i][j] == number:
				return False
	return True


def  unsassigned(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 0:
				return True
	return False


'''def is_free(board, row, col):
	if board[row][col] == 0:
		return True
	return False
	'''


def solve(board):
	#print('j')
	if not unsassigned(board):
		print_board(board)
		print('done')
		return True
	for row in range(len(board)):
		for col in range(len(board)):
			for number in range(1,10):
				if is_safe(board, row, col, number):
					board[row][col] = number
					print('doing')
					print_board(board)
					
					if solve(board):
						return True
	
					boarld[row][col] = 0
	return False
			

	#print_board(board)

board = [[1, 2, 0, 6, 0, 8, 0, 0, 0],
         [5, 8, 4, 2, 3, 9, 7, 0, 1],
         [0, 6, 0, 1, 4, 0, 0, 0, 0],
         [3, 7, 0, 0, 6, 1, 5, 8, 0],
         [6, 9, 1, 0, 8, 0, 2, 7, 4],
         [4, 5, 8, 7, 0, 2, 0, 1, 3],
         [0, 3, 0, 0, 2, 4, 1, 5, 0],
         [2, 0, 9, 8, 5, 0, 4, 3, 6],
         [0, 8, 0, 3, 0, 6, 0, 9, 2]]
#initialize()
#print_board(board)
solve(board)
def print_board(board):
	for row in board:
		for number in row:
			print(number, end = '    ' )
		print()
		print()
<<<<<<< HEAD
<<<<<<< HEAD

def find_empty_location(board,l):		#prunes for faster execution
	for i in range(N):
		for j in range(N):
			if board[i][j] == 0:
				l[0] = i
				l[1] = j
				return True
	return False


def is_safe(board, row, col, number):
	for x in range(N):
		if x!= col:
			if board[row][x] == number:
				#print('n1')
				return False

	for x in range(N):
		if x!= row:
			if board[x][col] == number:
				#print('n2')
				return False
	startrow = row - row%3
	startcol = col - col%3

	for i in range(3):
		for j in range(3):
			if (i+startrow)!=row and (j+startcol)!=col:
				if board[i + startrow][j + startcol] == number:
					return False
	return True


def solve(board, row, col):
	if (row==N-1 and col==N):
		return True

	if col==N:
		row+=1
		col=0

	if board[row][col]>0:		#also checks if given values obey
		n = board[row][col]
		if is_safe(board, row, col, n):
			return solve(board, row, col+1)
		return False

	for number in range(1, N+1):
		if is_safe(board, row, col, number):
			board[row][col] = number

			if solve(board, row, col+1):
				#print_board(board)
				#print()
				return True

		#print(board)
		board[row][col] = 0

	return False

def alternate(board):			#doesn't check if the given values obey. Skips those values!
	l = [0,0]

	if not find_empty_location(board, l):
		return True

	row, col = l[0], l[1]		#lists are mutable


	for number in range(1,N+1):
		if is_safe(board, row, col, number):
			board[row][col] = number

			if alternate(board):
				return True

			board[row][col] = 0

	return False

def check_board(board):		#checks the given values
	for i in range(N):
		for j in range(N):
			if board[i][j]>0:
				#print("no")
				if not is_safe(board, i, j, board[i][j]):
					print("hi",i,j)
					return False
	return True
	

N = 9	
board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print(check_board(board))

if check_board(board):
	if alternate(board):
		print_board(board)
	else:
		print("No solution is possible!")
else:
	print("Given values don't obey!")
=======
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
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
				else:
					continue
					
				if solve(board):
					return True
				board[row][col] = 0
	retur False
			

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
<<<<<<< HEAD
solve(board)
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
solve(board)
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05

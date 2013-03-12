board = []

for i in range(1, 4):
	board.append(["_"] * 3)

def print_board(board):
	for i in board:
		print " ".join(i)

print_board(board) 

def place_x():
	print "It's X's turn."
	row = int(raw_input("Row: ")) - 1
	col = int(raw_input("Column: ")) - 1
	
	if (board[row][col] != "X") and (board[row][col] != "O"):
		board[row][col] = "X"
	elif (1 > row > 3):
		print "That is not on the board."
	else:
		print "That is not a legal move. Pick a spot where there is no X or O."
	print_board(board)

def place_o():
	print "It's O's turn."
	row = int(raw_input("Row: ")) - 1
	col = int(raw_input("Column: ")) - 1
	
	if (board[row][col] != "X") and (board[row][col] != "O"):
		board[row][col] = "O"
	elif (1 > row > 3):
		print "That is not on the board."
	else:
		print "That is not a legal move. Pick a spot where there is no X or O."
	print_board(board)

place_o()

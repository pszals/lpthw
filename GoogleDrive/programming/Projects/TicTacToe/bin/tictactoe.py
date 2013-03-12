board = []

for i in range(1, 4):
	board.append(["_"] * 3)

def print_board(board):
	for i in board:
		print " ".join(i)

print_board(board) 

def place_x():
	row = int(raw_input("Row: "))
	col = int(raw_input("Column: "))
	
	if board[row][col] != "_" and (board[row][col] != "X") and (
													board[row][col] != "O"):
		board[row][col] = "X"
	print board

place_x()



																
from sys import exit

board = []

for i in range(1, 4):
	board.append(["_"] * 3)

def print_board(board):
	for i in board:
		print " ".join(i) 

def place_x():
	""" Allows the user to input an X onto the game board """
	print "It's X's turn."
	row = int(raw_input("Row: ")) - 1
	col = int(raw_input("Column: ")) - 1

		# I thought that this would solve the error that occurs if something other
		# than a 1,2, or 3 is entered. Not sure why it does not.
	if (row not in range(1, 4)) or (col not in range(1, 4)):	
		print "That is not on the board. Pick a spot where there is no X or O."
		place_x()
	elif (board[row][col] != "X") and (board[row][col] != "O"):
		board[row][col] = "X"	
	else:
		print "That is not a legal move. Pick a spot where there is no X or O."
		place_x()
		
def place_o():
	""" Allows the user to input an O onto the game board """
	print "It's O's turn."
	row = int(raw_input("Row: ")) - 1
	col = int(raw_input("Column: ")) - 1
	
	if (row not in range(1, 4)) or (col not in range(1, 4)):	
		print "That is not on the board. Pick a spot where there is no X or O."
		place_o()
	elif (board[row][col] != "X") and (board[row][col] != "O"):
		board[row][col] = "O"
	else:	
		print "That is not a legal move. Pick a spot where there is no X or O."
		place_o()

def play_game():
	"""This will run the game."""
	count = 0	
	while True:
		if (count % 2 == 0) and (count < 9):
			count += 1
			print_board(board)
			place_x() 
		elif (count % 2 != 0) and (count < 9):
			count += 1
			print_board(board)
			place_o()
		elif count == 9:
			print_board(board)
			#find_winner()
			print "Game Over"
			exit()

# location = board[row][col]
# There has to be a better way to talk about the spots on the board...
loc1 = board[0][0]
loc2 = board[0][1]
loc3 = board[0][2]
loc4 = board[1][0]
loc5 = board[1][1]
loc6 = board[1][2]
loc7 = board[2][0]
loc8 = board[2][1]
loc9 = board[2][2]

winning_triples = [(loc1, loc2, loc3), (loc4, loc5, loc6), (loc7, loc8, loc9),
(loc1, loc4, loc7), (loc2, loc5, loc8), (loc3, loc6, loc9),	
(loc1, loc5, loc9),	(loc7, loc5, loc3)]

winner1 = [(loc1, loc2, loc3)]
winner2 = [(loc4, loc5, loc6)]
winner3 = [(loc7, loc8, loc9)]
winner4 = [(loc1, loc4, loc7)]
winner5 = [(loc2, loc5, loc8)]
winner6 = [(loc3, loc6, loc9)]
winner7 = [(loc1, loc5, loc9)]
winner8 = [(loc7, loc5, loc3)] 

winning_game = [triple for board_triple in board for triple in winning_triples if board_triple == triple]

def find_winner():
	if winning_game[0, 1, 2] == ['X', 'X', 'X']:
		print "X wins"
		exit()
	elif winning_game[0, 1, 2] == ['O', 'O', 'O']:
		print "O wins"
		exit()
	elif winning_game == []:
		print "Cat's game"
		exit()			

play_game()

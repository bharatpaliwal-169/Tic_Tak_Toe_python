#This is TicTakToe Game.....
#...................Global Variables ..........
#Game Board....
board = [
				 "-","-","-",
				 "-","-","-",
				 "-","-","-"
				]
#game-on/off looper..
game_still_going = True
#current player
current_player = "X"
#result
winner = None


#displaying the game board..
def displayBoard():
	print("\n")
	print(board[0] + " | " + board[1] + " | " + board[2] + "  1 | 2 | 3 ")
	print(board[3] + " | " + board[4] + " | " + board[5] + "  4 | 5 | 6 ")
	print(board[6] + " | " + board[7] + " | " + board[8] + "  7 | 8 | 9 ")
	print("\n")
#-------End Display------------------------------

#___________Handel Turns______________________

def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there, Try again!")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  displayBoard()

#end of handel_turn
#______________________________________________
def check_if_gameover():
	check_if_win()
	check_if_tie()


def check_if_win():

	global winner


	#check rows 
	row_winner = check_rows()
	#check columns
	col_winner = check_columns()
	#check diagonals
	diagonal_winner = check_diagonals()

	if row_winner:
		winner = row_winner
	elif col_winner:
		winner = col_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None

#__________________________________________________________
def check_rows():

	global game_still_going


	row_1 = board[0] == board[1] == board[2] != '-'
	row_2 = board[3] == board[4] == board[5] != '-'
	row_3 = board[6] == board[7] == board[8] != '-'

	if row_1 or row_2 or row_3:
		game_still_going = False
	
	if row_1:
		return board[0] 
  
	elif row_2:
  
	  return board[3]

  
	elif row_3:
  
	  return board[6] 
  # Or return None if there was no winner
  
	else:
	  return None
	
#___________________________________________________________
	
def check_columns():

	global game_still_going

	col_1 = board[0] == board[3] == board[6] !=  '-'
	col_2 = board[1] == board[4] == board[7] !=  '-'
	col_3 = board[2] == board[5] == board[8] !=  '-'

	if col_1 or  col_2 or col_3:
		game_still_going= False

	if col_1:
		return board[0]
	elif col_2:
		return board[1]
	elif col_3:
		return board[2]

	else:
		return None
#___________________________________________________________	 
def check_diagonals():
	global game_still_going

	d1 = board[0] == board[4] == board[8] != '-'
	d2 = board[2] == board[4] == board[6] != '-'

	if d1 or d2 :
		game_still_going = False
	
	if d1:
		return board[0]
	elif d2:
		return board[2]

	else:
		return None
#__________________________________________________________	

def check_if_tie():
	global game_still_going

	if '-' not in board:
		game_still_going = False
		return True
	
	else:
		return False
#______________________________________________
	


def flip_player():
	global current_player 

	if current_player == "X":
		current_player = "O"
	
	elif current_player == "O":
		current_player = "X"

#__________________________________________________________
#-----------GamePlay----------------------
def gamePlay():
	#display the empty board at the first...
	displayBoard()

	#handel the turns ...
	while game_still_going:
		handle_turn(current_player)
		
		check_if_gameover()

		flip_player()
	
	#end of game 
	if winner == 'X' or winner == 'O':
		print(winner + " Won!")
	
	else:
		print("It's a Tie!")
#.....................end of gameplay.......
#__________________________________________________________
gamePlay()




 # Global variables
 board = {}
 turn = 'X'
 winner = None
 
 def init_game():
   # Use the global keyword to update global variables
   global board, turn
   board = {
   	'a1': None, `b1`: None, 'c1' None,
   	# etc
   }
   turn = 'X'


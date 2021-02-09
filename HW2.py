# 1 For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3. Make a function create_board() that creates such 
#a board, with values of integers 0. 
import numpy as np
def create_board():
    return np.zeros((3,3))
board = create_board()

# 2
#Players 1 and 2 will take turns changing values of this array from a 0 to a 1 or 2, indicating the number of the player who places there. 
#Create a function place(board, player, position) with player being the current player (an integer 1 or 2), and position a tuple of length 
#2 specifying a desired location to place their marker. Only allow the current player to place a piece on the board (change the board position 
#to their number) if that position is empty (zero).
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    else:
        print("That space is already occupied! Try again.")
    

place(board, 1, (0,0))
              

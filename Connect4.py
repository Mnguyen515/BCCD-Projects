import numpy as np

# Set size for the board
ROW_COUNT = 8
COLUMN_COUNT = 8

# Function creates the board filled with 0's initially
def create_board():
    board = np.zeros((8,8))
    return board
 
# Function places a piece where the player specifies
def drop_piece(board,row,col,piece):
    board[row][col]= piece

# Function checks if the move made is a valid location
def is_valid_location(board,col):
    #if this condition is true we will let the use drop piece here.
    #if not true that means the col is not vacant
    return board[5][col]==0

# Function makes the rows on the board
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r
        
# Function will print the board after every move
def print_board(board):
    print(np.flip(board,0))

# Function returns true after analyzing the board for a 4 in a row in possible direction
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
 
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
 
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
 
    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

# Initialize game settings
board = create_board()
print_board(board)
game_over = False
turn = 0

# Prompt a turn for each player until one of them gets 4 in a row
while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1, Make your Selection(0-8):"))
        #Player 1 will drop a piece on the board
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,1)
            if winning_move(board, 1):
                print("PLAYER 1 WINS!")
                game_over = True
         
    #Ask for player 2 input
    else:
        col = int(input("Player 2, Make your Selection(0-8):"))
        #Player 2 will drop a piece on the board
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,2)
            if winning_move(board, 1):
                print("PLAYER 2 WINS!")
                game_over = True

    # Reprint the board after every turn
    print_board(board)
    
    # Increment the turns
    turn += 1
    turn = turn % 2
# global variables

# board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-'] 
game = True
winner = None
current_player = 'x'

# display board
def display_board():
    print(board[0]+' | '+board[1]+' | '+board[2])
    print(board[3]+' | '+board[4]+' | '+board[5])
    print(board[6]+' | '+board[7]+' | '+board[8])
# play game
def play_game():
    display_board()

    while game:
        handle_turn(current_player)
        check_game()
        # flip player x to o
        flip_player()
    if winner == 'x' or winner == 'o':
        print(winner + ' won')
    elif winner == None:
        print('Tie')

# handle turn
def handle_turn(player):
    position = input('choose position from 1-9: ')
    position = int(position) - 1
    board[position] = 'x'
    display_board()

def check_game():
    check_win()
    check_tie()
    
def check_winner():
    # sets winner to global scope
    global winner
    row_winner = check_rwos()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_inner:
        winner = row_winner()
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
def check_rows():
    global game
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game = False
    if row_1: 
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return 
def check_columns():
    global game
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    if column_1 or column_2 or column_3:
        game = False
    if column_1: 
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return  
def check_diagonals():
    global game
    diagonals = board[0] == board[4] == board[8] != '-'
    diagonals = board[6] == board[4] == board[2] != '-'
    if diagonals or diagonals:
        game = False
    if diagonals: 
        return board[0]
    elif diagonals:
        return board[6]
    return  
def check_win():
    return 
def check_tie():
    return 
def flip_player():
    return 
play_game()
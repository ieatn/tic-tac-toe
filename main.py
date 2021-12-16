# global variables
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
        # x gets a turn
        handle_turn(current_player)
        # check if game over
        check_game()
        # o gets a turn
        flip_player()
    # game is over, winner is set to x or o or none
    if winner == 'x' or winner == 'o':
        print(winner + ' won')
    elif winner == None:
        print('Tie')

# player picks a index
def handle_turn(player):
    print(player + " 's turn.")
    position = input('choose position from 1-9: ')
    valid = False
    while not valid: 
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('invalid input. choose a position from 1-9')
        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print(" you can't go there. Go again.")
            
            
    board[position] = player
    display_board()


def check_game():
    check_win()
    check_tie()
    
def check_win():
    # check rows
    # check columns
    # check diagonals
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return 
        
def check_rows():
    global game
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game = False
    # return the winner x or o
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
    diagonals_1 = board[0] == board[4] == board[8] != '-'
    diagonals_2 = board[6] == board[4] == board[2] != '-'
    if diagonals_1 or diagonals_2:
        game = False
    if diagonals_1: 
        return board[0]
    elif diagonals_2:
        return board[6]
    return

def check_tie():
    global game
    if '-' not in board:
        game = False
    return

def flip_player():
    global current_player
    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'
    return

# driver code
if __name__ == '__main__':
    play_game()
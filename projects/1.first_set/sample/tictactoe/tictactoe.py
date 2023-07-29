board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

PLAYER_1 = 'X'
PLAYER_2 = 'O'
step = 0


def print_board():
    for row in board:
        print(row)
    
    print('________________')


def player_move():
    """

    """
    global step
    current_player = PLAYER_1 if step % 2 == 0 else PLAYER_2
    print(f'Player {current_player} turn!')
    
    while True:
        move_x = int(input('Enter x coordinate: '))
        move_y = int(input('Enter y coordinate: '))
        if 1 <= move_x <= 3 and 1 <= move_y <= 3 and board[move_y - 1][move_x - 1] is None:
            board[move_y - 1][move_x - 1] = current_player
            step = step + 1
            return
        
        print('Invalid input try again!')


def is_winner(player):
    # Check rows
    for row in board:
        all_same = True
        for item in row:
            if item != player:
                all_same = False
        
        if all_same:
            return True
    # Check columns
    for i in range(3):
        all_same = True
        for j in range(3):
            if board[j][i] != player:
                all_same = False
        
        if all_same:
            return True
    
    # Check diagonals
    diag_1 = board[0][0] == player and board[1][1] == player and board[2][2] == player
    diag_2 = board[0][2] == player and board[1][1] == player and board[2][0] == player

    if diag_1 or diag_2:
        return True
    
    return False


def is_game_over():
    if is_winner(PLAYER_1) or is_winner(PLAYER_2):
        return True
    
    for row in board:
        for item in row:
            if item is None:
                return False

    return True


def main():
    while True:
        print_board()
        player_move()
        if is_game_over():
            break
    
    if is_winner(PLAYER_1):
        print(f'Player {PLAYER_1} won!')
    elif is_winner(PLAYER_2):
        print(f'Player {PLAYER_2} won!')
    else:
        print('Game ove no one won! (tie)')


if __name__ == '__main__':
    main()
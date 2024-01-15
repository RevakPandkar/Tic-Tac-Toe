import random


def check_win(board, symbol):
    # Horizontally
    for row in board:
        if row.count(symbol) == 3:
            return True

    # Vertically
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == symbol:
            return True

    # Diagonally
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    else:
        return False


def evaluate_board(board):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1

    return 0


def board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False

    return True


def game_over(board):
    if check_win(board, "X") or check_win(board, "O") or board_full(board):
        return True

    return False


def minimax(board, is_maximizing):
    if game_over(board):
        return [evaluate_board(board), ()]

    best_move = ()

    if is_maximizing:
        best_value = -float('Inf')
        symbol = "X"
    else:
        best_value = float('Inf')
        symbol = "O"

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = symbol
                value = minimax(board, not is_maximizing)[0]
                board[i][j] = ' '

                if is_maximizing:
                    if value > best_value:
                        best_value = value
                        best_move = (i, j)
                else:
                    if value < best_value:
                        best_value = value
                        best_move = (i, j)

    return [best_value,best_move]


def print_board(board):
    print(f'{board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('----------')
    print(f'{board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('----------')
    print(f'{board[2][0]} | {board[2][1]} | {board[2][2]}')
    print('\n')


board = [[' '] * 3 for i in range(3)]
print(board)
playerTurn = True
moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

while not board_full(board):
    if playerTurn:
        symbol = "X"
        move = int(input('Enter your choice Player '))
        row = int((move - 1)/3)
        col = (move - 1) % 3

        if (row,col) in moves:
            moves.remove((row,col))
            playerTurn = not playerTurn
            board[row][col] = symbol
            print_board(board)
            if check_win(board,symbol):
                print('You win Player !!')
                exit()
        else:
            print_board(board)
            print('Oops Try Again')

    else:
        symbol = "O"
        best_move = minimax(board,False)[1]

        board[best_move[0]][best_move[1]] = symbol
        moves.remove(best_move)
        playerTurn = not playerTurn
        print_board(board)
        if check_win(board,symbol):
            print('Comp wins !!')
            exit()

else:
    print('Its a Tie')

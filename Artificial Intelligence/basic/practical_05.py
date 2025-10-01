#Name: Himanshu H. Jadhav
#Roll No. : SE-27
#Batch : S2
# Experiment No. 5 - Minimax Algorithm

import math

# Initial empty board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(b):
    for row in b:
        print('|'.join(row))
    print('-' * 5)

# Check if moves are available
def is_moves_left(b):
    return any(cell == ' ' for row in b for cell in row)

# Evaluate score
def evaluate(b):
    # Rows & Columns
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != ' ':
            return 10 if b[i][0] == 'X' else -10
        if b[0][i] == b[1][i] == b[2][i] != ' ':
            return 10 if b[0][i] == 'X' else -10

    # Diagonals
    if b[0][0] == b[1][1] == b[2][2] != ' ':
        return 10 if b[0][0] == 'X' else -10
    if b[0][2] == b[1][1] == b[2][0] != ' ':
        return 10 if b[0][2] == 'X' else -10

    return 0 

# Minimax algorithm
def minimax(b, depth, is_max):
    score = evaluate(b)
    if score != 0 or not is_moves_left(b):
        return score

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = 'X'
                    best = max(best, minimax(b, depth+1, False))
                    b[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = 'O'
                    best = min(best, minimax(b, depth+1, True))
                    b[i][j] = ' '
        return best

# Find best move for AI
def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'X'
                move_val = minimax(b, 0, False)
                b[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Example game loop (playable against user in command line)
def play_game():
    while True:
        print_board(board)
        if not is_moves_left(board) or evaluate(board) != 0:
            break

        row = int(input("Enter your move (row): "))
        col = int(input("Enter your move (col): "))

        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

        if is_moves_left(board) and evaluate(board) == 0:
            ai_move = find_best_move(board)
            board[ai_move[0]][ai_move[1]] = 'X'

    print_board(board)
    final_score = evaluate(board)
    if final_score == 10:
        print("AI Wins!")
    elif final_score == -10:
        print("You Win!")
    else:
        print("It's a Draw!")

play_game()
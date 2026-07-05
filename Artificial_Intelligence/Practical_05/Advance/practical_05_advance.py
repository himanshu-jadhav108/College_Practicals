import math
import matplotlib.pyplot as plt
import time

# Board
board = [[' ' for _ in range(3)] for _ in range(3)]

def plot_board(b):
    fig, ax = plt.subplots()
    for i in range(3):
        for j in range(3):
            ax.text(j+0.5, 2-i+0.5, b[i][j], fontsize=40, ha='center', va='center')
    ax.set_xlim(0,3)
    ax.set_ylim(0,3)
    ax.set_xticks(range(4))
    ax.set_yticks(range(4))
    ax.grid(True)
    plt.show()
    time.sleep(0.5)


def print_board(b):
    for row in b:
        print('|'.join(row))
    print('-' * 5)

def is_moves_left(b):
    return any(cell == ' ' for row in b for cell in row)

def evaluate(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != ' ':
            return 10 if b[i][0] == 'X' else -10
        if b[0][i] == b[1][i] == b[2][i] != ' ':
            return 10 if b[0][i] == 'X' else -10
    if b[0][0] == b[1][1] == b[2][2] != ' ':
        return 10 if b[0][0] == 'X' else -10
    if b[0][2] == b[1][1] == b[2][0] != ' ':
        return 10 if b[0][2] == 'X' else -10
    return 0

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

# Playable game
def play_game():
    while True:
        print_board(board)
        if not is_moves_left(board) or evaluate(board) != 0:
            break
        # Player move
        row = int(input("Enter your move (row 0-2): "))
        col = int(input("Enter your move (col 0-2): "))
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move!")
            continue
        # AI move
        if is_moves_left(board) and evaluate(board) == 0:
            ai_move = find_best_move(board)
            print(f"AI moves at {ai_move}")
            board[ai_move[0]][ai_move[1]] = 'X'
    print_board(board)
    score = evaluate(board)
    if score == 10:
        print("AI Wins!")
    elif score == -10:
        print("You Win!")
    else:
        print("Draw!")

play_game() 

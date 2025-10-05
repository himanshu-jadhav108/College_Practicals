import math

# Initialize empty board
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(b):
    print("\nBoard:")
    for row in b:
        print("|".join(cell if cell != ' ' else '_' for cell in row))
    print()

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

# Minimax with alpha-beta
def minimax(b, depth, is_max, alpha, beta):
    score = evaluate(b)
    if score != 0 or not is_moves_left(b):
        return score

    if is_max:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = 'X'
                    val = minimax(b, depth+1, False, alpha, beta)
                    b[i][j] = ' '
                    max_eval = max(max_eval, val)
                    alpha = max(alpha, val)
                    if beta <= alpha:
                        return max_eval
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = 'O'
                    val = minimax(b, depth+1, True, alpha, beta)
                    b[i][j] = ' '
                    min_eval = min(min_eval, val)
                    beta = min(beta, val)
                    if beta <= alpha:
                        return min_eval
        return min_eval

def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)

    print("\nAI is thinking...")
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'X'
                move_val = minimax(b, 0, False, -math.inf, math.inf)
                b[i][j] = ' '
                print(f"AI evaluates move ({i},{j}) = {move_val}")
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    print(f"AI chooses move {best_move} with value {best_val}\n")
    return best_move

def play_game():
    print_board(board)
    while True:
        if not is_moves_left(board) or evaluate(board) != 0:
            break

        # Player move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != ' ':
            print("Invalid! Try again.")
            continue
        board[row][col] = 'O'
        print_board(board)

        # AI move
        if is_moves_left(board) and evaluate(board) == 0:
            ai_move = find_best_move(board)
            board[ai_move[0]][ai_move[1]] = 'X'
            print(f"AI moves at {ai_move}")
            print_board(board)

    # Game result
    score = evaluate(board)
    if score == 10:
        print("AI Wins!")
    elif score == -10:
        print("You Win!")
    else:
        print("Draw!")

# Run game
if __name__ == "__main__":
    play_game()

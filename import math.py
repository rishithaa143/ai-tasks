import math

# Initialize the board
board = [" " for _ in range(9)]

# Print the board
def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Check for winner
def check_winner(player):
    win_combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_combos)

# Check if board is full
def is_full():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1  # AI wins
    elif check_winner("X"):
        return -1  # Human wins
    elif is_full():
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except:
            print("Please enter a valid number!")
            continue

        board[move] = "X"
        print_board()

        # Check if human won
        if check_winner("X"):
            print("🎉 You win!")
            break
        elif is_full():
            print("🤝 It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        best_move()
        print_board()

        # Check if AI won
        if check_winner("O"):
            print("😢 AI wins! Better luck next time.")
            break
        elif is_full():
            print("🤝 It's a draw!")
            break

# Run the game
if _name_ == "_main_":
    play_game()
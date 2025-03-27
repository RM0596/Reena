# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

# Function to check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Main game function
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Create an empty 3x3 board
    players = ["X", "O"]  # Two players: X and O
    turn = 0  # Start with player X (turn = 0)

    while True:
        print_board(board)  # Display the board
        current_player = players[turn % 2]  # Determine the current player
        print(f"Player {current_player}'s turn!")

        # Get valid move from the player
        while True:
            try:
                move = int(input(f"Enter a number (1-9) to place {current_player}: ")) - 1
                row, col = move // 3, move % 3
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell is already occupied, try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (tie game)
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the next player
        turn += 1

# Start the game
if __name__ == "__main__":
    tic_tac_toe()

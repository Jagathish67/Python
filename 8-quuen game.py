N = 8
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    for i in range(row):  
        if board[i][col]:  
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):  
        if board[i][j]:  
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):  
        if board[i][j]:  
            return False

    return True

def user_play():
    board = [[0] * N for _ in range(N)]
    placed_queens = 0

    print("Welcome to the 8-Queens Game! Place your queens one by one.")
    
    while placed_queens < N:
        print_board(board)
        try:
            row = int(input(f"Enter row (0-{N-1}) for queen {placed_queens + 1}: "))
            col = int(input(f"Enter column (0-{N-1}) for queen {placed_queens + 1}: "))

            if 0 <= row < N and 0 <= col < N and is_safe(board, row, col):
                board[row][col] = 1
                placed_queens += 1
            else:
                print("Invalid move! The queen is not safe or the position is out of bounds. Try again.")
        except ValueError:
            print("Invalid input! Enter numbers between 0 and 7.")

    print("\nFinal Board:")
    print_board(board)
    print("Congratulations! You've placed all 8 queens correctly.")

user_play()

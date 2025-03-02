def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    print("Welcome to XOX (Tic-Tac-Toe)!")
    print_board(board)

    while True:
        current_player = players[turn % 2]
        print(current_player,"'s turn.")

        try:
            row, col = input("Enter row and column (0-2, separated by space): ").split()
            row, col = int(row), int(col)

            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter numbers between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("Cell already occupied! Try again pls ")  
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print( current_player," wins! ")
                break

            if is_full(board):
                print("It's a draw!")
                break

            turn += 1
        except ValueError:
            print("Invalid input! Please enter two numbers b/w 0 and 2.")

    input("game over! press to exit.....")
if __name__ == "__main__":
    tic_tac_toe()

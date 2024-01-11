def print_board(board):
    for row in board:
        print(row)

def get_move(player):
    move = input(f"{player}, enter your move (row,column): ")
    row, col = move.split(",")
    return int(row) - 1, int(col) - 1

def check_win(board, player):
    for row in board:
        if all(square == player for square in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for col in range(3)] for row in range(3)]
    players = ["X", "O"]
    current_player = players[0]
    print_board(board)
    while True:
        row, col = get_move(current_player)
        board[row][col] = current_player
        print_board(board)
        if check_win(board, current_player):
            print(f"{current_player} wins!")
            break
        if all(square != " " for row in board for square in row):
            print("Tie!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

if __name__ == '__main__':
    tic_tac_toe()

def tic_tac_toe():
    board = [" " for _ in range(9)]

    def display_board():
        print("\n")
        print(f" {board[0]} | {board[1]} | {board[2]}")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]}")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]}")
        print()

    def check_winner(player):
        winning_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for position in winning_positions:
            if (
                board[position[0]] == player and
                board[position[1]] == player and
                board[position[2]] == player
            ):
                return True
        return False

    current_player = "X"
    moves = 0

    print("=" * 35)
    print("      TIC-TAC-TOE GAME")
    print("=" * 35)
    print("Board Positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print("\nType 'q' anytime to quit.\n")

    display_board()

    while True:
        choice = input(f"Player {current_player}, enter position (1-9) or 'q': ").strip()

        if choice.lower() == "q":
            print("\nGame Quit Successfully. Goodbye! 👋")
            break

        if not choice.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        position = int(choice)

        if position < 1 or position > 9:
            print("Invalid position. Choose 1 to 9.")
            continue

        if board[position - 1] != " ":
            print("Position already occupied. Try another one.")
            continue

        board[position - 1] = current_player
        moves += 1

        print("\nCurrent Game State:")
        display_board()

        if check_winner(current_player):
            print(f"🎉 Congratulations! Winner is '{current_player}' 🏆")
            break

        if moves == 9:
            print("🤝 It's a Draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


if __name__ == "__main__":
    tic_tac_toe()
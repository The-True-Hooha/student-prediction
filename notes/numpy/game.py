import numpy as np


class TicTacToe:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = 'X'

    def create_board(self):
        return np.array([[' ']*3 for _ in range(3)])

    def place_marker(self, position):
        row, col = position
        if self.board[row, col] == ' ':
            self.board[row, col] = self.current_player
            return True
        return False

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if (self.board[i, 0] == self.board[i, 1] == self.board[i, 2] != ' ' or
                    self.board[0, i] == self.board[1, i] == self.board[2, i] != ' '):
                return True
        if (self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != ' ' or
                self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != ' '):
            return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            print(self.board)
            row = int(
                input(f"Player {self.current_player}, enter row (0-2): "))
            col = int(
                input(f"Player {self.current_player}, enter column (0-2): "))

            if self.place_marker((row, col)):
                if self.check_winner():
                    print(self.board)
                    print(f"Player {self.current_player} wins!")
                    break
                if self.is_board_full():
                    print(self.board)
                    print("It's a tie!")
                    break
                self.switch_player()
            else:
                print("That position is already occupied. Try again.")


# Create and play the game
game = TicTacToe()
game.play_game()

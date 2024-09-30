from Board import Board
from Player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player(input("Name for Player 1 (X): "), 'X')
        self.player2 = Player(input("Name name for Player 2 (O): "), 'O')
        self.current_player = self.player1  # Start with Player 1

    def switch_player(self):
        # Switch between Player 1 and Player 2
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self):
        while True:
            # Display the board
            self.board.display()

            # Get input from the current player
            try:
                row = int(input(f"{self.current_player.get_name()}, Chose row to mark (0-2): "))
                col = int(input(f"{self.current_player.get_name()}, Chose column to mark (0-2): "))
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            # Update the board
            if self.board.update_board(row, col, self.current_player.get_symbol()):
                # Check for a winner
                if self.board.is_winner(self.current_player.get_symbol()):
                    self.board.display()
                    print(f"{self.current_player.get_name()} wins!")
                    break

                # Check for a draw
                if self.board.is_draw():
                    self.board.display()
                    print("The game is a draw!")
                    break

                # Switch to the next player
                self.switch_player()
            else:
                print("Try again!")

if __name__ == "__main__":
    game = Game()
    game.play()

class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        pass

    def display(self):
        print("    C0        C1        C2")
        # Loop through each row of the Tic Tac Toe board
        for i in range(3):  # Assuming a 3x3 board
            # Print the top part of each cell
            print("   _____ " * 3)

            print(f"R{i}", end='')
            # Print the middle part with the cell values
            for j in range(3):
                value = self.board[i][j] if self.board[i][j] is not None else ' '  # Use a space if the cell is empty
                print(f"|  {value}  |  ", end='')  # Print the value in the cell

            print()  # Move to the next line after printing the row

            # Print the bottom part of each cell
            print("  |_____|" * 3)

        print()  # Final new line after printing the entire board

        pass

    def update_board(self, row, col, player):
        # Validate the move
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Out of bounds.")
            return False
        if self.board[row][col] != ' ':
            print("Invalid move. Cell already taken.")
            return False

        # Update the board
        self.board[row][col] = player
        return True  # Move was successful

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
                all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False  # No winner

    def is_draw(self):
        # Check if the board is full and no winner
        if all(cell != ' ' for row in self.board for cell in row) and \
                not self.is_winner('X') and not self.is_winner('O'):
            return True
        return False  # Not a draw
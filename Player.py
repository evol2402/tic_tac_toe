class Player:
    def __init__(self, name, symbol):
        self.name = name  # Player's name
        self.symbol = symbol  # Player's symbol ('X' or 'O')

    def get_name(self):
        return self.name  # Return player's name

    def get_symbol(self):
        return self.symbol  # Return player's symbol

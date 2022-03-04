import random


class Player:
    def __init__(self, letter):
        # Letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Just pick a random box of those left to choose from.
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        chosen_value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                chosen_value = int(square)
                if chosen_value not in game.available_moves():
                    raise ValueError
                valid_square = True  # By now the choice is correct.
            except ValueError:
                print('Invalid square selection, try again.')
        return chosen_value

import random
import math


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


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # If Genius start, he just picks a random square.
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # choice based on minimax algorythm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        # Return best possible move, considering the outcome of every possible move.
        max_player = self.letter
        other_player = 'o' if self.letter == 'x' else 'x'
        # Recursive base case:
        if state.current_winner == other_player:
            # the score is our utility function: (empty squares + 1)*1 if max, *-1 if min.
            # (this is just a way of assigning value to the particular branch result)
            # We want to maximize the moves that make us win, and minimize those who make
            # the opponent win.
            return {'position': None, 'score': 1*(state.num_empty_squares() + 1) if
                    other_player == max_player else -1*(state.num_empty_squares() + 1)}
        # else if there are no empty squares to choose:
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        # Initialize dictionaries:
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # min possible score, anything would be bigger than this.
        else:
            best = {'position': None, 'score': math.inf}  # max possible score, anything would be smaller than this.
        # Starting recursion:
        for possible_move in state.available_moves():
            # 1) make a move, try that spot.
            state.make_move(possible_move, player)
            # 2) recurse using minimax, to simulate a game after making that move.
            sim_score = self.minimax(state, other_player)  # (other players turn)
            # 3) undo the move.
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # 4) update dictionaries if necessary.
            if player == max_player:  # maximizing the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:  # while minimizing the other_player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best


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

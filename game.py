from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # a 3x3 board to play
        self.current_winner = None

    def print_board(self):
        # To get the rows:
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Prints the numbers corresponding to each box in the board.
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # return a list of the available squares to choose from.
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If valid move: move and return True, else: return False.
        if self.board[square] == ' ':
            self.board[square] = letter
            # If this is a winning move, update current winner.
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Return True if there is a winner, False if there is not.
        # if 3 in a row:
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # if 3 in a column:
        column_ind = square % 3
        column = [self.board[column_ind+i*3]for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # if 3 in diagonal:
        diagonal1 = [self.board[i] for i in [0, 4, 8]]
        if all([spot == letter for spot in diagonal1]):
            return True
        diagonal2 = [self.board[i] for i in [2, 4, 6]]
        if all([spot == letter for spot in diagonal2]):
            return True
        return False


def play(game, x_player, o_player, print_game=True):
    # Returns the winner of the game, or None if a tie
    if print_game:
        game.print_board_nums()
    letter = 'x'  # x will begin.
    # while we still have empty squares:
    while game.empty_squares():
        # get move from the player in turn:
        if letter == 'x':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        # If the move was correctly executed, print the move on the board.
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
                return letter
        if letter == 'x':
            letter = 'o'
        else:
            letter = 'x'

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_p = HumanPlayer('x')
    o_p = GeniusComputerPlayer('o')
    t = TicTacToe()
    play(t, x_p, o_p)

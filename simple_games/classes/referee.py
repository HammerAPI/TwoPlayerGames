##
# This class models a Referee for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##
class Referee:

    def __init__(self, board, rules):
        """
        This class models a referee for a game.

        Args:
            board : The board of the game being played
            rules : The ruleset of the current game
        """
        self.board = board
        self.rules = rules

    def update_board(self, board, player, move):
        """
        This method updates the game board according to the game's ruleset.

        Args:
            board : The game board
            move : The move made
        """
        self.rules.update_board(board, player, move)

    def ask_for_move(self, player, board):
        """
        Retrieves a proposed move from the current player.

        Args:
            player : Player whose turn it is
            board : The game board

        Return:
            The players move, or None if the move failed.
        """

        # Ask for a move from the player
        proposed_move = player.move(board)

        # If the move was illegal, the player's move is None
        if not self.rules.is_legal(self.board, proposed_move):
            proposed_move = None

        # Return the move, which is either valid or None
        return proposed_move

    def is_game_over(self, board):
        """
        Checks to see if the game is over.

        Args:
            board : The game board

        Return:
            True if the game is over, else False.
        """
        return self.rules.is_game_over(board)

    def declare_winner(self, board, players, winner=None):
        """
        Declares a winner to the game and updates each player's win/loss counters.

        Args:
            board : The game board
            players : List of players in the game
            winner : (Optional) The winning player, if already decided

        Return:
            The winning player of the game
        """
        # If a winner was not already provided,
        # decide on a winner by the game's rules
        if winner is None:
            winner = self.rules.declare_winner(board, players)

        board.data["winner"] = winner.name

        # Get the loser, as well
        loser = players[0] if players[1] is winner else players[1]

        # Update winner and loser win/loss scores
        winner.wins += 1
        loser.losses += 1


        return winner

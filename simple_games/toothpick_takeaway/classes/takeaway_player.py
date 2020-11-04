##
# This class models a player for the Toothpick Takeaway game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Oct 7, 2020
##

class TakeawayPlayer:

    def __init__(self, player_name, strategy = lambda x: None):
        """ The player constructor

        Args:
            player_num : the player number in the game
            is_human : whether or not the player is human-controlled

        Return:
            None
        """
        self.player_name = player_name
        self.strategy = strategy

    def move(self, board):
        """ This function takes in a board and then allows the player to make
        a choice on the next move.

        Args:
            board : the board to move on

        Return:
            The move made (take 1 or 2 toothpicks)
        """

        move = self.strategy(board)

        return move
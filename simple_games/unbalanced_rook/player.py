##
# This class models a player for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Sep 22, 2020
##
class Player:

    def __init__(self, player_num):
        """ The player constructor

        Args:
            player_num : the player number in the game

        Return:
            None 
        """
        self.player_num = player_num

    def move(self, board):
        """ This function takes in a board and then allows the player to make
        a choice on the next move.

        Args:
            board : the board object for the current game

        Return:
            The move made.
        """
        pass
"""
This is a ConnectFiveGame class, which represents the model in the Connect 5
"Gomoku" game

Author: Kevin, Jacob
"""
from typing import List
class ConnectFiveGame:
    board: List[List[str]]
    P1 = 'X'
    P2 = 'O'
    row: int, col: int

    def __init__(self, controller : ConnectFiveController) -> None:
        """
        initialize a new ConnectFiveGame object

        == Precondition ==

        """
        self.controller = controller
        self.board = controller._board
        

    """
    Returns the opponent of player
    """
    def otherPlayer(self, player):
        if player == P1:
            return P2
        elif player == P2:
            return P1
        return None

    def alternation(self, row, col, drow, dcol):
        stopping = ' '
        while validCoordinate(row, col):
            if board[row][col] == ' ':
                return
            elif board[row][col] == stopping:
                return stopping
            else:
                stopping = otherPlayer(board[row][col])

            row += drow
            col += dcol

        return None

    
    def uniformChips (self, row : int, col : int, drow : int, dcol : int):
    """
    Return the player that has 5 in at this position in this position
    If neither then return None
    
    :param row: the row of the current position
    :param col: the col of the current position 
    :param drow: the vertical direction
    :param dcol: the horizontal direction
    """
        if (controller.get_chip(row, col) != ' '):
            current_chip = controller.get_chip(row, col)
            while controller.validCoordinate(row+drow, col+dcol):
                #TO DO : continue checking if the next chip equals the current chip
        return None
                
    
    def hasMove(self, str : player):
    """
    Checks if this player has a valid move on the board
    
    :param player: a player chip on the ConnectFiveBoard
    """
        row = 0
        col = 0
        for row in range(board.get_dimension):
            for col in range(board.get_dimension):
                if (controller.get_chip(row, num_to_alpha(col)) == ' '):
                    return True
        return False
        
    def getCount(self, player):
        count = 0
        for i in range(len(self.row)):
            for j in range(len(self.col)):
                if self.board[i][j] == player:
                    count += 1
        return count

    def checkWinner(self):
    """
    Check if there is a winner (i.e If a player has 5 chips in a row on the board)
    """
         for row in range(board.get_dimension):
            for col in range(board.get_dimension):
                for drow in range(2):
                    for dcol in range(2):
                        winner = uniformChips(row, col, drow, dcol)
                        if winner == "X":
                            return "X"
                        elif winner == "O":
                            return "O"


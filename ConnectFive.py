"""
<<<<<<< HEAD
This is a ConnectFiveController class, which represents the controller in the Connect 5
"Gomoku" game. I have checked all possible
=======
This is a ConnectFiveGame class, which represents the model in the Connect 5
"Gomoku" game
>>>>>>> refs/remotes/origin/master

Author: Kevin, Jacob
"""
from typing import List
class ConnectFiveGame:
    board : List[List[str]]
    P1 = 'X'
    P2 = 'O'

    def __init__(self, controller : object) -> None:
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
        if player == self.P1:
            return self.P2
        elif player == self.P2:
            return self.P1
        return None

    def alternation(self, row, col, drow, dcol):
        stopping = ' '
        while self.board.validCoordinate(row, col):
            if self.board[row][col] == ' ':
                return
            elif self.board[row][col] == stopping:
                return stopping
            else:
                stopping = self.otherPlayer(self.board[row][col])

            row += drow
            col += dcol

        return None

    
    def uniformChips(self, row:int, col:int, drow:int, dcol:int):
        """
        Return the player that has 5 in a row starting at position (row, col)
        in direction (drow, dcol)
        If neither player has 5 in a row then return None

        :param row: the row of the current position
        :param col: the col of the current position
        :param drow: the vertical direction
        :param dcol: the horizontal direction
        """
        if self.controller.get_chip(row, col) != ' ' and self.controller.validCoordinate(row, col):
            current_chip = self.controller.get_chip(row, col)
            count = 1
            # continue until edge of board is hit
            while self.controller.validCoordinate(row+drow, col+dcol):
                # get the next chip in drow, dcol direction
                next_chip = self.controller.get_chip(row+drow, col+dcol)
                # update counter if the next chip is the same as the current chip
                if current_chip == next_chip:
                    count += 1
                    current_chip = next_chip
                # the chip is not the same, check if an unbroken line of 5 of one chip
                else:
                    if count == 5:
                        return current_chip
                    else:
                        return None
            # edge has been reached, check unbroken line of 5 of one chip
            if count == 5:
                return current_chip
        return None
                
    
    def hasMove(self, player : str):
        """
        Checks if player has a valid move on the board

        :param player: a player chip on the ConnectFiveBoard
        """
        for row in range(self.board.get_dimension):
            for col in range(self.board.get_dimension):
                # player can move if there is an empty space
                if self.controller.get_chip(row, self.board.num_to_alpha(col)) == ' ':
                    return True
        return False
        
    def getCount(self, player):
        """
        Return how many chips of type player are on the board

        :param player:
        :return:
        """
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

<<<<<<< HEAD


=======
        for row in range(self.board.get_dimension):
            for col in range(self.board.get_dimension):
                for drow in range(-1, 2):
                    for dcol in range(-1, 2):
                        winner = self.uniformChips(row, col, drow, dcol)
                        if winner == "X":
                            return "X"
                        elif winner == "O":
                            return "O"
>>>>>>> refs/remotes/origin/master

    def isGameOver(self):
        """
        Return True iff the board is fulfilled all chips
        """
        for row in range(self.board.get_dimension):
            for col in range(self.board.get_dimension):
                winner = self.uniformChips(row,col,drow,dcol)
                if self.board[row][col] == " " or winner == None:
                    return True
        return False

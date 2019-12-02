"""
This is a ConnectFiveGame class, which represents the model in the Connect 5
"Gomoku" game

Author: Phan Trung Kien, Jacob
"""
from typing import List
from ConnectFiveBoard import ConnectFiveBoard

class ConnectFiveGame:
    board: ConnectFiveBoard
    P1 = 'X'
    P2 = 'O'

    def __init__(self, board : ConnectFiveBoard) -> None:
        """
        initialize a new ConnectFiveGame object

        == Precondition ==

        """
        self.board = board



    def otherPlayer(self, player):
        """
        Returns the opponent of player
        """
        if player == self.P1:
            return self.P2
        elif player == self.P2:
            return self.P1
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

        if self.board.get_chip(row, col) != " " and self.board.valid(row, col):
            # initialize the current chip we are comparing
            crnt_row = row
            crnt_col = col
            current_chip = self.board.get_chip(crnt_row, crnt_col)
            count = 1
            # continue until edge of board is hit
            while self.board.valid(crnt_row+drow, crnt_col + dcol):
                # get the next chip in drow, dcol direction that we want to compare
                next_chip = self.board.get_chip(crnt_row+drow, crnt_col + dcol)

                # update counter if the next chip is the same as the current chip
                #   and update the current chip we are comparing.
                if next_chip == current_chip:
                    count += 1
                    crnt_row = crnt_row + drow
                    crnt_col = crnt_col + dcol
                    current_chip = self.board.get_chip(crnt_row, crnt_col)
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


    def hasMove(self):
        """
        Checks if player has a valid move on the board

        :param player: a player chip on the ConnectFiveBoard
        """
        for row in range(self.board.get_dimension()):
            for col in range(self.board.get_dimension()):
                # player can move if there is an empty space
                if self.board.get_chip(row, col) == " ":
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

        for row in range(self.board.get_dimension()):
            for col in range(self.board.get_dimension()):
                for drow in range(-1, 2):
                    for dcol in range(-1, 2):
                        if drow != 0 or dcol != 0:
                            winner = self.uniformChips(row, col, drow, dcol)
                            if winner is not None:
                                return winner
        return None

    def isGameOver(self):
        """
        Return True if no player has a move or one of the
        players has 5 of their chips in an unbroken line on the board
        """

        winner = self.checkWinner()
        if self.hasMove() == False or winner != None:
            return True
        return False

    def move(self, row, col, player):
        """
        Place player chip at (row, col) on the board
        """
        self.board.place_token(player, row, col)



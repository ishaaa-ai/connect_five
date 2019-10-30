"""
This is a ConnectFiveController class, which represents the controller in the Connect 5
"Gomoku" game. I have checked all possible

Author: Kevin, Jacob
"""
from typing import List
class ConnectFiveBoard:
    dim: int
    board: List[List[str]]
    P1 = 'X'
    P2 = 'O'
    row: int, col: int

    def __init__(self, player, dim = 8) -> None:
        """
        initialize a new ConnectFiveBoard object

        == Precondition ==
        _dim is no bigger than 15

        :param dim: the dimension of the board (15 default)
        """

        self.dim = dim
        self.board = []
        self.player = player

    def Connect5Board(self):
        for i in range(len(dim)):
            for j in range(len(dim)):
                board[i][j] = ' '

        mid = dim /2
        board[mid-1][mid-1] = board[mid][mid] = P1
        board[mid][mid - 1] = board[mid - 1][mid] = P2

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


    def hasMove(self, row, col, drow, dcol):
        if get(row, col) == ' ':
            return alternation(row + drow, col + dcol, drow, dcol)
        else:
            return None

    def getCount(self, player):
        count = 0
        for i in range(len(self.row)):
            for j in range(len(self.col)):
                if self.board[i][j] == player:
                    count += 1
        return count

    def checkWinner(self):
        if self.getCount(P1) == 5:
            return P1
        elif self.getCount(P2) == 5:
            return P2
        return None




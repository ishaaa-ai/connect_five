"""
This is a ConnectFiveBoard class, which represents the board in the Connect 5
"Gomoku" game

Author: Michael Kwan
"""

from __future__ import annotations
from typing import Optional


class ConnectFiveBoard:
    """
    A connect five board

    == Private Attributes ==
    _grid: a _grid that represents the board
    _dim: the dimension of the square _grid (usually 15)
    _num_to_alpha: a dictionary associates numbers greater than 9 with english
                   alphabet characters explicitly defined for cleanliness
    _alpha_to_num: a dictionary that associates the letters a, b, c, d, e to
                   numbers greater than 9, explicitly defined for cleanliness
    """

    _dim: int
    _grid: list[list[str]]
    _num_to_alpha = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e"}
    _alpha_to_num = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14}

    def __init__(self, dim: int = 15) -> None:
        """
        initialize a new ConnectFiveBoard object

        == Precondition ==
        _dim is no bigger than 15

        :param dim: the dimension of the board (15 default)
        """
        self._dim = dim

        l1 = []
        l2 = []
        # make a _dim size list of spaces
        for x in range(dim):
            l1.append(" ")

        # make a list that has <_dim> number of <_dim> size lists
        for x in range(dim):
            l2.append(l1[:])
        # create an empty _grid
        self._grid = l2[:]

    def get_dimension(self) -> int:
        """
        Get the board's dimension
        :return: the dimension
        """
        return self._dim

    def get_chip(self, row, col) -> str:
        """
        Get the piece at a specific coordinate on the grid
        :return: the str at row,col
        """
        return self._grid[row][col]

    def valid_coordinate(self, row: int, col: int) -> bool:
        """
        validity check on the position
        :param row: row position
        :param col: column position
        :return: true if empty, false otherwise
        """

        if not (0 <= row < self._dim and 0 <= col < self._dim):  # out of bounds
            return False
        elif self._grid[row][col] == " ":
            return True
        else:
            return False

    def valid(self, row: int, col: int) -> bool:
        if not (0 <= row < self._dim and 0 <= col < self._dim):  # out of bounds
            return False
        return True
    
    def place_token(self, token: str, row: int, col: int) -> None:
        """
        Places a token on a position on the _grid

        == Precondition ==
        The row/col position is actually valid

        :param token: the token that represents the character (str length of 1)
        :param row: row position to place token
        :param col: column position to place token
        :return: None
        """

        if self.valid_coordinate(row, col):
            self._grid[row][col] = token


    def num_to_alpha(self, num: int) -> str:
        """
        Convert a number to the corresponding alphabetical character

        *Precondition*
        9 < num < 15

        :param num: the number to convert to an alphabetical character
        :return: the alphabetical character
        """

        return self._num_to_alpha[num]

    def alpha_to_num(self, alpha: str) -> int:
        """
        Convert an alphabetical character to a corresponding number

        *Precondition*
        alpha is a single character

        :param alpha: the alphabetical character to convert to a number
        :return: the number
        """

        return self._alpha_to_num[alpha]

    def __str__(self) -> str:
        """
        return a string representation of the object

        Grid design by Arnold Rosenbloom for the CSC207 Othello project,
        used with permission

        Permission Acquired via email
        Date: Monday October 21 2019
        Time: 8:17 PM

        :return: the string representation of the object
        """

        s = ""
        s += "  "
        for col in range(self._dim):
            if col < 10:  # print out number if not double digit
                s += str(col) + " "
            else:  # correspond the number to a letter instead
                s += self.num_to_alpha(col) + " "
        s += '\n'

        s += " +"
        for col in range(self._dim):
            s += "-+"

        s += '\n'

        for row in range(self._dim):
            if row < 10:  # print out number if not double digit
                s += str(row) + "|"
            else:  # correspond number to letter instead
                s += self.num_to_alpha(row) + "|"

            for col in range(self._dim):
                s += self._grid[row][col] + "|"

            if row < 10:  # print out number if not double digit
                s += str(row) + "\n"
            else:  # correspond number to letter instead
                s += self.num_to_alpha(row) + "\n"

            s += " +"
            for col in range(self._dim):
                s += "-+"

            s += '\n'

        s += "  "
        for col in range(self._dim):
            if col < 10:  # print out number if not double digit
                s += str(col) + " "
            else:  # correspond number to letter instead
                s += self.num_to_alpha(col) + " "

        s += '\n'
        return s


if __name__ == "__main__":  # testing
    a = ConnectFiveBoard(15)

    print(a)

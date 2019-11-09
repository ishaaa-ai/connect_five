"""
This is a ConnectFiveController class, which represents the controller in the Connect 5
"Gomoku" game
Author: Gauravdeep Setia
"""
from typing import Tuple
from ConnectFiveBoard import ConnectFiveBoard
from ConnectFive import ConnectFiveGame


class ConnectFiveController:

    _board: ConnectFiveBoard
    _game: ConnectFiveGame
    _player: str

    def __init__(self) -> None:
        """
        Initialize a new ConnectFiveController object
        Creates a ConnectFiveBoard object.
        """
        self._board = ConnectFiveBoard(15)
        self._game = ConnectFiveGame(self._board)
        self._player = "X"

    def get_move(self) -> Tuple[int, int]:
        """
        poop
        @return: the move
        """
        while True:
            print("The rows and columns are from 1-e")
            print("0,1,2,3,4,5,6,7,8,9,a,b,c,d,e")
            row = input("Row: ")
            col = input("Column: ")
            print("")

            if (row in ['a', 'b', 'c', 'd', 'e'] or (0 <= int(row) <= 9)) \
                    and (col in ['a', 'b', 'c', 'd', 'e'] or
                         (0 <= int(col) <= 9)):

                if row is str:
                    row = self._board.alpha_to_num(row)
                else:
                    row = int(row)
                if col is str:
                    col = self._board.alpha_to_num()
                else:
                    col = int(col)

                if self._board.valid_coordinate(row, col):
                    return row, col
                else:
                    print("Invalid move, try again")
                    print("")
            else:
                print("Invalid input, try again")
                print("")

    def player_turn(self) -> str:
        """
        Returns the player ("X" or "O") whose turn it currently is.
        ~ Isha Kerpal
        """
        msg = "It is player: " + self._game.otherPlayer(self._player) + "'s turn."

        return msg

    def return_board(self):
        """
        Returns a string representation of the updated board.
        ~ Isha Kerpal
        """
        return "Board: " + self._board.__str__()

    def check_move(self) -> bool:
        """
        Checks if the current player has any move currently on the board.
        Returns True if the player has a move.
        Returns False if the player doesn't have a move anywhere on the board.
        Disclaimer : Method hasMove(player) in the ConnectFiveBoard class
                    ( in ConnectFive.py) will be implemented later.

        ~ Isha Kerpal
        """
        if self._game.hasMove(self._player):
            return True
        return False

    def play(self):
        """
        idk
        :return:
        """

        while self._game.isGameOver():
            self.return_board()
            self.player_turn()
            move = self.get_move()
            self._game.move(move[0], move[1], self._player)
            self._player = self._game.otherPlayer(self._player)

        print(self._game.checkWinner())




if __name__ == "__main__":
    """
    Runs only for the first two games. (Needs to be modified)
    """
    c = ConnectFiveController()
    c.play()
    # # Prints the board after it has been modified with the new move.
    # # ~ Isha Kerpal
    # print(c.return_board())
    # # Prints which player's turn it is
    # # ~ Isha Kerpal
    # print(c.player_turn())
    # if c.check_move():
        #c.get_move()


"""
This is a ConnectFiveController class, which represents the controller in the
Connect 5 "Gomoku" game.
Author: Gauravdeep Setia, Isha Kerpal
"""
from typing import Tuple

from ConnectFive import ConnectFiveGame
from ConnectFiveBoard import ConnectFiveBoard


class ConnectFiveController:
    _board: ConnectFiveBoard
    _game: ConnectFiveGame
    _player: str

    def __init__(self) -> None:
        """
        Initialize a new ConnectFiveController object.
        Creates a ConnectFiveBoard object.

        @return: None
        """
        self._board = ConnectFiveBoard(15)
        self._game = ConnectFiveGame(self._board)
        self._player = "X"

    def get_move(self) -> Tuple[int, int]:
        """
        Prompts the user to input a row and column on the board where
        they want to make the move.

        @return: A tuple with the row and column on the board where
        the user makes a move.
        """
        while True:
            print("The rows and columns are from 1-e")
            print("0,1,2,3,4,5,6,7,8,9,a,b,c,d,e")

            row = input("Row: ")
            col = input("Column: ")

            print("")

            if len(row) > 0 and len(col) > 0 and (row in
                                                  ['a', 'b', 'c', 'd', 'e'] or (
                                                          0 <= int(row) <= 9)) \
                    and (col in ['a', 'b', 'c', 'd', 'e'] or
                         (0 <= int(col) <= 9)):

                if row in ['a', 'b', 'c', 'd', 'e']:
                    row = self._board.alpha_to_num(row)
                else:
                    row = int(row)
                if col in ['a', 'b', 'c', 'd', 'e']:
                    col = self._board.alpha_to_num(col)
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
        @return: The player ("X" or "O") whose turn it currently is.
        """
        print("It is player: " + self._player + "'s turn.")

    def return_board(self):
        """
        @return: String representation of the updated board.
        """
        print("Board: \n" + self._board.__str__())

    def check_move(self) -> bool:
        """
        Checks if the current player has any move currently on the board.

        @return: True if the player has a move.
                 False if the player doesn't have a move anywhere on the board.
        """
        if self._game.has_move():
            return True
        return False

    def play(self):
        """
        Makes use of the get_move method and makes adjustments to the board
        and the game according to the move made by the user.

        @return: None
        """

        while not self._game.is_game_over():
            self.return_board()
            self.player_turn()
            if self.check_move():
                move = self.get_move()
                self._game.move(move[0], move[1], self._player)
                self._player = self._game.other_player(self._player)

        winner = self._game.check_winner()
        if winner is None:
            self.return_board()
            print("No player wins because no player got 5 chips in a row.")
        else:
            self.return_board()
            print(winner + " is the winner.")

        input("The game is done, press enter to exit.")


if __name__ == "__main__":
    """
    Makes a ConnectFiveController object and starts a new game.
    """
    c = ConnectFiveController()
    c.play()

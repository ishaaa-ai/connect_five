"""
This is a ConnectFiveController class, which represents the controller in the Connect 5
"Gomoku" game

Author: Gauravdeep Setia
"""
from typing import Tuple
from ConnectFiveBoard import ConnectFiveBoard


class ConnectFiveController:

    _board: ConnectFiveBoard()

    def __init__(self) -> None:
        """
        Initialize a new ConnectFiveController object
        Creates a ConnectFiveBoard object.
        """
        self._board: ConnectFiveBoard(15)

    def get_move(self) -> Tuple[str, str]:
        """

        """

        while True:
            try:
                print("The rows and columns are from 1-e")
                print("0,1,2,3,4,5,6,7,8,9,a,b,c,d,e")
                row = input("Row: ")
                col = input("Column: ")
                print("")

                if (row in ['a', 'b', 'c', 'd', 'e'] or (0 <= int(row) <= 9)) \
                        and (col in ['a', 'b', 'c', 'd', 'e'] or
                             (0 <= int(col) <= 9)):
                    if self._board.valid_coordinate(row, col):
                        return row, col
                    else:
                        print("Invalid move, try again")
                        print("")
                else:
                    print("Invalid input, try again")
                    print("")

            except:
                print("Invalid input, try again")
                print("")


if __name__ == "__main__":
    c = ConnectFiveController()

    c.get_move()







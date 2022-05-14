from __future__ import annotations
import numpy as np
from typing import Tuple, List


class Board:
    
    def __init__(self, x_dim: int, y_dim: int):
        self.__values = np.zeros(x_dim * y_dim).reshape(x_dim, y_dim)
        self.__temp_values = self.__values.copy()
    
    def getBoard(self) -> List[List[int]]:
        return self.__values

    def updateBoard(self) -> Board:
        self.__values = self.__temp_values.copy()
        return self

    def partialUpdate(self, cordination: Tuple[int, int], new_value: int) -> Board:
        self.__temp_values[cordination] = new_value

    def _forceSetValues(self, cordination: Tuple[int, int], new_value) -> Board:
        '''
        Warning. You are going to directly change the
        board values itself. 
        Make sure you know what you are doing.
        If you want to pre-update the board partially,
        use Board.partialUpdate() instead.
        '''
        self.__values[cordination] = new_value
        self.__temp_values[cordination] = new_value
        return self

    def __str__(self) -> str:
        return ' ' + str(self.__values)[1:-1]

    def calculateNeighbors(self, cordination: Tuple[int, int]) -> int:

        n_neighbors = 0
        x, y = cordination
        x_min, x_max = max(x-1, 0), min(x+1, len(self.__values[0]))
        y_min, y_max = max(y-1, 0), min(y+1, len(self.__values))
        for i in range(x_min, x_max+1):
            for j in range(y_min, y_max+1):
                if (i, j) == (x, y):
                    continue
                if self.__values[i, j] > 0: # isAlive
                    n_neighbors += 1

        return n_neighbors

    def handleFuture(self, cordination: Tuple[int, int], n_neighbors: int) -> Board:

        if self.__values[cordination] > 0: # isAlive

            if n_neighbors < 2 or n_neighbors > 3:
                self.__temp_values[cordination] = 0 # Dies
        else: # isDead

            if n_neighbors == 3:
                self.__temp_values[cordination] = 1 # getsAlive

        return self

    def iterate(self):
        '''
        Iterate once.
        '''
        xs, ys = np.where(self.getBoard() > 0)

        x_min, x_max = max(min(xs) - 1, 0), min(max(xs) + 1, 10)
        y_min, y_max = max(min(ys) - 1, 0), min(max(ys) + 1, 10)

        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max + 1):
                cordination = (x, y)
                n_neighbors = self.calculateNeighbors(cordination)
                self.handleFuture(cordination, n_neighbors)

        self.updateBoard()


def main():

    board = Board(10, 10)

    ### Initial values, Must be implemented in UI.

    for i in range(1, 4):
        j = 1
        cordination = (i, j)
        board._forceSetValues(cordination, 1)
    
    ### End of Initial values

    print(board)
    board.iterate()
    print()
    print(board)
    board.iterate()
    print()
    print(board)
    


if __name__ == '__main__':
    main()
        
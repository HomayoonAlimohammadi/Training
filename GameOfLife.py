from __future__ import annotations
from time import sleep
import numpy as np
from typing import Tuple, List
import pygame
import sys


class Board:
    
    def __init__(self, x_dim: int, y_dim: int):
        self.__values = np.zeros(x_dim * y_dim).reshape(x_dim, y_dim)
        self.x_dim = x_dim
        self.y_dim = y_dim
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
        x_min, x_max = max(x-1, 0), min(x+1, self.x_dim)
        y_min, y_max = max(y-1, 0), min(y+1, self.y_dim)
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

        x_min, x_max = max(min(xs) - 1, 0), min(max(xs) + 1, self.x_dim)
        y_min, y_max = max(min(ys) - 1, 0), min(max(ys) + 1, self.y_dim)

        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max + 1):
                cordination = (x, y)
                n_neighbors = self.calculateNeighbors(cordination)
                self.handleFuture(cordination, n_neighbors)

        self.updateUI((x_min, x_max), (y_min, y_max))
        self.updateBoard()

    def updateUI(self, xs: Tuple[int, int], ys: Tuple[int, int]) -> None:
        drawBaseGrid()
        x_min, x_max = xs
        y_min, y_max = ys
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max + 1):
                if self.__values[x, y] == 1:
                    rect = pygame.Rect(x * blockSize, y * blockSize, 
                                    blockSize, blockSize)
                    pygame.draw.rect(SCREEN, WHITE, rect, blockSize)



def main():

    board = Board(WINDOW_WIDTH//blockSize, WINDOW_HEIGHT//blockSize)

    ### Initial values, Must be implemented in UI.

    # for i in range(3, 5):
    #     for j in range(3, 5):
    #         cordination = (i, j)
    #         board._forceSetValues(cordination, 1)
    # for i in range(5, 7):
    #     for j in range(5, 7):
    #         cordination = (i, j)
    #         board._forceSetValues(cordination, 1)

    cordination = (2, 4)
    board._forceSetValues(cordination, 1)
    cordination = (4, 4)
    board._forceSetValues(cordination, 1)
    cordination = (4, 5)
    board._forceSetValues(cordination, 1)
    cordination = (3, 5)
    board._forceSetValues(cordination, 1)
    cordination = (3, 6)
    board._forceSetValues(cordination, 1)

    ### End of Initial values
    board.updateUI((0, board.x_dim-2), (0, board.y_dim-2))
    for i in range(50):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() 
        sleep(0.1)
        board.iterate()   

        
    

def drawBaseGrid():
    SCREEN.fill(BLACK)
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
blockSize = 20 #Set the size of the grid block

pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
drawBaseGrid()

if __name__ == '__main__':
    main()



        
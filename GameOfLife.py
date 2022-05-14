import numpy as np
from typing import Tuple


class Board:
    pass


def calculateNeighbors(cordination: Tuple[int, int], board: Board) -> int:
    pass

def handleFuture(cordination: Tuple[int, int], n_neighbors: int) -> bool:
    pass

board = np.zeros(100).reshape(10, 10)

board[2:5, 2:7] = 3
print(board)

xs, ys = np.where(board > 0.5)

x_min, x_max = max(min(xs) - 1, 0), min(max(xs) + 1, 10)
y_min, y_max = max(min(ys) - 1, 0), min(max(ys) + 1, 10)


old_board = board.copy()
for x in range(x_min, x_max+1):
    for y in range(y_min, y_max + 1):
        cord = (x, y)
        n_neighbors = calculateNeighbors(cord, old_board)
        isAlive = handleFuture(cord, n_neighbors)
        

print(board)
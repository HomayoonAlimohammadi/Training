from typing import List, Tuple
from sympy import flatten


def calculate_max_fresh_time(grid: List[List[int]]) -> int:
    """Return number of days until all the oranges are
    going to rot. Given a grid with following properties:
    `0`: empty cell
    `1`: fresh orange
    `2`: rotten orange
    Return -1 if impossible.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    days = 0
    bombs = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                bombs.append((row, col))

    old_bombs = bombs.copy()
    while old_bombs:
        bombs = []
        rot = False
        while old_bombs:
            row, col = old_bombs.pop()
            for r, c in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if (
                    0 <= row + r < n_rows
                    and 0 <= col + c < n_cols
                    and grid[row + r][col + c] == 1
                    and (row + r, col + c) not in bombs
                ):
                    grid[row + r][col + c] = 2
                    bombs.append((row + r, col + c))
                    rot = True

        days += rot
        old_bombs = bombs.copy()

    return days if 1 not in flatten(grid) else -1


grid = [
    [2, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1],
]
# assert calculate_max_fresh_time(grid) == -1

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
assert calculate_max_fresh_time(grid) == 4

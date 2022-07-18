from functools import lru_cache
from typing import List
from math import comb


class Solution:
    def uniquePath(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)

    def uniquePaths_recursive(self, m: int, n: int) -> int:
        @lru_cache
        def dfs(r, c):

            if r == m - 1 and c == n - 1:
                return 1

            go_right, go_down = 0, 0
            if r != m - 1:
                go_right = dfs(r + 1, c)

            if c != n - 1:
                go_down = dfs(r, c + 1)

            return go_right + go_down

        return dfs(0, 0)

    def uniquePaths_dynamic(self, m: int, n: int) -> int:

        board = [[0] * n] * m
        print(board)
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    board[r][c] = 1
                else:
                    try:
                        right = board[r][c + 1]
                    except IndexError:
                        right = 0

                    try:
                        down = board[r + 1][c]
                    except IndexError:
                        down = 0

                    board[r][c] = right + down

        return board[0][0]

    def uniquePaths_optimal_dynamic(self, m: int, n: int) -> int:

        row = [1] * n
        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row

        return row[0]


def print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        print(row)


def unique_paths(m: int, n: int) -> int:
    grid = []
    for row_idx in range(m):
        row = []
        for col_idx in range(n):
            row.append(0)
        grid.append(row)
    grid[m - 1][n - 1] = 1
    for row in range(m - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            print(row, col)
            right, down = 0, 0
            if 0 <= row + 1 < len(grid):
                down = grid[row + 1][col]
            if 0 <= col + 1 < len(grid[0]):
                right = grid[row][col + 1]
            grid[row][col] += right + down
            print_grid(grid)
            print()
    return grid[0][0]


# func = Solution().uniquePaths_optimal_dynamic
# print(func(3, 7))

m, n = 3, 7
print(unique_paths(m, n))

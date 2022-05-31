from functools import lru_cache
from typing import List
from math import comb

class Solution:

    def uniquePath(self, m: int, n: int) -> int:
        return comb(m+n-2, m-1)

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
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c == n-1:
                    board[r][c] = 1
                else:
                    try:
                        right = board[r][c+1]
                    except IndexError:
                        right = 0

                    try:
                        down = board[r+1][c]
                    except IndexError:
                        down = 0

                    board[r][c] = right + down

        return board[0][0]

    def uniquePaths_optimal_dynamic(self, m: int, n: int) -> int:

        row = [1] * n
        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n-2, -1, -1):
                new_row[j] = new_row[j+1] + row[j]
            row = new_row

        return row[0]
                
func = Solution().uniquePaths_optimal_dynamic
print(func(3, 7))
                
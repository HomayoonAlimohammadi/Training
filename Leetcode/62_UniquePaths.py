from typing import List


class Solution:

    def uniquePath(self, m: int, n: int) -> int:

        def dfs(coor, d, r, cache):
            if coor == (m-1, n-1):
                cache[(d, r)] = ...
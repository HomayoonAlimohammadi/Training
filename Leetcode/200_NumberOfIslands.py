from typing import List
from collections import deque


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        # def agglomerate(node_coordination, island, grid):
        #     if node_coordination in seen:
        #         return island
        #     i, j = node_coordination
        #     if i > 0 and grid[i - 1][j] == '1' and (i-1, j) not in island:
        #         island = agglomerate((i-1, j), island + [(i-1, j)], grid)
        #     if j > 0 and grid[i][j-1] == '1' and (i, j-1) not in island:
        #         island = agglomerate((i, j-1), island + [(i, j-1)], grid)
        #     if i < len(grid)-1 and grid[i + 1][j] == '1' and (i+1, j) not in island:
        #         island = agglomerate((i+1, j), island + [(i+1, j)], grid)
        #     if j < len(grid[0])-1 and grid[i][j+1] == '1' and (i, j+1) not in island:
        #         island = agglomerate((i, j+1), island + [(i, j+1)], grid)

        #     return island

        if not grid:
            return 0

        def visit(node_coordination):
            i, j = node_coordination
            if i > 0 and grid[i - 1][j] == '1' and (i-1, j) not in seen:
                seen.add((i-1, j))
                visit((i-1, j))
            if j > 0 and grid[i][j-1] == '1' and (i, j-1) not in seen:
                seen.add((i, j-1))
                visit((i, j-1))
            if i < len(grid)-1 and grid[i + 1][j] == '1' and (i+1, j) not in seen:
                seen.add((i+1, j))
                visit((i+1, j))
            if j < len(grid[0])-1 and grid[i][j+1] == '1' and (i, j+1) not in seen:
                seen.add((i, j+1))
                visit((i, j+1))

        def bfs(coor):
            q = deque()
            q.append(coor)     
            directions = [(0,0), (1,0), (-1, 0), (0,1), (0,-1)]       
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in seen):
                        q.append((r, c))
                        seen.add((r, c))
                
        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        for i in range(rows):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in seen:
                    bfs((i,j))
                    # visit((i,j))
                    num_islands += 1

        return num_islands


grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
func = Solution().numIslands
print(func(grid))
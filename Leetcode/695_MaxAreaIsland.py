from typing import List 


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid)) or \
                not (0 <= c < len(grid[0])) or \
                grid[r][c] == 0 or \
                (r, c) in seen:
                return 0
            seen.add((r, c))
            return 1 + area(r-1, c) + area(r+1, c) + \
                    area(r, c-1) + area(r, c+1)
        
        areas = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                areas.append(area(r, c))
        return max(areas)

    def maxAreaIterative(self, grid):
        seen = set()
        maxArea = 0
        for r0, row in range(len(grid)):
            for c0, val in range(len(grid[0])):
                if (r0, c0) in seen:
                    continue
                seen.add((r0, c0))
                stack = [(r0, c0)]
                shape = 0
                while stack:
                    stack.pop()
                    shape += 1
                    for nr, nc in ([r0-1, c0], [r0+1, c0], [r0, c0+1]
                                    [r0, c0-1]):
                                    if not (0 <= nr < len(grid)) or \
                                        not (0 <= nc < len(grid[0])) or \
                                        grid[nr][nc] == 0 or \
                                        (nr, nc) in seen:
                                        seen.add((nr, nc))
                                        stack.append([nr, nc])
                maxArea = max(shape, maxArea)
                

func = Solution().maxAreaOfIsland
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(func(grid))
func2 = Solution().maxAreaIterative 
print(func(grid))
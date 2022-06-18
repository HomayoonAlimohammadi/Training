from typing import List, Set, Tuple


class Solution:
    '''Class containing functions solving the problem.'''

    def max_area_of_island(self, grid: List[List[int]]) -> int:
        '''Calculate max area amongst all islands in a grid.'''

        seen: Set[Tuple[int, int]] = set()
        def area(row: int, col: int) -> int:
            if not (0 <= row < len(grid) 
                    and 0 <= col < len(grid[0])
                    and grid[row][col] == 1
                    and (row, col) not in seen):
                        return 0
            seen.add((row, col))
            
            return 1 + area(row-1, col) + area(row+1, col) + \
                area(row, col+1) + area(row, col-1)

        max_area = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_area = max(max_area, area(row, col))
        
        return max_area




from typing import List
import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        for i in range(len(board)):
            print(f'{i=}')
            row = list(board[i,:])
            print('Row: ',row)
            while '.' in row:
                del row[row.index('.')]
            
            col = list(board[:,i])
            print('Column: ', col)
            while '.' in col:
                del col[col.index('.')]
                
            print('Row nums: ',row)
            print('Col nums: ',col)
            print()
                
            if len(col) != len(set(col)):
                return 'false'
            if len(row) != len(set(row)):
                return 'false'
            
        for i in range(0,9,3):
            for j in range(0,9,3):
                boardSubSet = list(board[i:i+3,j:j+3].flatten())
                print(boardSubSet)
                while '.' in boardSubSet:
                    del boardSubSet[boardSubSet.index('.')]
                if len(boardSubSet) != len(set(boardSubSet)):
                    return 'false'
                    
        return 'true'
    
    
S = Solution()
board = [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
ans = S.isValidSudoku(board)
print(ans)
        
from typing import List
import numpy as np
from collections import defaultdict


class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            
            l = board[i][:]
            while '.' in l:
                l.remove('.')
            
            if len(l) != len(set(l)):
                return False
        
        board = np.array(board)
        board = np.transpose(board)
        for i in range(9):
            
            l = list(board[i,:])
            
            while '.' in l:
                l.remove('.')
                
            if len(l) != len(set(l)):
                return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                l = list(board[i:i+3,j:j+3].flatten())
                while '.' in l:
                    l.remove('.')

                if len(l) != len(set(l)):
                    return False

    
        return True


sol = Solution1()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["2",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))


class Solution2:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                if val == '.':
                    continue

                if (val in rows[i] or 
                    val in cols[j] or 
                    val in squares[i//3, j//3]):

                    return False

                rows[i].add(val)
                cols[j].add(val)
                squares[i//3, j//3].add(val)

        return True


sol = Solution2()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["2",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))


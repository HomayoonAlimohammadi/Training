from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            
            l = board[i][:]
            while '.' in l:
                l.remove('.')
            
            if len(l) != len(set(l)):
                return False
                        
        for i in range(9):
            
            l = [board[j][i] for j in range(9)]
            
            while '.' in l:
                l.remove('.')
                
            if len(l) != len(set(l)):
                return False

        
            
        return True


sol = Solution()
board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))
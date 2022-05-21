from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> List[int]:

        if target < matrix[0][0] or \
            target > matrix[-1][-1]:
            # return 'Not found!'
            return False

        start, end = 0, len(matrix)
        temp_num = None
        while True:

            index = (start + end) // 2
            curr = matrix[index][0]

            if temp_num == curr:
                break

            if curr == target:
                # return [index, 0]
                return True
            if curr > target:
                end = index
            elif curr < target:
                start = index
            
            temp_num = curr

        row_index = index

        start, end = 0, len(matrix[0])
        temp_num = None
        while True:

            index = (start + end) // 2
            curr = matrix[row_index][index]

            if temp_num == curr:
                break

            if curr == target:
                # return [row_index, index]
                return True
            if curr > target:
                end = index
            elif curr < target:
                start = index
            
            temp_num = curr

        # return 'Not found'
        return False


sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60], [61, 70, 80, 90]]
target = 90
print(sol.searchMatrix(matrix, target))

            

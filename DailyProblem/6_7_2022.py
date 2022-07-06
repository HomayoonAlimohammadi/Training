from typing import List


def solution(matrix: List[List[int]]) -> int:

    least_matrix = [matrix[0]]
    for row_idx in range(1, len(matrix)):
        least_row = []
        for k_house in range(len(matrix[0])):
            price = matrix[row_idx][k_house] + min(
                least_matrix[-1][:k_house] + least_matrix[-1][k_house + 1 :]
            )
            least_row.append(price)
        least_matrix.append(least_row)

    return min(least_matrix[-1])


matrix = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
print(solution(matrix))

matrix = [[1, 2, 3], [1, 4, 6]]
print(solution(matrix))

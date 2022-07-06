from typing import List


def solution(matrix: List[List[int]]) -> int:

    if len(matrix) == 0:
        return 0

    least_matrix = [matrix[0]]
    for row_idx in range(1, len(matrix)):
        least_row = []

        first_least = min(least_matrix[-1])
        first_least_idx = least_matrix[-1].index(first_least)
        second_least = min(
            least_matrix[-1][:first_least_idx] + least_matrix[-1][first_least_idx + 1 :]
        )

        for k_house in range(len(matrix[0])):

            least_before = first_least
            if least_matrix[-1][k_house] == least_before:
                least_before = second_least

            price = matrix[row_idx][k_house] + least_before
            least_row.append(price)
        least_matrix.append(least_row)

    return min(least_matrix[-1])


matrix = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
print(solution(matrix))

matrix = [[1, 2, 3], [1, 4, 6]]
print(solution(matrix))

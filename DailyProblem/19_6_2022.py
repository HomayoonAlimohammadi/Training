"""
Given a list of numbers, calculate another list in which
i_th element is the product of all numbers in the list except
the original i_th element.
"""

from functools import reduce
from typing import List


def solution_1(input_nums: List[int]) -> List[int]:
    """Calculate the result list via the first solution."""

    result: List[int] = []
    prod: int = reduce(lambda x, y: x * y, nums)
    for num in input_nums:
        try:
            replacement = int(prod / num)

        except ZeroDivisionError:
            replacement = prod
        result.append(replacement)

    return result


def solution_2(input_nums: List[int]) -> List[int]:
    """Calculate the result list via the second solution."""

    result: List[int] = [1] * len(input_nums)
    prod = 1
    for i, _ in enumerate(result):
        result[i] *= prod
        prod *= input_nums[i]

    prod = 1
    for i in range(len(result) - 1, -1, -1):
        result[i] *= prod
        prod *= input_nums[i]

    return result


nums: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(solution_1(nums))
print(solution_2(nums))

nums: List[int] = [2, 3, 4]

print(solution_1(nums))
print(solution_2(nums))

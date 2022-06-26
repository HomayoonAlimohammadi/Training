from typing import List
from functools import lru_cache


def solution(nums: List[int]) -> int:
    @lru_cache
    def calculate_sum(idx: int, partial_sum: int = 0, max_sum: int = 0) -> int:

        if idx >= len(nums):
            return max_sum

        max_sum = max(max_sum, partial_sum + nums[idx])
        single_step = calculate_sum(idx + 2, partial_sum + nums[idx], max_sum)
        double_step = calculate_sum(idx + 3, partial_sum + nums[idx], max_sum)

        max_sum = max(max_sum, single_step, double_step)
        return max_sum

    return max(calculate_sum(0), calculate_sum(1))


nums = [2, 4, 6, 2, 5]
max_sum = solution(nums)
print(max_sum)

nums = [5, 1, 1, 5]
max_sum = solution(nums)
print(max_sum)

nums = [5]
max_sum = solution(nums)
print(max_sum)

nums = []
max_sum = solution(nums)
print(max_sum)

nums = [1, 2]
max_sum = solution(nums)
print(max_sum)

nums = [1, 3, 1]
max_sum = solution(nums)
print(max_sum)

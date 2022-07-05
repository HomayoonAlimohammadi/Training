from typing import List
from collections import deque


def solution(nums: List[int], k: int) -> List[int]:
    max_list = deque()

    for i in range(k):
        if not max_list:
            max_list.append(nums[i])
            continue

        while max_list and nums[i] > max_list[-1]:
            max_list.pop()

        max_list.append(nums[i])

    result = [max_list[0]]

    for i in range(k, len(nums)):
        while max_list and nums[i] > max_list[-1]:
            max_list.pop()

        max_list.append(nums[i])

        if max_list[0] == nums[i - k]:
            max_list.popleft()

        result.append(max_list[0])

    return result


nums = [10, 5]
k = 2
print(solution(nums, k))

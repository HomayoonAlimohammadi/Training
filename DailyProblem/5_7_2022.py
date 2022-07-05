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


def solution_better(nums: List[int], k: int) -> List[int]:
    q = deque()
    max_values = []

    for i, num in enumerate(nums):

        while q and q[-1] < num:
            q.pop()

        q.append(num)

        if i >= k and q[0] == nums[i - k]:
            q.popleft()

        if i >= k - 1:
            max_values.append(q[0])

    return max_values


nums = [10, 5]
k = 2
print(solution(nums, k))

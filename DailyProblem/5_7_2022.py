from typing import List


def solution(nums: List[int], k: int) -> List[int]:
    counter = {}
    for i in range(k):
        counter[nums[i]] = counter.get(nums[i], 0) + 1

    max_list = [max(counter.keys())]
    for i in range(k, len(nums)):
        counter[nums[i]] = counter.get(nums[i], 0) + 1
        counter[nums[i - k]] -= 1
        if counter[nums[i - k]] == 0:
            del counter[nums[i - k]]

        max_list.append(max(counter.keys()))

    return max_list


nums = [10, 5, 2, 7, 8, 7]
k = 3
print(solution(nums, k))

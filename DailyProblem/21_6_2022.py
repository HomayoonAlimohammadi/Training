from typing import List


def find_smallest_integer(nums: List[int]) -> int:
    """Return smallest integer not available in a sequence"""
    for i in range(1, len(nums)):
        while i > 0 and nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1

    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > start + 1:
            return start + 1
        start = nums[i]


nums = [3, 4, -1, 1]
print(find_smallest_integer(nums))

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            return 1

        has_end_of_len = False

        for i in range(len(nums)):
            target = int(str(nums[i]).split("*")[0])
            if target == len(nums):
                has_end_of_len = True
            if 0 <= target < len(nums):
                nums[target] = str(nums[target]) + "*"

        print(nums)
        for i in range(1, len(nums)):
            if not isinstance(nums[i], str):
                return i

        if has_end_of_len:
            return len(nums) + 1
        return len(nums)

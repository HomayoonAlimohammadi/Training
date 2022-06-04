from typing import List
from collections import deque


class Solution:

    def canJump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        rec = [0] * len(nums)
        pos, goal = len(nums) - 2, len(nums) - 1

        while pos >= 0:
            if nums[pos] >= goal - pos:
                new = 1
            else:
                new = min(rec[pos+1: pos+nums[pos]+1]) + 1
            rec[pos] = new
            pos -= 1

        return rec


func = Solution().canJump
nums = [2,3,1,1,4]
print(func(nums))

from typing import List
from collections import deque


class Solution:

    def canJump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        rec = [0] * len(nums)
        pos, goal = len(nums) - 2, len(nums) - 1

        while pos >= 0:
            if nums[pos] >= goal - pos:
                new = 1
            else:
                if nums[pos] == 0:
                    new = float('inf')
                else:
                    new = min(rec[pos+1: pos+nums[pos]+1]) + 1
            rec[pos] = new
            pos -= 1

        return rec[0]


func = Solution().canJump
nums = [2,3,1,1,4]
print(func(nums))

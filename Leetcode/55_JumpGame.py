from typing import List


class Solution:

    def canJump_bili(self, nums: List[int]) -> bool:

        def jump(idx: int) -> bool:

            if idx >= len(nums) or nums[idx] == 0:
                return False

            if idx == len(nums) - 1:
                return True

            results = []
            for i in range(1, nums[idx]+1):
                results.append(jump(idx + i))

            return any(results)

        return jump(0)

    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        def jump(idx: int) -> bool:

            if idx >= len(nums):
                return False

            if idx == len(nums) - 1:
                return True

            if nums[idx] == 0:
                return False

            for i in range(min(len(nums) - idx, nums[idx]), 0, -1):
                if jump(idx + i):
                    return True

            return False

        return jump(0)


func = Solution().canJump
nums = [2,3,1,1,4]
nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
nums = [0]
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(func(nums))
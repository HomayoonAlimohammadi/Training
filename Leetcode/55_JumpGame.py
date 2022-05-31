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


func = Solution().canJump_bili
nums = [3,2,1,0,4]
nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
print(func(nums))
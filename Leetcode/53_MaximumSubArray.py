from typing import List


class Solution:

    def maxSubArray_false(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        MAX = sum(nums)
        SUM = sum(nums)
        while l < r:
            
            print(l, r, sum(nums[l:r+1]), MAX)
            if nums[r] > nums[l]:
                SUM -= nums[l]
                MAX = max(MAX, SUM)
                l += 1
            else:
                SUM -= nums[r]
                MAX = max(MAX, SUM)
                r -= 1

        return MAX

    def maxSubArray(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     return nums[0]

        curr_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            if curr_sum <= 0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum
            

func = Solution().maxSubArray
nums = [-1, -2]
print(func(nums))
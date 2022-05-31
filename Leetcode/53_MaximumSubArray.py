from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        
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
            

func = Solution().maxSubArray
nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
print(func(nums))
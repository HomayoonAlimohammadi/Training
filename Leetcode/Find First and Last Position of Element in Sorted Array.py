from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            first = nums.index(target)
            last = len(nums) - nums[::-1].index(target) - 1
            return [first, last]
        except:
            return [-1, -1]
        
        
S = Solution()
nums = [0,0,0,0,1,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10,11,11]
target = 0
ans = S.searchRange(nums, target)
ans
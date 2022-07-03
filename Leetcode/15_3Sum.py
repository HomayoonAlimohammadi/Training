from typing import List
from random import randint
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                triple_sum = nums[i] + nums[j] + nums[k]
                
                if triple_sum == 0:
                    results.append([nums[i] , nums[j] , nums[k]])
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                    j += 1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
                elif triple_sum > 0:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
            
                else:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            i += 1
            while i < len(nums)- 2 and nums[i] == nums[i-1]:
                i += 1
                    
            return results
                    
    
S = Solution()
# nums = [-1,0,1,2,-1,4]
nums=[randint(-1e+5,1e+5) for i in range(3000)]
S.threeSum(nums)
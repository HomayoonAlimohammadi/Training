from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
        
S = Solution()
nums = [1,2,3,4]
target = 0
ans = S.search(nums,target)
print(ans)
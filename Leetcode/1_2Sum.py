from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i in range(len(nums)):
            
            left = target - nums[i]
            if left in hashmap:
                result = [min(i, hashmap[left])+1, max(i, hashmap[left])+1]
                return result

            hashmap[nums[i]] = i

        return False


sol = Solution()
nums = [-1, 0]
target = -1
print(sol.twoSum(nums, target))


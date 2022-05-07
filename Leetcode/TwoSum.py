from typing import List

### Solution Number 1

class Solution1:

    def twoSums(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)-1):
            compliment = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == compliment:
                    return [i, j]


### Solution Number 2

class Solution2:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment == nums[i]:
                continue
            exists = hashmap.get(compliment)
            if exists and hashmap[compliment] != i:
                return [i, hashmap[compliment]]

### Solution Number 3

class Solution3:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i in range(len(nums)):
            first = nums[i]
            
            compliment = target - first
            exists = hashmap.get(compliment)

            if exists != None:
                return [i, hashmap[compliment]]

            hashmap[first] = i 

            print(i, exists, hashmap)


sol = Solution3()

nums = [2,7,11,15]
target = 9
sol.twoSum(nums, target)
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        hashmap = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                hashmap[nums[i]+nums[j]] = hashmap.get(nums[i]+nums[j], []) + [[i,j]]

        results = []
        for i in range(len(nums)):
            left =  0 - nums[i]
            if left in hashmap:
                couples = hashmap[left]
                for couple in couples:
                    if i in couple:
                        continue
                    a, b = couple
                    k1 = min(nums[a], nums[b], nums[i])
                    k3 = max(nums[a], nums[b], nums[i])
                    k2 = 0 - (k1 + k3)

                    if [k1, k2, k3] not in results:
                        results.append([k1, k2, k3])

        return results


sol = Solution()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
print(sol.threeSum(nums))
a = [[-1, 0, 1], [-1, -1, 2], [-2, -1, 3], [-3, -1, 4], [-2, 0, 2], [-4, 0, 4], [-3, 0, 3], [-3, 1, 2], [-4, 1, 3]]
print(len(a), len(expected))
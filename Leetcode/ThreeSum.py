from typing import List
from collections import Counter


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


class Solution2:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        results = []
        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1

            while j < k:

                Sum = nums[i] + nums[j] + nums[k]

                if Sum == 0:

                    results.append([nums[i], nums[j], nums[k]])
                    k -= 1

                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif Sum > 0:
                    k -= 1

                else:
                    j += 1

        return results


class Solution3:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        cnt = Counter(nums)
        sortedNums = sorted(cnt)
        hashmap = {}
        for i in range(len(sortedNums)):
            for j in range(len(sortedNums)):
                hashmap[sortedNums[i]+sortedNums[j]] = \
                    hashmap.get(sortedNums[i]+sortedNums[j], []) + [[i, j]]

        for i in range(len(nums)):
            pass

        raise NotImplementedError



sol = Solution2()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
nums_2 = [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]

expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
result = sol.threeSum(nums)
print('result', result)
print('expected', expected)
print(len(result), len(expected))
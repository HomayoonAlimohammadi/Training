from typing import List, Tuple
from itertools import combinations


class Solution:

    def subsets(self, nums: List[int]) -> List[Tuple[int]]:
        '''
        Return all possible subsets of a list.
        '''
        results = []
        for i in range(len(nums)+1):
            results += combinations(nums, i)

        return results

    def subsets_manual(self, nums: List[int]) -> List[List[int]]:
        '''
        Return all possible subsets of a list
        Use binary combinations
        '''
        def filter_comb(nums: List[int], num: int, comb: str) -> List[int]:
            idx = nums.index(num)
            return int(comb[idx])

        results = []
        for i in range(2 ** len(nums)):
            comb = bin(i)[2:].zfill(len(nums))
            result = list(filter(lambda num: filter_comb(nums, num, comb), nums))
            results.append(result)

        return results


        



nums = [1,2,3]
subsets = Solution().subsets_manual(nums)
print(subsets)
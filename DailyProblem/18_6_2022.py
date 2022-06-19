from typing import List, Set 


class Solution:
    def add_up(self, nums: List[int], k: int) -> bool:
        '''
        Return a boolean representing whether 
        any two numbers in a given list add up to k
        '''

        hashmap: Set[int] = set()
        for num in nums:
            if k - num in hashmap:
                return True 
            hashmap.add(num)

        return False


nums: List[int] = [10, 15, 3, 7]
k = 17
func = Solution().add_up
print(func(nums, k))
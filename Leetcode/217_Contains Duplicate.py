from typing import List


class Solution1:

    def containsDuplicate(self, nums: List[int]):

        return len(set(nums)) != len(nums)


class Solution2:

    def containsDuplicate(self, nums: List[int]):

        hashmap = {}
        for element in nums:
            if hashmap.get(element) != None:
                return True

            hashmap[element] = 1

        return False
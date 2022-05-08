from typing import List
from collections import Counter


class Solution1:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        return [tup[0] for tup in counter.most_common(k)]


sol = Solution1()
nums = [1,1,1,2,2,3]
k = 2
print('Solution 1:', sol.topKFrequent(nums, k))


class Solution2:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        k_most_frequest = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)[:k]
        return [tup[0] for tup in k_most_frequest]


sol = Solution2()
nums = [1,1,1,2,2,3]
k = 2
print('Solution 2:', sol.topKFrequent(nums, k))
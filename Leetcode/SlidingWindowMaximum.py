from typing import List
import unittest
from time import time
import bisect
from collections import deque
from SlidingWindowMaximumTestCase import nums_ans, nums_input


class Solution1:

    def maxSlidingWindow(self, nums: List[int], k: int) -> int:
        
        if k == 1:
            return nums

        window = sorted(nums[:k])
        max_values = []
        max_values.append(window[-1])
        for i in range(k, len(nums)):
            old = nums[i-k]
            old_index = window.index(old)
            window.pop(old_index)
            new = nums[i]
            bisect.insort(window, new)
            max_values.append(window[-1])

        return max_values


class Solution2:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        max_values = []

        for i, num in enumerate(nums):

            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(i)

            if q[0] <= i-k:
                q.popleft()

            if i >= k-1:
                max_values.append(nums[q[0]])

        return max_values

class Test(unittest.TestCase):

    def setUp(self):
        self.func = Solution2().maxSlidingWindow

    def test_solution_2(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        ans = self.func(nums, k)
        expected = [3,3,5,5,6,7]
        self.assertEqual(ans, expected)

        nums = nums_input
        k = 50000
        ans = self.func(nums, k)
        expected = nums_ans
        self.assertEqual(ans, expected)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
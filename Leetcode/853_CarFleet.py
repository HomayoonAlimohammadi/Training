from typing import List
import unittest


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        records = [
            (pos, spd) for pos, spd in zip(position, speed)
        ]
        
        records.sort(key=lambda x: x[0])
        
        for i in range(len(records)):
            records[i] = (target - records[i][0])/records[i][1]
            
        stack = []
        for record in records:
            while stack and record >= stack[-1]:
                stack.pop()
                
            stack.append(record)
        
        return len(stack)


class TestCases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution().carFleet

    def test_solution_1(self):
        target = 12
        position = [10,8,0,5,3]
        speed = [2,4,1,1,3]
        ans = self.sol(target, position, speed)
        expected = 3
        self.assertEqual(ans, expected)

        target = 100
        position = [0,2,4]
        speed = [4,2,1]
        ans = self.sol(target, position, speed)
        expected = 1
        self.assertEqual(ans, expected)

        target = 10
        position = [3]
        speed = [3]
        ans = self.sol(target, position, speed)
        expected = 1
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
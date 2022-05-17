from typing import List
import unittest


class Solution1:

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        MAP = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: x / y,
            '*': lambda x, y: x * y
        }
        for token in tokens:
            if token in MAP:
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                result = int(MAP[token](operand_1, operand_2))
                stack.append(result)
            else:
                stack.append(token)

        return int(stack.pop())


class TestCases(unittest.TestCase):

    def setUp(self):
        self.solution_1 = Solution1().evalRPN

    def test_solution_1(self):
        tokens = ['2', '1', '+', '3', '*']
        ans = self.solution_1(tokens)
        expected = 9
        self.assertEqual(ans, expected)

        tokens = ["4","13","5","/","+"]
        ans = self.solution_1(tokens)
        expected = 6
        self.assertEqual(ans, expected)

        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        ans = self.solution_1(tokens)
        expected = 22
        self.assertEqual(ans, expected)

        tokens = ['1']
        ans = self.solution_1(tokens)
        expected = 1
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
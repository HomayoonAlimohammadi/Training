import unittest


class Solution1:

    def isValid(self, s: str) -> bool:

        stack = []
        MAP = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack or stack[-1] != MAP[char]:
                    return False
                stack.pop()

        return len(stack) == 0


class TestCases(unittest.TestCase):

    def setUp(self):
        self.solution_1 = Solution1().isValid

    def test_solution_1(self): 
        s = '()'
        ans = self.solution_1(s)
        expected = True
        self.assertEqual(ans, expected)

        s = '()[]{}'
        ans = self.solution_1(s)
        expected = True
        self.assertEqual(ans, expected)

        s = '(]'
        ans = self.solution_1(s)
        expected = False
        self.assertEqual(ans, expected)

        s = '({(}))'
        ans = self.solution_1(s)
        expected = False
        self.assertEqual(ans, expected)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
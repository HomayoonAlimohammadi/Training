from collections import Counter
import unittest


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if s == t:
            return s

        minSub = s * 2
        start, end = 0, 1
        cnt_ref = Counter(t)
        while end <= len(s):
            substring = s[start: end]
            # print('substring:', substring)
            cnt_sub = Counter(substring)
            # print(len(cnt_ref - cnt_sub))
            # print()
            while len(cnt_ref - cnt_sub) == 0 and start <= end:
                if len(substring) < len(minSub):
                    # print(f'minSub updated from {minSub} to {substring}')
                    minSub = substring
                substring = s[start: end]
                # print('substring:', substring)
                # print(len(cnt_ref - cnt_sub))
                # print()
                cnt_sub = Counter(substring)
                start += 1
            end += 1
        
        if minSub == 2 * s:
            return ''
        return minSub


class Tests(unittest.TestCase):

    def setUp(self):
        self.func = Solution().minWindow

    def test_examples(self):
        s = 'ADOBECODEBANC'
        t = 'ABC'
        self.assertEqual(self.func(s, t), 'BANC')

        s = 'a'
        t = 'a'
        self.assertEqual(self.func(s, t), 'a')
        
        s = 'a'
        t = 'aa'
        self.assertEqual(self.func(s, t), '')
        
        s = 'ab'
        t = 'b'
        self.assertEqual(self.func(s, t), 'b')
        
        s = 'abc'
        t = 'ac'
        self.assertEqual(self.func(s, t), 'abc')
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()
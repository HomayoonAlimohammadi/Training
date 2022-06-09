from functools import lru_cache 


class Solution:
    def longestValidParantheses(self, s: str) -> int:

        @lru_cache
        def process(s: str) -> int:
            stack = []
            for letter in s:
                if letter == '(':
                    stack.append('(')
                else:
                    if len(stack) == 0:
                        return False
                    stack.pop()

            return len(stack) == 0 

        max_len = 0
        for i in range(len(s) - 1):
            for j in range(i+2, len(s)+1, 2):
                sub_s = s[i:j]
                # print(sub_s, i, j)
                if process(sub_s):
                    max_len = max(max_len, j-i)

        return max_len 


func = Solution().longestValidParantheses
# print(func('((())') == 4)
# print(func('(()') == 2)
# print(func(')()())') == 4)
# print(func('') == 0)
print(func("()(()"))
            




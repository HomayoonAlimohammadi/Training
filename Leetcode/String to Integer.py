class Solution:
    def myAtoi(self, s: str) -> int:
        result = ''
        if len(s) == 0:
            return 0
        while len(s) != 0:
            if s[0] == ' ':
                s = s[1:]
                continue
            break
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+':
            result += s[0]
            s = s[1:]
        while len(s) != 0:
            if not s[0].isdigit():
                    break
            else:
                result += s[0]
                s = s[1:]
        nums = [num for num in list(result) if num.isdigit()]
        if len(nums) == 0:
            return 0
        result = int(result)
        if result > 2**31 - 1:
            result = 2**31 - 1
        elif result < -2**31:
            result = -2**31
        return result
    
S = Solution()

s = '3248293847'
print(S.myAtoi(s))
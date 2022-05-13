class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0: return 0
        start, end = 0, 1
        maxLen = 1
        while end < len(s):
            substring = s[start: end+1]
            len_sub = len(substring)
            if len_sub == len(set(substring)):
                if maxLen < len_sub:
                    maxLen = len_sub
                end += 1
            else: start += 1

        return maxLen
        
        
    
    
sol = Solution()
s = '1'
print(sol.lengthOfLongestSubstring(s))
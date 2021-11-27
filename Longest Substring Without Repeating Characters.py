class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_len = 0
        for char in s:
            if char in substring:
                substring = substring[substring.find(char)+1:] + char
            else:
                substring += char
            if len(substring) > max_len:
                max_len = len(substring)
        return max_len

class Solution:

    def isPalindrome(self, s: str) -> bool:

        s_purged = ''.join(list(filter(lambda char: char.isalpha() or char.isdigit(), s))).lower()
        
        if s_purged == s_purged[::-1]:
            return True

        return False


sol = Solution()
s = 'A man, a plan, a canal: Panama'
print(sol.isPalindrome(s))

        

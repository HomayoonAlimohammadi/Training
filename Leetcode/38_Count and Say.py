class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.say(self.countAndSay(n-1))
        
    def say(self, nums):
        if nums == '1':
            return '11'
        
        result = ''
        i = 1
        ref = nums[0]
        for num in nums[1:]:
            if num == ref:
                i += 1
            else:
                result += str(i) + ref
                ref = num
                i = 1
        result += str(i) + ref
        return result
        
        
        
        
S = Solution()
n = 5
ans = S.countAndSay(n)
print(ans)
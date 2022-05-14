from collections import Counter


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_ref = Counter(s1)
        start, end = 0, 1
        while end <= len(s2):
            cnt_sub = Counter(s2[start: end])
            if cnt_sub == cnt_ref:
                return True
            elif len(cnt_sub - cnt_ref) == 0:
                end += 1
            else:
                start += 1

        return False


class Solution1:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cnt_ref = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            substring = s2[i: i+len(s1)]
            cnt_sub = Counter(substring)
            if cnt_sub == cnt_ref:
                return True
        return False


sol = Solution1()
s1 = 'adc'
s2 = 'dcda'
print(sol.checkInclusion(s1, s2))
                
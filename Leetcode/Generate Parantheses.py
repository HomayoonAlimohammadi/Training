from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        for i in range(2**(2*n)):
            candid = format(i,'b').zfill(2*n)
            if candid.count('1') != len(candid)//2:
                continue
            can_org = candid
            while True:
                j = candid.find('10')
                if j == -1:
                    break
                candid = candid[:j] + candid[j+2:]
            if candid != '':
                continue
            candid = can_org
            final = ''
            for j in candid:
                if j == '1':
                    final += '('
                else:
                    final += ')'
            results.append(final)
        return results
    
S = Solution()
n = 3
ans = S.generateParenthesis(n)
print(ans)
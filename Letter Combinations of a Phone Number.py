from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':list('abc'),'3':list('def'),'4':list('ghi'),
              '5':list('jkl'),'6':list('mno'),'7':list('pqrs'),'8':list('tuv'),
              '9':list('wxyz')}
        if len(digits) == 0:
            return []
        nums = list(digits)
        results = ['']
        for num in nums:
            temp = []
            for part in results:
                for add in dic[num]:
                    temp.append(part+add)
            results = temp[:]
            
        return results
                    
            
        
        
S = Solution()
digits = '234'
S.letterCombinations(digits)
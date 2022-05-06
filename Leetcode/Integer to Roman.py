class Solution:
    def intToRoman(self, num: int) -> str:
        chunks = [1000,500,100,50,10,5,1]
        marks = ['M', 'D','C','L','X','V','I']
        result = ''
        i = 0
        while i < len(chunks):
            left = num
            if 900 <= left < 1000:
                result += 'CM'
                num -= 900
            elif 400 <= left < 500:
                result += 'CD'
                num -= 400
            elif 90 <= left < 100:
                result += 'XC'
                num -= 90
            elif 40 <= left < 50:
                result += 'XL'
                num -= 40
            elif left == 9:
                result += 'IX'
                num -= 9
            elif left == 4:
                result += 'IV'
                num -= 4
            else:
                rep = num // chunks[i]
                result += rep * marks[i] 
                num %= chunks[i]
            i += 1
        return result
    
S = Solution()

num = 1546
print(S.intToRoman(num))
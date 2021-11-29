class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines = [''] * numRows
        index = 0
        flag = True
        
        if numRows == 1:
            return s
        
        if numRows == 2:
            for i in range(len(s)):
                lines[i%2] += s[i]
        else:
            for i in range(0, len(s), 2*numRows - 2):
                # Zig:
                for j in range(numRows):
                    lines[j] += s[index]
                    index += 1
                    if index == len(s):
                        flag = False
                        break

                # Zag:
                for hope in range(numRows - 2, 0,-1):
                    for k in range(numRows):
                        if k == hope:
                            lines[k] += s[index]
                            index += 1
                        else:
    #                         lines[k] += ' '
                            lines[k] += ''
                        if index == len(s):
                            flag = False
                            break
                if not flag:
                    break
                    
        result = ''
        for line in lines:
#             result += line + '\n'
            result += line
        return result

S = Solution()

s = 'PAYPALISHIRING'
numRows = 4
ans = S.convert(s, numRows)
from typing import List


class Solution1:

    def generateParantheses(self, string: List[str], num_opening: int,
                            num_closing: int,total_len: int, results: List[str]=None):

        if num_closing == total_len and num_closing == num_opening:
            results.append(string)
            return string

        if num_opening < total_len:
            self.generateParantheses(string+'(', num_opening+1, num_closing, total_len, results)
        
        if num_closing < total_len and num_closing < num_opening:
            self.generateParantheses(string+')', num_opening, num_closing+1, total_len, results)
        
        return results

class Solution2:

    def generateParantheses(self, n: int) -> List[str]:

        results = []
        for i in range(2**(2*n)):
            candid = format(i, 'b').zfill(2 * n)
            if candid.count('0') != candid.count('1'):
                continue
            candid_org = candid
            open_num = 0
            close_num = 0
            while candid:
                if close_num > open_num:
                    break
                if candid[0] == '1':
                    open_num += 1
                    candid = candid[1:]

                elif candid[0] == '0':
                    close_num += 1
                    candid = candid[1:]
            else:
                result = ''
                for char in candid_org:
                    if char == '0':
                        result += ')'
                    elif char == '1':
                        result += '('
                results.append(result)

        return results


n = 3
print('Solution 1')
sol = Solution1()
string = ''
print(sol.generateParantheses(string, 0, 0, n, []))

print('Solution 2')
sol = Solution2()
print(sol.generateParantheses(n))

print(set())
class Solution:

    def removeDuplicate(self, string: str) -> str:

        i = 0
        while i < len(string)-1:
            print(string)
            print(i)
            if string[i] == string[i+1]:
                string = string[:i] + string[i+2:]
                if i > 0:
                    i -= 1
                continue
            i += 1

        return string


sol = Solution()
string = "aaaaaaaaaaaa"
print(sol.removeDuplicate(string))

            


            

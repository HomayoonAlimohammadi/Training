from typing import List


class Solution:

    def extractValues(self, pack: List) -> List[int]:
        
        index = 0
        while index < len(pack):

            current = pack[index]
            if isinstance(current, list):
                for element in current:
                    pack.append(element)
                pack = pack[:index] + pack[index+1:]

            else:
                index += 1

        return pack


sol = Solution()
pack = ['salam', 1, 2, ['nested', ['another', 0, ['prize']], 10], 100]
print(sol.extractValues(pack))
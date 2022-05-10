from typing import List


class Solution:

    def encode(self, strs: List[str]) -> List[str]:

        result = []
        for word in strs:
            enc_word = ''
            for char in word:
                enc_word += chr(128 - ord(char))

            enc_word = enc_word[::-1]
            result.append(enc_word)

        result.reverse()

        result = '£'.join(result)

        return result

    def decode(self, strs: List[str]) -> List[str]:

        strs = strs.split('£')

        strs.reverse()
        result = []
        for word in strs:
            dec_word = ''
            reversed = word[::-1]
            for char in reversed:
                dec_word += chr(128 - ord(char))

            result.append(dec_word)

        return result


sol = Solution()
strs = ['salam', 'homayoon']
enc = sol.encode(strs)
print(enc)
print(len(enc))
dec = sol.decode(enc)
print(dec)
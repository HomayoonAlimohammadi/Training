from collections import Counter


class Solution1:

    def validAnagram(self, s: str, t: str) -> bool:

        hashmap_s = {}
        for letter in s:
            hashmap_s[letter] = hashmap_s.get(letter, 0) + 1

        hashmap_t = {}
        for letter in t:
            hashmap_t[letter] = hashmap_t.get(letter, 0) + 1

        if hashmap_s == hashmap_t:
            return True

        return False


class Solution2:

    def validAnagram(self, s: str, t: str) -> bool:

        t = list(t)

        for letter in s:
            try:
                t.remove(letter)
            except ValueError as e:
                return False

        return len(t) == 0


class Solution3:

    def validAnagram(self, s: str, t: str) -> bool:

        hashmap_s = {}
        for letter in s:
            hashmap_s[letter] = hashmap_s.get(letter, 0) + 1

        for letter in t:

            letter_in_s = hashmap_s.get(letter, 0) 
            if letter_in_s == 0:
                return False

            hashmap_s[letter] -= 1

        if any(hashmap_s.values()):
            return False

        return True

        
class Solution4:

    def validAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)

            
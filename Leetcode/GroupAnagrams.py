from typing import List
from collections import Counter


def hash_counter(counter: Counter):

    result = ''
    list_items = sorted(counter.items(), key=lambda x: x[0])
    for key, value in list_items:
        result += str(key) + str(value)

    return hash(result)
    

class Solution1:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:
            hashmap[hash_counter(Counter(word))] = \
                hashmap.get(hash_counter(Counter(word)), []) + [word]
            

        return list(hashmap.values())


s = Solution1()
strs = ["eat","tea","tan","ate","nat","bat"]
print('Solution 1:', s.groupAnagrams(strs))  


class Solution2:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:

            sorted_word = ''.join(sorted(word))
            hashmap[sorted_word] = hashmap.get(sorted_word, []) + [word]

        return list(hashmap.values())


s = Solution2()
strs = ["eat","tea","tan","ate","nat","bat"]
print('Solution 2:', s.groupAnagrams(strs))  
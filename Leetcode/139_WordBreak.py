from typing import List
from functools import lru_cache
from collections import deque


def solution(word: str, word_list: List[str]) -> bool:
    @lru_cache
    def search_combination(string: str) -> bool:

        if len(string) == string.count("*"):
            return True

        for word in word_list:
            if word in string:
                word_idx = string.index(word)
                string_editted = (
                    string[:word_idx] + "*" + string[word_idx + len(word) :]
                )

                if search_combination(string_editted):
                    return True

        return False

    return search_combination(word)


def solution_dp(word: str, word_list: List[str]) -> bool:

    possibilities = deque([word])
    while possibilities:
        candid = possibilities.popleft()
        if len(candid) == 0:
            return True
        for word in word_list:
            if candid.startswith(word):
                new_pos = candid[len(word) :]
                if len(new_pos) == 0:
                    return True
                if new_pos not in possibilities:
                    possibilities.append(new_pos)

    return False


word = "catsandogs"
word_list = ["cats", "and", "dogs", "an"]
# print(solution_dp(word, word_list))

word = "applepenapple"
word_list = ["apple", "pen"]
# print(solution_dp(word, word_list))

word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
word_list = [
    "a",
    "aa",
    "aaa",
    "aaaa",
    "aaaaa",
    "aaaaaa",
    "aaaaaaa",
    "aaaaaaaa",
    "aaaaaaaaa",
    "aaaaaaaaaa",
]
print(solution_dp(word, word_list))

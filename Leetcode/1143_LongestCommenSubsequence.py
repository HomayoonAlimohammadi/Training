from collections import deque


def longest_common_subsequence(string1: str, string2: str) -> str:
    def find_longest(string1: str, string2: str, subseq: str = "") -> str:
        if not string1:
            return subseq

        pick_first = ""
        if string1[0] in string2:
            new_string2 = string2[string2.index(string1[0]) + 1 :]
            pick_first = find_longest(string1[1:], new_string2, subseq + string1[0])
        dont_pick_first = find_longest(string1[1:], string2, subseq)
        if len(pick_first) >= len(dont_pick_first):
            return pick_first
        return dont_pick_first

    return find_longest(string1, string2)


def longest_common_subsequence_dynamic(string1: str, string2: str) -> str:
    grid = []
    for i in range(len(string1) + 1):
        row = [0 for _ in range(len(string2) + 1)]
        grid.append(row)

    for i in range(len(string1) - 1, -1, -1):
        for j in range(len(string2) - 1, -1, -1):
            if string1[i] == string2[j]:
                grid[i][j] = grid[i + 1][j + 1] + 1
            else:
                grid[i][j] = max(grid[i + 1][j], grid[i][j + 1])
    return grid[0][0]


def longest_common_subsequence_opt(string1: str, string2: str) -> str:
    def find_longest(string1: str, string2: str) -> int:
        if not string1 or not string2:
            return 0

        if string1[0] == string2[0]:
            return find_longest(string1[1:], string2[1:]) + 1
        else:
            return max(
                find_longest(string1[1:], string2), find_longest(string1, string2[1:])
            )

    return find_longest(string1, string2)


string1 = "abc"
string2 = "adc"
print(longest_common_subsequence_opt(string1, string2))

string1 = "abcde"
string2 = "ace"
print(longest_common_subsequence_opt(string1, string2))

string1 = "abcdefg"
string2 = "abcdefg"
print(longest_common_subsequence_opt(string1, string2))

string1 = "abc"
string2 = "abc"
print(longest_common_subsequence_opt(string1, string2))


string1 = "a"
string2 = "d"
print(longest_common_subsequence_opt(string1, string2))

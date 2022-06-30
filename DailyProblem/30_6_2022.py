def solution(string: str, k: int) -> str:
    l, r = 0, 1
    hashmap = {}
    hashmap[string[l]] = 1
    largest_substring = ""
    while r < len(string) and l < r:
        if len(hashmap.keys()) > k:
            hashmap[string[l]] -= 1
            if hashmap[string[l]] == 0:
                del hashmap[string[l]]
            l += 1
        else:
            if len(string[l:r]) > len(largest_substring):
                largest_substring = string[l:r]
            if r < len(string):
                hashmap[string[r]] = hashmap.get(string[r], 0) + 1
            r += 1

    return largest_substring


print(solution("WORLD", 4))

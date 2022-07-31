from functools import lru_cache


# can also be implemented with a handmade cache.
# e.g. cache[(s1, s2, s3)] = bool
@lru_cache
def is_interleaved(s1: str, s2: str, s3: str) -> bool:
    if s1 == s2 == s3 == "":
        return True

    pick_from_s1, pick_from_s2 = False, False
    if s1 and s3 and s1[0] == s3[0]:
        pick_from_s1 = is_interleaved(s1[1:], s2, s3[1:])
    if pick_from_s1:
        return True

    if s2 and s3 and s2[0] == s3[0]:
        pick_from_s2 = is_interleaved(s1, s2[1:], s3[1:])

    return pick_from_s2


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(is_interleaved(s1, s2, s3))

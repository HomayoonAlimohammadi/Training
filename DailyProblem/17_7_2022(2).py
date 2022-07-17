from functools import lru_cache
from time import time


def levenshtein_distance(a: str, b: str) -> int:
    if len(b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)

    if a[0] == b[0]:
        return levenshtein_distance(a[1:], b[1:])

    trim_a = levenshtein_distance(a[1:], b)
    trim_b = levenshtein_distance(a, b[1:])
    trim_both = levenshtein_distance(a[1:], b[1:])
    return 1 + min(trim_a, trim_b, trim_both)


@lru_cache
def levenshtein_distance_cached(a: str, b: str) -> int:
    if len(b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)

    if a[0] == b[0]:
        return levenshtein_distance_cached(a[1:], b[1:])

    trim_a = levenshtein_distance_cached(a[1:], b)
    trim_b = levenshtein_distance_cached(a, b[1:])
    trim_both = levenshtein_distance_cached(a[1:], b[1:])
    return 1 + min(trim_a, trim_b, trim_both)


t0 = time()
a, b = "kitten", "sitting"
for _ in range(1000):
    levenshtein_distance(a, b)
print(time() - t0)

t1 = time()
for _ in range(6000000):
    levenshtein_distance_cached(a, b)
print(time() - t1)

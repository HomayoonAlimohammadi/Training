"""
Return all possible ways to climb a staircase with n stairs.
You can climb either 1 or 2 steps at a time.
"""
from functools import lru_cache
from typing import List

# a better way instead of this function is to iterate over numbers
# it will be O(n) but now its O(2^n)
@lru_cache
def solution(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    return solution(n - 1) + solution(n - 2)


# this one is O(len(steps)^n) !!
@lru_cache
def solution_generalized(n: int, steps: List[int]) -> int:

    if n < steps[0]:
        return 0

    if n in steps:
        ans = 1
        for i in range(steps.index(n)):
            ans += solution_generalized(n - steps[i], steps)
        return ans

    ans = 0
    for step in steps:
        if n < step:
            break
        ans += solution_generalized(n - step, steps)

    return ans


print(solution(4))
print(solution_generalized(5, [1, 3, 5, 7]))

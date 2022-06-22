"""
A module to calculate number of possible ways to
take steps towards the end. 
"""


def permutation(n_steps: int) -> int:

    if n_steps == 1 or n_steps == 2:
        return n_steps
    base_1, base_2 = 1, 1
    for i in range(n_steps - 1):
        ans = base_1 + base_2
        base_2, base_1 = ans, base_2

    return ans


n = int(input())
print(permutation(n))

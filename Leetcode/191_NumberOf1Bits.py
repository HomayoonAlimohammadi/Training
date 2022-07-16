def solution(n: int) -> int:
    """It is called hamming weight as well."""
    return bin(n).count("1")


def solution2(n: int) -> int:
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res


def solution3(n: int) -> int:
    res = 0
    while n:
        res += 1
        n = n & (n - 1)


n = 11
print(solution(n))

from math import sin


def solution(k: int) -> int:
    for n in range(1, 10**9):
        if 0 < sin(n) * k < 1:
            return n


n = int(input())
print(solution(n))

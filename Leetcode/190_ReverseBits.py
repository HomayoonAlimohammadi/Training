def solution(n: int) -> int:
    n = '{:032b}'.format(n)
    print(len(n))
    print(n)
    return int(n[::-1], 2)


n = 43261596
print(solution(n))

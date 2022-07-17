def solution(n: int) -> int:
    n = "{:032b}".format(n)
    return int(n[::-1], 2)


n = 43261596
print(solution(n))

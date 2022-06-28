def solution(a: int) -> int:
    valid_nums = list("1379")
    if str(a)[-1] not in valid_nums:
        return -1

    base = "1" * (len(str(a)))
    k = int(base) / a
    while k < 10**1000_000:
        if k == int(k):
            return k
        base += "1"
        k = int(base) / a
    return -1


a = int(input())
print(solution(a))

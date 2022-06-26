from functools import lru_cache


@lru_cache
def calculate_ways(code: str) -> int:

    if not code:
        return 1

    if code[0] == "0":
        return 0

    if len(code) == 1:
        return 1

    total = calculate_ways(code[1:])
    if int(code[:2]) in range(10, 27):
        total += calculate_ways(code[2:])

    return total


print(calculate_ways("123123"))

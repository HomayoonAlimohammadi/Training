def solution(n: int) -> bool:
    cache = {}
    while True:
        if n in cache:
            return False

        digits = list(str(n))
        digits = [int(digit) ** 2 for digit in digits]
        sum_digits = sum(digits)
        print(f"{digits} --> {sum_digits}")
        if sum_digits == 1:
            return True
        cache[n] = sum_digits
        n = sum_digits


n = 19
print(solution(n))

n = 2
print(solution(n))

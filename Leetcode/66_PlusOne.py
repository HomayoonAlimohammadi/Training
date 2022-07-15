def solution(digits: list[int]) -> list[int]:
    idx = len(digits) - 1
    while True:
        if digits[idx] < 9:
            digits[idx] += 1
            return digits
        digits[idx] = 0
        if idx > 0:
            idx -= 1
        else:
            digits.insert(0, 1)
            return digits


digits = [1, 2, 9]
print(solution(digits))

digits = [9]
print(solution(digits))

digits = [9, 9, 9]
print(solution(digits))

digits = [1, 2, 3]
print(solution(digits))

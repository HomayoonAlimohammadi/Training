def solution(n: int) -> list[int]:
    output = []
    for num in range(n + 1):
        n_one_bits = 0
        while num > 0:
            num = num & (num - 1)
            n_one_bits += 1
        output.append(n_one_bits)
    return output


n = 2
print(solution(n))

n = 5
print(solution(n))

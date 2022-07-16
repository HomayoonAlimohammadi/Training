def solution(num_list: list[int]) -> int:
    result = 0
    for num in num_list:
        result ^= num

    return result


num_list = [4, 1, 2, 1, 2]
print(solution(num_list))

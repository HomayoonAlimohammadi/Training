from functools import reduce


def solution():
    _ = int(input())
    nums = [int(num) for num in input().split()]
    unique_nums = [num for num in nums if nums.count(num) == 1]
    if len(unique_nums) == 0:
        return 0
    result = reduce(lambda x, y: x ^ y, unique_nums)
    return result


print(solution())

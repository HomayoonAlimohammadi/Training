def solution(nums: list[int]) -> int:
    target = sum(range(len(nums) + 1))
    for num in nums:
        target -= num
    return target


nums = [0, 1, 3]
print(solution(nums))

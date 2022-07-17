def solution(nums: list[int]) -> list[int]:
    duplicates = []
    for num in nums:
        if isinstance(num, str):
            num = int(num[1:])
        target = nums[abs(num)]
        if isinstance(nums[abs(num)], int):
            nums[abs(num)] = "*" + str(target)
        else:
            duplicates.append(num)

    return duplicates


nums = [1, 2, 3, 6, 3, 6, 1]
print(solution(nums))

nums = [1, 2, 3, 4, 3]
print(solution(nums))

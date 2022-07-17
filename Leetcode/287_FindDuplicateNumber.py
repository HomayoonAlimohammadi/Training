def solution(nums: list[int]) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while slow != slow2:
        slow, slow2 = nums[slow], nums[slow2]

    return slow2


nums = [1, 3, 2, 2, 4]
print(solution(nums))

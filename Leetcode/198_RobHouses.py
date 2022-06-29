from typing import List


def rob_max_amount(nums: List[int]) -> int:

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    amounts = nums[:2]
    amount = max(amounts[0] + nums[2], amounts[1])
    amounts.append(amount)

    for house_idx in range(3, len(nums)):
        amount = max(
            amounts[house_idx - 1],
            nums[house_idx] + amounts[house_idx - 2],
            nums[house_idx] + amounts[house_idx - 3],
        )
        amounts.append(amount)

    print(amounts)
    return max(amounts[-2:])

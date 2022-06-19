from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Calculate all unique combinations that add up to the target.
    A combination is unique if no other combination has the same frequency
    of values.
    """

    results: List[List[int]] = []
    candidates.sort()

    def find_combination(
        nums: List[int], combination: List[int], comb_sum: int
    ) -> None:

        if comb_sum == target:
            results.append(combination.copy())
            return

        org_combination = combination.copy()
        org_sum = comb_sum
        for i, num in enumerate(nums):
            while comb_sum + num <= target:
                combination.append(num)
                comb_sum += num
                find_combination(nums[i + 1 :], combination.copy(), comb_sum)

            combination = org_combination.copy()
            comb_sum = org_sum

    find_combination(candidates, [], 0)
    return results


NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
TARGET = 9
print(combination_sum(NUMS, TARGET))

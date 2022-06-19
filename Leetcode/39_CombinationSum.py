from typing import List, Dict
from collections import Counter


def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Calculate all unique combinations that add up to the target.
    A combination is unique if no other combination has the same frequency
    of values.
    """

    results: List[List[int]] = []
    results_counter: List[Dict[int, int]] = []
    nums.sort()

    def find_combination(combination: List[int], comb_sum: int) -> None:

        if comb_sum == target:
            if Counter(combination) not in results_counter:
                results.append(combination.copy())
                results_counter.append(Counter(combination))
            return

        if comb_sum < target:
            for num in nums:
                if comb_sum + num <= target:
                    combination.append(num)
                    find_combination(combination, comb_sum + num)
                    combination.pop()
                else:
                    break

    find_combination([], 0)
    return results


NUMS = [100, 200, 4, 12]
TARGET = 400
combination_sum(NUMS, TARGET)

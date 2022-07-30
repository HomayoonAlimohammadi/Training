from functools import lru_cache


def get_n_permutations(nums: list[int], target: int) -> int:
    @lru_cache
    def check_num(idx: int, sum_until_now: int) -> int:
        if idx >= len(nums):
            return sum_until_now == target

        new_element = nums[idx]
        subtract = check_num(idx + 1, sum_until_now - new_element)
        add = check_num(idx + 1, sum_until_now + new_element)
        return subtract + add

    return check_num(0, 0)


def get_n_permutations_3(nums: list[int], target: int) -> int:
    cache = {}

    def check_num(idx: int, sum_until_now: int) -> int:
        if idx >= len(nums):
            return sum_until_now == target
        if (idx, sum_until_now) in cache:
            return cache[(idx, sum_until_now)]

        new_element = nums[idx]
        subtract = check_num(idx + 1, sum_until_now - new_element)
        add = check_num(idx + 1, sum_until_now + new_element)
        total = subtract + add
        cache[(idx, sum_until_now)] = total
        return total

    return check_num(0, 0)


def get_n_permutations_2(nums: list[int], target: int) -> int:
    new_val = nums.pop()
    sums_until_now = [new_val, -new_val]
    while nums:
        new_val = nums.pop()
        new_sums = []
        while sums_until_now:
            old_sum = sums_until_now.pop()
            new_sums.append(old_sum + new_val)
            new_sums.append(old_sum - new_val)
        sums_until_now = new_sums.copy()

    return sums_until_now.count(target)


nums = [1, 1, 1, 1, 1]
target = 3
print(get_n_permutations(nums, target))
print(get_n_permutations_2(nums, target))
print(get_n_permutations_3(nums, target))


nums = [1]
target = 1
print(get_n_permutations(nums, target))
print(get_n_permutations_2(nums, target))
print(get_n_permutations_3(nums, target))


nums = [1]
target = 10
print(get_n_permutations(nums, target))
print(get_n_permutations_2(nums, target))
print(get_n_permutations_3(nums, target))

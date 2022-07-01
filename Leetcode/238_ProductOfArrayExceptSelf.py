from typing import List


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]
        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            result.append(product)

        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            result[i - 1] *= product

        return result


def solution(nums: List[int]) -> List[int]:
    zero_count = 0
    total_prod = 1
    zero_idx
    for idx, num in enumerate(nums):
        if num == 0:
            if zero_count >= 1:
                return [0 for _ in range(len(nums))]
            if zero_count == 0:
                zero_count += 1
                zero_idx = idx
                continue
        total_prod *= num

    if zero_count == 1:
        ans = [0 for _ in range(len(nums))]
        ans[zero_idx] = total_prod
        return ans

    return [int(total_prod / num) for num in nums]


sol = Solution1()
nums = [1, 2, 3, 4]
print(sol.productExceptSelf(nums))

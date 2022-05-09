from typing import List


class Solution1:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]
        product = 1
        for i in range(len(nums)-1):
            product *= nums[i]
            result.append(product)

        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            result[i-1] *= product

        return result

solution = Solution1()
nums = [1,2,3,4]
print(solution.productExceptSelf(nums))
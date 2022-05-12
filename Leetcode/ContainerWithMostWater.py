from typing import List


class Solution:

    def mostArea(self, height: List[int]) -> int:

        first, last = 0, len(height) - 1
        maxArea = min(height[first], height[last]) * (last - first)
        while first < last:

            area = min(height[first], height[last]) * (last - first)
            if area > maxArea:
                maxArea = area

            if height[first] > height[last]:
                last -= 1
            else:
                first += 1

        return maxArea


sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.mostArea(height))


        
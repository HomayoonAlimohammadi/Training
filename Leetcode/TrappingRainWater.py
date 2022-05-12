from typing import List
import numpy as np


class Solution:

    def trap(self, height: List[int]) -> int:

        while len(height) > 0 and height[0] == 0:
            height.pop(0)

        while len(height) > 0 and height[-1] == 0:
            height.pop()

        water = np.array(height)

        first = 0
        last = len(height) - 1
        level = 0
        
        while first < last: 

            level = max(min(height[first], height[last]), level)
            water[first:last+1] = level

            if height[first] >= height[last]:
                last -= 1

            else:
                first += 1

        for i in range(len(water)):
            if water[i] >= height[i]:
                water[i] -= height[i]
            else:
                water[i] = 0

        print(water)

        return sum(water)


sol = Solution()
height = [2,6,3,8,2,7,2,5,0]
print(sol.trap(height))


class Solution2:

    def trap(self, height: List[int]) -> int:

        start, end = 0, len(height) - 1
        output = 0
        max_start, max_end = 0, 0

        while start < end:

            if height[start] > height[end]:
                if height[end] < max_end:
                    output += max_end - height[end]
                else:
                    max_end = height[end]
                end -= 1

            else:
                if height[start] < max_start:
                    output += max_start - height[start]
                else:
                    max_start = height[start]

                start += 1

        return output


sol = Solution2()
height = [2,6,3,8,2,7,2,5,0]
print(sol.trap(height))


from typing import List
from collections import Counter


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:

        DEBUG = 1
        i, j = 0, len(heights) - 1
        maxArea = 0
        heights_sorted = sorted(heights, reverse=True)
        height_map = Counter(heights)
        
        while i <= j:

            height = heights_sorted[-1]
            area = (j - i + 1) * height
            maxArea = max(area, maxArea)

            if DEBUG:
                print('heights:', heights[i:j+1])
                print(f'{height_map=}')
                print(f'{heights_sorted=}')
                print(f'{height=}')
                print(f'{maxArea=}')
                print(i, j)
                print()

            if i == j:
                break

            i_temp = i
            j_temp = j
            while heights[i_temp] == heights[j_temp] and i < j - 1:
                j_temp -= 1
                i_temp += 1

            if heights[j_temp] > heights[i_temp]:

                height_map[heights[i]] -= 1
                if height_map[heights[i]] == 0:

                    temp_stack = []
                    while heights_sorted[-1] != heights[i]:
                        h = heights_sorted.pop()
                        temp_stack.append(h)
                    while heights_sorted[-1] == heights[i]:
                        heights_sorted.pop()
                    while temp_stack:
                        h = temp_stack.pop()
                        heights_sorted.append(h)

                i += 1
                
            else:
                
                height_map[heights[j]] -= 1
                if height_map[heights[j]] == 0:

                    temp_stack = []
                    while heights_sorted[-1] != heights[j]:
                        h = heights_sorted.pop()
                        temp_stack.append(h)
                    while heights_sorted[-1] == heights[j]:
                        heights_sorted.pop()
                    while temp_stack:
                        h = temp_stack.pop()
                        heights_sorted.append(h)

                j -= 1

        return maxArea


class Solution2:

    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            # stack.append((i, h))
            index = None
            while stack and stack[-1][1] > h:
                index = stack[-1][0]
                height = stack[-1][1]
                area = ((i - index) * height)
                maxArea = max(maxArea, area)
                stack.pop()
            if index is None:
                index = i
            stack.append((index, h))

        for i, h in stack:
            maxArea = max(maxArea, (h * (len(heights) - i)))

        return maxArea


sol = Solution2()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))
            

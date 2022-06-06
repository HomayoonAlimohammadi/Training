from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])

        n_s = []
        i = 0
        while i < len(intervals):
            inter = intervals[i]
            while i < len(intervals) - 1 and inter[1] >= intervals[i+1][0]:
                i += 1
                inter[1] = max(inter[1], intervals[i][1])
                
            n_s.append(inter)
            i += 1

        return n_s


func = Solution().merge
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1, 3], [2, 5], [6, 9]]
print(func(intervals))
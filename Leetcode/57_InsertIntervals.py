from typing import List
import unittest


class Solution:

    def insert_old(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]

        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        if i == len(intervals):

            if intervals[-1][1] < newInterval[0]:
                intervals.append(newInterval)

            elif intervals[-1][1] < newInterval[1]:
                intervals[-1][1] = newInterval[1]

            return intervals
        
        m = newInterval[:]
        idx_m = i 
        idx_a = i

        if i != 0:
            b = intervals[i - 1]
            idx_b = i - 1
            if m[0] <= b[1]:
                m[0] = b[0]
                m[1] = max(m[1], b[1])
                del intervals[idx_b]
                idx_m -= 1
                idx_a -= 1
            
        if i == len(intervals) - 1:
            if m[1] >= intervals[i][0]:
                m[1] = max(m[1], intervals[i][1])
                del intervals[i]
            intervals.insert(idx_m, m)
            # print('reached end', m)
            return intervals
        
        a = intervals[idx_a]

        while m[1] >= a[0] and idx_a < len(intervals)-1:
            # print(m,'collide with next:',intervals[idx_a])
            m[1] = max(a[1], m[1])
            del intervals[idx_a]
            a = intervals[idx_a]
            # print('-->', m)

        if m[1] >= a[0]:
            m[1] = max(a[1], m[1])
            del intervals[idx_a]

        intervals.insert(idx_m, m)
        return intervals

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]

        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        m = newInterval[:]
        idx_m = i

        # ghabli dare ya na
        if idx_m > 0: 
            b = intervals[i-1]
            if m[0] >= b[1]:
                m[1] = max(m[1], b[1])
                del intervals[i-1]
            
        # badi dare ya na
        if idx_m < len(intervals) - 1:
            idx_a = i
            a = intervals[idx_a]

            while m[1] >= a[0] and idx_a < len(intervals)-1:
                m[1] = max(a[1], m[1])
                del intervals[idx_a]
                a = intervals[idx_a]

        if idx_m == 0:
            pass

    def insert_merge(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]

        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        intervals.insert(i, newInterval)
        intervals = self.merge(intervals)
        return intervals

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



        
            

class TestInsert(unittest.TestCase):

    def setUp(self):
        self.func = Solution().insert

    def test_insert(self):
        
        # intervals = [[1,3],[6,9]]
        # newInterval = [2,5]
        # ans = [[1,5], [6, 9]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        # newInterval = [4,8]
        # ans = [[1, 2], [3, 10], [12, 16]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        # intervals = [[1,2], [3,5]]
        # newInterval = [3,4]
        # ans = [[1,2], [3,5]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        # intervals = [[1,2], [3,5]]
        # newInterval = [6,7]
        # ans = [[1, 2], [3, 5], [6, 7]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        # intervals = [[3,4], [5,6]]
        # newInterval = [1,2]
        # ans = [[1, 2], [3,4], [5,6]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        # intervals = [[3,4], [5,6]]
        # newInterval = [1,3]
        # ans = [[1,4], [5,6]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        # intervals = [[1,5]]
        # newInterval = [2,3]
        # ans = [[1,5]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        # intervals = [[1,5]]
        # newInterval = [2,6]
        # ans = [[1,6]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        # intervals = [[1,5]]
        # newInterval = [6,7]
        # ans = [[1,5], [6,7]]
        # self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[1,5], [6,8]]
        newInterval = [5,6]
        ans = [[1,8]]
        self.assertEqual(self.func(intervals, newInterval), ans)


unittest.main()
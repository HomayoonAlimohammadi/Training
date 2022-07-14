from typing import List
import unittest


class Solution:
    def insert_old(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        new_idx = 0
        for idx, interval in enumerate(intervals):
            if new_interval[0] <= interval[0]:
                new_idx = idx
                break
        else:
            new_idx = len(intervals)

        # merge with previouse interval
        before = new_idx - 1
        if before >= 0 and intervals[before][1] >= new_interval[0]:
            new_interval[0] = intervals[before][0]
            new_interval[1] = max(intervals[before][1], new_interval[1])
            intervals.pop(before)
            new_idx -= 1

        # merge with later interval(s)
        after = new_idx
        while after < len(intervals) and intervals[after][0] <= new_interval[1]:
            new_interval[1] = max(intervals[after][1], new_interval[1])
            intervals.pop(after)

        intervals.insert(new_idx, new_interval)
        return intervals

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]

        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        m = newInterval[:]
        idx_m = i

        # ghabli dare ya na
        if idx_m > 0:
            b = intervals[i - 1]
            if m[0] >= b[1]:
                m[1] = max(m[1], b[1])
                del intervals[i - 1]

        # badi dare ya na
        if idx_m < len(intervals) - 1:
            idx_a = i
            a = intervals[idx_a]

            while m[1] >= a[0] and idx_a < len(intervals) - 1:
                m[1] = max(a[1], m[1])
                del intervals[idx_a]
                a = intervals[idx_a]

        if idx_m == 0:
            pass

    def insert_merge(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]

        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        intervals.insert(i, newInterval)
        intervals = self.merge(intervals)
        return intervals

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        n_s = []
        i = 0
        while i < len(intervals):
            inter = intervals[i]
            while i < len(intervals) - 1 and inter[1] >= intervals[i + 1][0]:
                i += 1
                inter[1] = max(inter[1], intervals[i][1])

            n_s.append(inter)
            i += 1

        return n_s


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.func = Solution().insert_old

    def test_insert(self):

        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        ans = [[1, 5], [6, 9]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        ans = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[1, 2], [3, 5]]
        newInterval = [3, 4]
        ans = [[1, 2], [3, 5]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[1, 2], [3, 5]]
        newInterval = [6, 7]
        ans = [[1, 2], [3, 5], [6, 7]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[3, 4], [5, 6]]
        newInterval = [1, 2]
        ans = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[3, 4], [5, 6]]
        newInterval = [1, 3]
        ans = [[1, 4], [5, 6]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[1, 5]]
        newInterval = [2, 3]
        ans = [[1, 5]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[1, 5]]
        newInterval = [2, 6]
        ans = [[1, 6]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[1, 5]]
        newInterval = [6, 7]
        ans = [[1, 5], [6, 7]]
        self.assertEqual(self.func(intervals, newInterval), ans)

        intervals = [[1, 5], [6, 8]]
        newInterval = [5, 6]
        ans = [[1, 8]]
        self.assertEqual(self.func(intervals, newInterval), ans)


if __name__ == "__main__":
    unittest.main()
    # intervals = [[1, 3], [6, 9]]
    # new_interval = [-2, 12]
    # print(Solution().insert_old(intervals, new_interval))

    # intervals = [[1, 5]]
    # new_interval = [2, 3]
    # print(Solution().insert_old(intervals, new_interval))

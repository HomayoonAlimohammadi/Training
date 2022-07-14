from typing import List
from collections import defaultdict


def solution(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda interval: (interval[0], -interval[1]))
    mapping = defaultdict(list)
    for idx, interval in enumerate(intervals):
        start, end = idx, idx + 1
        while end < len(intervals) and intervals[end][0] < interval[1]:
            mapping[start].append(end)
            mapping[end].append(start)
            end += 1

    items = list(mapping.items())
    items.sort(key=lambda item: len(item[1]))

    min_deletes = 0
    while items:
        key, values = items.pop()
        if key not in mapping:
            continue
        for target in values:
            mapping[target].remove(key)
            if len(mapping[target]) == 0:
                del mapping[target]
        min_deletes += 1
    return min_deletes


def solution_2(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda interval: (interval[0], -interval[1]))
    idx = 0
    pops = 0
    while idx < len(intervals) - 1:
        if intervals[idx][1] > intervals[idx + 1][0]:
            if (intervals[idx][1] - intervals[idx][0]) > (
                intervals[idx + 1][1] - intervals[idx + 1][0]
            ):  # first one was larger
                intervals.pop(idx)
            else:
                intervals.pop(idx + 1)
            pops += 1
        else:
            idx += 1
    return pops


def solution_2(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda interval: (interval[0], -interval[1]))
    idx = 0
    pops = 0
    while idx < len(intervals) - 1:
        if intervals[idx][1] > intervals[idx + 1][0]:
            if intervals[idx][1] > intervals[idx + 1][1]:
                intervals.pop(idx)
            else:
                intervals.pop(idx + 1)
            pops += 1
        else:
            idx += 1
    return pops


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(solution(intervals))
print(solution_2(intervals))

print()
intervals = [[1, 2], [1, 2], [1, 2]]
print(solution(intervals))
print(solution_2(intervals))

print()
intervals = [[1, 2], [2, 3]]
print(solution(intervals))
print(solution_2(intervals))

print()
intervals = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
print(solution(intervals))
print(solution_2(intervals))

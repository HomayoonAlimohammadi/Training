def solution(intervals: list[tuple[int]]) -> int:
    intervals.sort(key=lambda tup: tup[0])

    max_classes = 0
    for idx, current_interval in enumerate(intervals):
        before_idx = idx - 1
        n_overlapping = 1
        while before_idx >= 0 and intervals[before_idx][1] > current_interval[0]:
            n_overlapping += 1
            before_idx -= 1
        max_classes = max(max_classes, n_overlapping)

    return max_classes


intervals = [(30, 75), (0, 50), (60, 150), (0, 200)]
print(solution(intervals))

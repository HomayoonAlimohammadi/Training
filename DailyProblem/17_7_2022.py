from typing import List


def solution(heights: List[int]) -> int:
    base = heights.pop()
    puddle = []
    max_water = 0
    while heights:
        ground = heights.pop()
        while puddle and ground > puddle[-1]:
            hole = puddle.pop()
            max_water += min(ground, base) - hole
        base = max(base, ground)
        puddle.append(ground)

    return max_water


heights = [2, 1, 2]
print(solution(heights))

heights = [3, 0, 1, 3, 0, 5]
print(solution(heights))

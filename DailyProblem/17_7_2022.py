from typing import List


def solution(heights: List[int]) -> int:
    base = heights.pop()
    print(f"first base: {base}")
    puddle = [base]
    max_water = 0
    while heights:
        ground = heights.pop()
        if ground >= base:
            while puddle:
                hole = puddle.pop()
                max_water += base - hole
            base = ground
        puddle.append(ground)

    if not puddle:
        return max_water

    heights = puddle.copy()
    base = heights.pop()
    puddle = [base]
    while heights:
        ground = heights.pop()
        if ground >= base:
            while puddle:
                max_water += base - puddle.pop()
            base = ground
        puddle.append(ground)

    return max_water


heights = [2, 1, 2]
print(solution(heights))

heights = [3, 0, 1, 3, 0, 5]
print(solution(heights))

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution(heights))

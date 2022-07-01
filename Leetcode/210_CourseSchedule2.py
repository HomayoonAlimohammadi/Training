from typing import List


def solution(num_courses: int, prerequisites: List[List[int]]):

    pre_map = {}
    for course, pre in prerequisites:
        pre_map[course] = pre_map.get(course, []) + [pre]

    order = []
    visited = set()

    def has_loop(course: int):
        if len(pre_map.get(course, [])) == 0:
            if course not in order:
                order.append(course)
            return False
        if course in visited:
            return True

        visited.add(course)
        for pre in pre_map.get(course, []):
            if has_loop(pre):
                return True

        visited.remove(course)
        pre_map[course] = []
        if course not in order:
            order.append(course)
        return False

    for course in range(num_courses):
        if has_loop(course):
            return []

    return order

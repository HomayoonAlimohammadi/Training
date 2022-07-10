from random import randint
from collections import deque


def solution(grid: list[list[bool]], start: tuple[int], end: tuple[int]) -> int:
    seen = set()
    potentials = [start]

    steps = 1
    new_potentials = []
    while True:
        if len(potentials) == 0:
            steps += 1
            potentials = new_potentials.copy()

        row, col = potentials.pop()
        seen.add((row, col))

        for dr, dc in (0, -1), (-1, 0), (0, 1), (1, 0):
            if (row + dr, col + dc) == end:
                return steps
            if (
                (row + dr, col + dc) not in seen
                and 0 <= row + dr < len(grid)
                and 0 <= col + dc < len(grid[0])
                and grid[row + dr][col + dc] == False  # is a tile not a wall.
            ):
                new_potentials.append((row + dr, col + dc))


def solution_bfs(grid: list[list[bool]], start: tuple[int], end: tuple[int]) -> int:
    locations = deque([(*start, 0)])
    seen = set()
    while locations:
        row, col, steps = locations.popleft()

        for dr, dc in (0, -1), (-1, 0), (0, 1), (1, 0):
            if (row + dr, col + dc) == end:
                return steps + 1
            if (
                (row + dr, col + dc) not in seen
                and 0 <= row + dr < len(grid)
                and 0 <= col + dc < len(grid[0])
                and grid[row + dr][col + dc] == False  # is a tile not a wall.
            ):
                locations.append((row + dr, col + dc, steps + 1))


def solution_dfs(grid: list[list[bool]], start: tuple[int], end: tuple[int]) -> int:

    seen = set()

    def dfs(location: tuple[int], steps: int) -> tuple[bool, int]:
        if location == end:
            return True, steps
        if location in seen:
            return False, steps

        seen.add(location)
        row, col = location
        for dr, dc in (0, -1), (-1, 0), (0, 1), (1, 0):
            if (
                (row + dr, col + dc) not in seen
                and 0 <= row + dr < len(grid)
                and 0 <= col + dc < len(grid[0])
                and grid[row + dr][col + dc] == False  # is a tile not a wall.
            ):
                res = dfs((row + dr, col + dc), steps + 1)
                if res[0]:
                    return res

    is_possible, steps = dfs(start, 0)
    return steps


def solution_random(grid: list[list[bool]], start: tuple[int], end: tuple[int]) -> int:
    mapping = {
        1: (1, 0),  # down
        2: (0, 1),  # left
        3: (-1, 0),  # up
        4: (0, -1),  # right
    }

    counter = 10
    THRESHOLD = 10
    while True:
        counter += 1
        if counter > THRESHOLD:
            current_loc = start
            counter = 0
            seen = set()

        row, col = current_loc
        seen.add(current_loc)
        dr, dc = mapping[randint(1, 4)]
        if (row + dr, col + dc) == end:
            return counter
        if (
            (row + dr, col + dc) not in seen
            and 0 <= row + dr < len(grid)
            and 0 <= col + dc < len(grid[0])
            and not grid[row + dr][col + dc]
        ):
            current_loc = (row + dr, col + dc)


grid = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False],
]
start = (3, 0)
end = (0, 0)


def test_random(grid: list[list[bool]], start: tuple[int], end: tuple[int]) -> int:
    results = []
    for _ in range(100):
        results.append(solution_random(grid, start, end))

    print(min(results))


def test_main(grid: list[list[bool]], start: tuple[int], end: tuple[int]) -> int:
    print(solution(grid, start, end))
    print(solution_bfs(grid, start, end))
    print(solution_dfs(grid, start, end))


test_main(grid, start, end)

from typing import List


def find_gates(
    grid: List[List[int]], inf_value: float | None = None
) -> List[List[int]]:
    """
    Replace grid elements with shortest path to gates.
    `-1`: a wall or obstacle.
    `0`: a gate.
    `inf (2^31 - 1)`: empty path.
    """
    gates = []
    for r_idx, row in enumerate(grid):
        for c_idx, element in enumerate(row):
            if element == 0:
                gates.append((r_idx, c_idx))

    ALL_SIDES = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    N_ROWS = len(grid)
    N_COLUMNS = len(grid[0])
    INF = float("inf") if inf_value is None else inf_value

    distance = 1
    new_gates = []
    while True:
        if len(gates) == 0:  # no more gates in current iteration
            if len(new_gates) == 0:  # no gates for next iteration
                break
            distance += 1  # increase distance for next iteration
            gates = new_gates.copy()  # set next iter to current iter
            new_gates = []  # ready for next iter
        row, col = gates.pop()
        for dr, dc in ALL_SIDES:
            if (
                0 <= row + dr < N_ROWS
                and 0 <= col + dc < N_COLUMNS
                and grid[row + dr][col + dc] == INF
            ):
                # grid[row+dr][col+dc] = min(grid[row+dr][col+dc], distance)
                grid[row + dr][col + dc] = distance
                new_gates.append((row + dr, col + dc))

    return grid


grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
print(find_gates(grid=grid, inf_value=2**31 - 1))

grid = [[0, -1], [2147483647, 2147483647]]
print(find_gates(grid=grid, inf_value=2**31 - 1))

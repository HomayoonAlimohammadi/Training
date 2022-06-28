from typing import List, Tuple


def calculate_max_fresh_time(grid: List[List[int]]) -> Tuple[int, List[List[int]]]:
    """Return number of days until all the oranges are
    going to rot. Given a grid with following properties:
    `0`: empty cell
    `1`: fresh orange
    `2`: rotten orange
    Return -1 if impossible.
    """
    grid_mod = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for row in range(len(grid)):
        time = float("inf")
        for col in range(len(grid[0])):

            if grid[row][col] == 0:
                grid_mod[row][col] = 0
                time += 1
                print(f"{row}, {col} set to 0 because empty")
                continue

            if grid[row][col] == 2:
                print(f"{row}, {col} set to 0 because rotten")
                time = 0

            elif grid[row][col] == 1:
                time = min(grid_mod[row][col], time)
                print(f"{row}, {col} set to {time} because fresh")

            grid_mod[row][col] = time
            time += 1

        for col in range(len(grid[0]) - 1, -1, -1):

            if grid[row][col] == 0:
                grid_mod[row][col] = 0
                time += 1
                print(f"{row}, {col} set to 0 because empty")
                continue

            if grid[row][col] == 2:
                print(f"{row}, {col} set to 0 because rotten")
                time = 0

            elif grid[row][col] == 1:
                time = min(grid_mod[row][col], time)
                print(f"{row}, {col} set to {time} because fresh")

            grid_mod[row][col] = time
            time += 1

    for row in range(len(grid) - 1, -1, -1):
        time = float("inf")
        for col in range(len(grid[0])):

            if grid[row][col] == 0:
                grid_mod[row][col] = 0
                time += 1
                print(f"{row}, {col} set to 0 because empty")
                continue

            if grid[row][col] == 2:
                print(f"{row}, {col} set to 0 because rotten")
                time = 0

            elif grid[row][col] == 1:
                time = min(grid_mod[row][col], time)
                print(f"{row}, {col} set to {time} because fresh")

            grid_mod[row][col] = time
            time += 1

        for col in range(len(grid[0]) - 1, -1, -1):

            if grid[row][col] == 0:
                grid_mod[row][col] = 0
                time += 1
                print(f"{row}, {col} set to 0 because empty")
                continue

            if grid[row][col] == 2:
                print(f"{row}, {col} set to 0 because rotten")
                time = 0

            elif grid[row][col] == 1:
                time = min(grid_mod[row][col], time)
                print(f"{row}, {col} set to {time} because fresh")

            grid_mod[row][col] = time
            time += 1

    for col in range(len(grid[0])):
        time = float("inf")
        for row in range(len(grid)):

            if grid[row][col] == 0:
                grid_mod[row][col] = 0
                time += 1
                print(f"{row}, {col} set to 0 because empty")
                continue

            if grid[row][col] == 2:
                print(f"{row}, {col} set to 0 because rotten")
                time = 0

            elif grid[row][col] == 1:
                time = min(grid_mod[row][col], time)
                print(f"{row}, {col} set to {time} because fresh")

            grid_mod[row][col] = time
            time += 1

        for row in range(len(grid) - 1, -1, -1):

            if grid[row][col] == 0:
                grid_mod[row][col] = 0
                time += 1
                print(f"{row}, {col} set to 0 because empty")
                continue

            if grid[row][col] == 2:
                print(f"{row}, {col} set to 0 because rotten")
                time = 0

            elif grid[row][col] == 1:
                time = min(grid_mod[row][col], time)
                print(f"{row}, {col} set to {time} because fresh")

            grid_mod[row][col] = time
            time += 1

    for col in range(len(grid[0]) - 1, -1, -1):
        time = float("inf")
        for row in range(len(grid)):

            if grid[row][col] == 0:
                grid_mod[row][col] = 0
                time += 1
                print(f"{row}, {col} set to 0 because empty")
                continue

            if grid[row][col] == 2:
                print(f"{row}, {col} set to 0 because rotten")
                time = 0

            elif grid[row][col] == 1:
                time = min(grid_mod[row][col], time)
                print(f"{row}, {col} set to {time} because fresh")

            grid_mod[row][col] = time
            time += 1

        for row in range(len(grid) - 1, -1, -1):

            if grid[row][col] == 0:
                grid_mod[row][col] = 0
                time += 1
                print(f"{row}, {col} set to 0 because empty")
                continue

            if grid[row][col] == 2:
                print(f"{row}, {col} set to 0 because rotten")
                time = 0

            elif grid[row][col] == 1:
                time = min(grid_mod[row][col], time)
                print(f"{row}, {col} set to {time} because fresh")

            grid_mod[row][col] = time
            time += 1

    MAX_TIME = 0
    for row in grid_mod:
        for element in row:
            MAX_TIME = max(MAX_TIME, element)

    MAX_TIME = -1 if MAX_TIME == float("inf") else MAX_TIME
    return grid_mod, MAX_TIME


grid = [[2, 1, 1], [1, 1, 0], [1, 0, 1]]
print(calculate_max_fresh_time(grid))

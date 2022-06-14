m = int(input())
grid = []
for i in range(m):
    row = [int(x) for x in input().split()]
    grid.append(row)

seen = set()
def area(r, c):
    '''calculate area of the island'''
    if not (0 <= r < len(grid)) or \
       not (0 <= c < len(grid[0])) or \
       grid[r][c] != 0 or \
       (r, c) in seen:
        return 0

    seen.add((r, c))
    return 1 + (r+1, c) + (r-1, c) + \
             (r, c+1), (r, c-1)

areas = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        areas.append(area(r, c))

print(max(areas))



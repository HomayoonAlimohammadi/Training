import bisect


def find_closest_zero(board, i, j):
    row = board[i]
    MIN = float('inf')
    col_idx = 0
    for col in range(len(board[0])):
        if row[col] == 0:
            MIN = min(MIN, abs(col -  j))
            col_idx = col
    return col_idx

def update_row(row, new_sit):
    for col in range(len(row)):
        row[col] = min(row[col], abs(new_sit - col))
    return row

n, m, k = input().split()
n, m, k = int(n), int(m), int(k)

# board = np.array([
#     [float('inf') for i in range(m)] for i in range(n)
# ])
board = []
records = {}
for r in range(n):
    line = input()
    row = [''] * m
    oc = [float('-inf')]
    for col in range(m):
        if line[col] == '#':
            row[col] = 0
            oc.append(col)
    oc.append(float('inf'))
    for col in range(m):
        if row[col] == 0:
            continue
        bisect.insort(oc, col)
        idx = oc.index(col)
        left = col - oc[idx-1]
        right = oc[idx + 1] - col
        dist = min(left, right)
        row[col] = dist
        oc.remove(col)
    board.append(row)
    records[r] = max(row)

# print(records)
# print(board)

for p in range(k):
    # key = max(records.keys())
    # sit = records[key].popleft()
    # r, c = sit 
    # r, c = r+1, c+1
    # print(r, c)
    # if len(records[key]) == 0:
    #     del records[key]

    dist = max(records.values())
    for k in records.keys():
        if records[k] == dist:
            row = board[k]
            row_idx = k
            break

    col_idx = row.index(dist)
    # closest = find_closest_zero(board, row_idx, col_idx)
    row = update_row(row, col_idx)
    board[row_idx] = row
    records[row_idx] = max(row)
    print(row_idx+1, col_idx+1)

    

    



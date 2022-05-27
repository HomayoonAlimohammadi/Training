import numpy as np


def is_sexy(l):
    if len(l) < 3:
        return True
    for i in range(2, len(l)):
        if l[i] != (l[i-1])**2 / l[i-1]:
            return False
    return True

def check_sexy_sub_board(sub_board):
    sexy = True
    for row in sub_board:
        if not is_sexy(row):
            sexy = False
            break
        # print('sexy:', row)
    else:
        for col in sub_board.transpose():
            if not is_sexy(col):
                sexy = False
                break
            # print('sexy', col)
    return sexy

n, m = input().split()
n, m = int(n), int(m)

board = []
for row in range(n):
    row = [int(i) for i in input().split()]
    board.append(row)

board = np.array(board)

def traverse(bot_left, l, h):

    i, j = bot_left
    if i - h < 0:
        return l * (h-1)
    if j + l >= len(board[0]):
        return h * (l - 1)

    sub_board = board[i-h:i, j:j+l]
    sexy = check_sexy_sub_board(sub_board)
    exp_length, exp_height, go_left, go_top = 0, 0, 0, 0
    # print(sub_board)
    if sexy:
        # print('exp_legnth')
        exp_length = traverse((i, j), l+1, h)
        # print('exp_height')
        exp_height = traverse((i, j), l, h+1)
    else:
        # print('go_top')
        go_top = traverse((i-1, j), l, h)
        # print('go_left')
        go_left = traverse((i, j+1), l, h)

    # print([exp_length, exp_height, go_top, go_left])
    return max([exp_length, exp_height, go_top, go_left])


print(traverse((n, 0), 2, 2))

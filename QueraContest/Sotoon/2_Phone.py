from collections import deque


number = deque(input())
numpad = {}
for i in range(10):
    numpad[str(i)] = input()

# print(numpad)
# print(number)
n_press = 0
n_presses = []
def choose(number, n_press):
    while number:
        num = number.popleft()
        candid = deque(numpad[num])
        candid.popleft()
        n_press += 1
        # print(number)
        while candid and number:
            if candid[0] == number[0]:
                p = choose(number, n_press + len(candid))
                n_presses.append(p)
                candid.popleft()
                number.popleft()
            else:
                break
        # print(candid)
        # print(n_press)
        # print()
        n_press += len(candid)
    n_presses.append(n_press)

    return min(n_presses)

print(n_press)

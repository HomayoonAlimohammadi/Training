from collections import deque


def solution(n: int) -> int:
    counter = 0
    i = 0
    while True:
        squared = i * i
        if str(squared)[-len(str(i)) :] == str(i):
            counter += 1
            if counter == n:
                return i

        i += 1


def gen_auto(n: int):
    total = [0, 1, 5, 6]
    nums = deque(total.copy())
    while len(total) < n:
        x = nums.popleft()
        new = (3 * x**2 - 2 * x**3) % (10 ** (2 * len(str(x))))
        if new not in total:
            total.append(new)
            nums.append(new)
    return total


print(gen_auto(20))

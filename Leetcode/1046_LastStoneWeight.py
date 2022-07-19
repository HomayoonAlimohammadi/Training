import bisect
import heapq


def solution_insort(stones: list[int]) -> int:
    stones.sort()
    while len(stones) > 1:
        y = stones.pop()
        x = stones.pop()
        if x < y:
            bisect.insort(stones, y - x)

    if stones:
        return stones[0]
    return 0


def solution_heapq(stones: list[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        if x < y:
            heapq.heappush(stones, -(y - x))

    if stones:
        return -stones[0]
    return 0


stones = [2, 7, 4, 1, 8, 1]
print(solution_insort(stones))
print(solution_heapq(stones))

stones = [1]
print(solution_insort(stones))
print(solution_heapq(stones))

stones = [2, 7, 4, 1, 8, 1]
print(solution_insort(stones))
print(solution_heapq(stones))

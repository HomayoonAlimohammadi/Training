from functools import lru_cache


# too slow
def solution_recursive(costs: list[int]) -> int:
    @lru_cache
    def jump(current: int, cost: int) -> int:
        single_step, double_step = float("inf"), float("inf")
        if current >= len(costs):
            return cost
        cost += costs[current]
        single_step = jump(current + 1, cost)
        double_step = jump(current + 2, cost)

        return min(single_step, double_step)

    start_from_0 = jump(current=0, cost=0)
    start_from_1 = jump(current=1, cost=0)

    return min(start_from_0, start_from_1)


# better, accepted but not dynamic
def solution_2_recursive(costs: list[int]) -> int:
    LEN_COSTS = len(costs)
    costs.append(0)

    @lru_cache
    def add_cost(step: int) -> int:
        if step < 0:
            return float("inf")
        if step in [0, 1]:
            return costs[step]
        return costs[step] + min(add_cost(step - 1), add_cost(step - 2))

    return add_cost(LEN_COSTS)


# dynamic solution
def solution(costs: list[int]) -> int:
    min_costs = costs[0:2]
    for cost in costs[2:]:
        min_cost = cost + min(min_costs[-2:])
        min_costs.append(min_cost)

    return min(min_costs[-2:])

    # Even better
    double_last, last = costs[0], costs[1]
    for cost in costs[2:]:
        min_cost = cost + min(last, double_last)
        double_last = last
        last = min_cost

    return min(last, double_last)


costs = [10, 15, 20]
print(solution(costs))
print(solution_recursive(costs))
print(solution_2_recursive(costs))

costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(solution(costs))
print(solution_recursive(costs))
print(solution_2_recursive(costs))

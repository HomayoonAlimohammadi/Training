from typing import List
from functools import lru_cache
from time import time


def get_min_coins(coins: List[int], amount: int) -> int:
    """Return minimum number of coins that sum up to `amount`."""
    if amount == 0:
        return 0
    coins.sort()
    num_coins_list = []
    for amnt in range(1, amount + 1):
        if amnt in coins:
            num_coins_list.append(1)
            continue
        coin_idx = 0
        num_coins = float("inf")
        while 0 <= coin_idx < len(coins) and coins[coin_idx] <= amnt:
            coin = coins[coin_idx]
            num_coins = min(num_coins, num_coins_list[-coin] + 1)
            coin_idx += 1
        num_coins_list.append(num_coins)

    min_coins = num_coins_list[amount - 1]
    min_coins = -1 if min_coins == float("inf") else min_coins
    return min_coins


def get_min_coins_rec(coins: List[int], amount: int) -> int:
    """Return minimum number of coins that sum up to `amount`."""
    coins.sort(reverse=True)

    @lru_cache
    def pick(amount_left: int, n_picks: int):
        if amount_left == 0:
            return n_picks
        if amount_left < coins[-1]:
            return -1
        min_picks = float("inf")
        for coin in coins:
            if coin <= amount_left:
                n_picks = pick(amount_left - coin, n_picks + 1)
                n_picks = float("inf") if n_picks == -1 else n_picks
                min_picks = min(min_picks, n_picks)

        return min_picks

    min_coins = pick(amount, 0)
    min_coins = -1 if min_coins == float("inf") else min_coins
    return min_coins


coins = [1, 2, 5]
amount = 30
t0 = time()
print(get_min_coins(coins, amount))
t1 = time()
print("time:", t1 - t0)
print()
print(get_min_coins_rec(coins, amount))
print("time:", time() - t1)

from __future__ import annotations


def calculate_max_profit(prices: list[int]) -> int:

    cache: dict[tuple[bool, int], int] = {}

    def cache_profit(can_buy: bool, price_idx: int) -> int:
        if price_idx >= len(prices):
            return 0

        if (can_buy, price_idx) in cache:
            return cache[(can_buy, price_idx)]

        skip = cache_profit(can_buy, price_idx + 1)
        do_buy, do_sell = 0, 0
        if can_buy:
            do_buy = cache_profit(False, price_idx + 1) - prices[price_idx]
        else:
            do_sell = cache_profit(True, price_idx + 2) + prices[price_idx]

        max_prof = max(skip, do_buy, do_sell)
        cache[(can_buy, price_idx)] = max_prof
        return max_prof

    return cache_profit(True, 0)


prices = [1, 2, 3, 0, 2]
print(calculate_max_profit(prices))

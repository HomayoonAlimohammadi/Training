from __future__ import annotations
from typing import List
from dataclasses import dataclass
from datetime import datetime
from time import sleep
from random import choice, randint
from string import ascii_letters


@dataclass
class Order:
    """A dataclass containing Order details."""

    order_id: str
    order_date: datetime


class OrderManager:
    """A class to manage order logs."""

    def __init__(self, orders: List[Order] = None) -> None:
        self._log = [] if orders is None else orders

    def record(self, order_id: str) -> None:
        """Add order_id to the end of the log."""
        new_order = Order(order_id=order_id, order_date=datetime.now())
        self._log.append(new_order)

    def get_last(self, idx: int) -> Order:
        """Return `i_th` last order from the log."""
        return self._log[-idx]

    def __str__(self) -> str:
        result = f"OrderManager({[order for order in self._log]})"


def order_generator(n_orders: int) -> OrderManager:
    order_manager = OrderManager()
    for i in range(n_orders):
        order_id = "".join([choice(ascii_letters) for _ in range(10)])
        order_manager.record(order_id)
        sleep(0.02)

    return order_manager


def main():
    N_ORDERS = 100
    N_TEST = 10
    order_manager = order_generator(N_ORDERS)
    for _ in range(N_TEST):
        order_idx = randint(1, N_ORDERS - 1)
        order = order_manager.get_last(order_idx)
        print(f"{order_idx}th order: {order}")


if __name__ == "__main__":
    main()

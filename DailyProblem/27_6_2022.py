from typing import Callable
from time import sleep


def scheduler(f: Callable, n: int) -> None:
    """Calls `f` after `n` miliseconds."""
    sleep(n / 1000)
    f()


def func():
    print("Hello world!")


scheduler(func, 1000)

from typing import overload

@overload
def f(a: int) -> int:
    return a * 2

@overload
def f(a: str) -> str:
    return a * 10

def f(a: float) -> float:
    return a


a = 2.0
print(f(a))

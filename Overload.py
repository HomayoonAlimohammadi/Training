from functools import singledispatch

@singledispatch
def f(a: int) -> int:
    return a * 2

@f.register
def _(a: str) -> str:
    return a * 10

@f.register(float)
def _(a: float) -> float:
    return a


for a in [1, 1.0, '1']:
    print(f'For type: {type(a).__name__}, f returned: {f(a)}')
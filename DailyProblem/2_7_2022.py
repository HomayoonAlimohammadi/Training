import random
from string import ascii_letters
from typing import Any, Generator


def data_stream_gen(
    total_length: int | None = None, element_length: int = 100
) -> Generator[str, None, None]:
    if total_length is None:
        total_length == float("inf")
    idx = 0
    while idx < total_length:
        element = ""
        for el_length in range(element_length):
            element += random.choice(ascii_letters)
        yield element
        idx += 1


def n_th_data(data_gen: Generator[str, None, None], idx: int) -> str:
    for i in range(idx + 1):
        element = next(data_gen)
    return element


def solution(big_stream: Any) -> Any:
    random_element = None

    for idx, element in enumerate(big_stream):
        if idx == 0:
            random_element = element
        elif random.randint(1, idx + 1) == 1:  # prob of 1 in n
            random_element = element

    return random_element


TOTAL_LENGTH = 1_000_000
ELEMENT_LENGTH = 100
data = data_stream_gen(TOTAL_LENGTH, ELEMENT_LENGTH)
element_idx = random.randint(0, TOTAL_LENGTH)
print(n_th_data(data, element_idx))

from collections import deque


def solution(original_string: int, word_list: list[str]) -> list[str] | None:

    combs = deque([(original_string, [])])
    while combs:
        old_string, old_order = combs.popleft()
        for word in word_list:
            if old_string.startswith(word):
                new_string = old_string[len(word) :]
                new_order = old_order.copy() + [word]
                if len(new_string) == 0:
                    return new_order
                combs.append((new_string, new_order))

    return None


word_list = ["bedbath", "bed", "bath", "and", "beyond"]
original_string = "bedbathandbeyond"
print(solution(original_string, word_list))

word_list = ["bedbath", "bed", "bath", "beyond"]
original_string = "bedbathandbeyond"
print(solution(original_string, word_list))

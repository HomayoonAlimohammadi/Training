from collections import deque


def solution(original_string: int, word_list: list[str]) -> list[str] | None:

    combs = deque([(original_string, [])])
    results = []
    while combs:
        old_string, old_order = combs.popleft()
        for word in word_list:
            if old_string.startswith(word):
                new_string = old_string[len(word) :]
                new_order = old_order.copy() + [word]
                if len(new_string) == 0:
                    results.append(" ".join(new_order))
                else:
                    combs.append((new_string, new_order))

    return results


word_list = ["bedbath", "bed", "bath", "and", "beyond"]
original_string = "bedbathandbeyond"
print(solution(original_string, word_list))

word_list = ["bedbath", "bed", "bath", "beyond"]
original_string = "bedbathandbeyond"
print(solution(original_string, word_list))

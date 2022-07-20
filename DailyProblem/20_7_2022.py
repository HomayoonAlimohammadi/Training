from functools import lru_cache
from collections import Counter


def find_largest_palindromic_sub_sequences(string: str) -> list[str]:
    pal_sub_seqs = []
    start, end = 0, len(string)

    @lru_cache
    def check_pal(start, end) -> str:
        if start >= end or end > len(string):
            return
        sub_seq = string[start:end]
        if sub_seq == sub_seq[::-1]:
            if not pal_sub_seqs:
                pal_sub_seqs.append(sub_seq)
            elif len(sub_seq) >= len(pal_sub_seqs[-1]):
                while pal_sub_seqs and len(pal_sub_seqs[-1]) < len(sub_seq):
                    pal_sub_seqs.pop()
                pal_sub_seqs.append(sub_seq)
        check_pal(start + 1, end)
        check_pal(start, end - 1)

    check_pal(start, end)
    return pal_sub_seqs


def make_palindromic(string: str) -> str:
    pal_sub_seqs = find_largest_palindromic_sub_sequences(string)
    pal_sub_seqs.sort()
    sub_seq = pal_sub_seqs[0]
    start_idx = string.index(sub_seq)
    end_idx = start_idx + len(sub_seq)
    before, after = string[:start_idx], string[end_idx:]
    ...


string = "googleel"
print(make_palindromic(string))

def solution(words: list[str], max_width: int) -> list[str]:
    line_words = []
    line_length = 0
    final_text = []
    need_word = True
    while True:
        if need_word:
            if len(words) == 0:
                final_line = " ".join(line_words)
                final_line += " " * (max_width - len(final_line))
                final_text.append(final_line)
                break
            word = words.pop(0)
            need_word = False
        line_words.append(word)
        line_length += len(word)
        if len(line_words) == 1:
            need_word = True
            continue
        else:
            n_blanks = len(line_words) - 1
        space_dist = (max_width - line_length) / n_blanks
        if not (
            (line_length + n_blanks) <= max_width and space_dist == int(space_dist)
        ):
            bad_word = line_words.pop()
            if len(line_words) == 1:
                final_line = line_words[0] + " " * (max_width - len(line_words[0]))
            else:
                line_length -= len(bad_word)
                space_dist = (max_width - line_length) // n_blanks
                final_line = (" " * space_dist).join(line_words)
            final_text.append(final_line)
            line_words = []
            line_length = 0
        else:
            need_word = True

    return final_text


words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16
print(solution(words, max_width))


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
max_width = 16
print(solution(words, max_width))

words = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
max_width = 20
print(solution(words, max_width))

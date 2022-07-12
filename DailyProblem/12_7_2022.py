def find_last(string, target) -> int:
    if target not in string:
        return -1
    start = 0
    while string.find(target, start) != -1:
        start = string.find(target, start) + 1
    return start - 1


def my_regex(pattern: str, string: str) -> bool:
    idx = 0
    while idx < len(pattern):
        if pattern[idx] == ".":
            if len(string) == 0:
                return False
            string = string[1:]
            idx += 1
        elif pattern[idx] == "*":
            if idx < len(pattern) - 1:
                match = ""
                idx += 1
                while idx < len(pattern) and pattern[idx] not in [".", "*"]:
                    match += pattern[idx]
                    idx += 1
                shift_idx = find_last(string, match)
                if shift_idx == -1:
                    return False
                string = string[shift_idx + len(match) :]
            else:
                string = ""
                idx += 1
        else:
            if pattern[idx] == string[0]:
                string = string[1:]
                idx += 1
            else:
                return False
    return True if len(string) == 0 else False


pattern = ".*at*"
string = "chatats"
assert my_regex(pattern, string) == True

pattern = ".*at"
string = "chatat"
assert my_regex(pattern, string) == True

pattern = "ra."
string = "ray"
assert my_regex(pattern, string) == True

pattern = "ra."
string = "raymond"
assert my_regex(pattern, string) == False

pattern = "ra*"
string = "raymond"
assert my_regex(pattern, string) == True

pattern = "*ond"
string = "raymond"
assert my_regex(pattern, string) == True

print("All test cases passed.")

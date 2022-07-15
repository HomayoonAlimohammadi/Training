def encode(string: str) -> str:
    ref = string[0]
    cnt = 0
    encoded = ""
    while string:
        if string[0] == ref:
            string = string[1:]
            cnt += 1
        else:
            encoded += str(cnt) + ref
            ref = string[0]
            cnt = 0
    encoded += str(cnt) + ref
    return encoded


def decode(string: str) -> str:
    decoded = ""
    while string:
        cnt, ref = int(string[0]), string[1]
        string = string[2:]
        decoded += cnt * ref
    return decoded

string = 'AAAABBBCCDAA'
encoded = encode(string)
print(decode(encoded) == string)
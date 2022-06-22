from string import ascii_lowercase


def is_palindrome(string: str) -> bool:
    """
    Returns a `boolean` indicating whether
    a given string is a palindrome or not
    """
    for i in range(len(string)):
        if string[i] != string[len(string) - i - 1]:
            return False

    return True


def check_palindromable(string: str) -> bool:
    """
    Returns a boolean indicating whether a given
    string could be transformed to a palindrome
    by deleting only 1 character.
    """
    i, j = 0, len(string) - 1
    while i <= j:
        if string[i] != string[j]:
            if string[i + 1] == string[j]:
                return is_palindrome(string[i + 1 : j])
            elif string[j - 1] == string[i]:
                return is_palindrome(string[i:j])

            return False

        i += 1
        j -= 1


print(check_palindromable("abcbda"))
print(check_palindromable("abc"))
print(check_palindromable("abca"))
print(check_palindromable("ededde"))

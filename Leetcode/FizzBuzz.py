def play_fizz_buzz(last_num: int) -> None:

    SYMBOLS = {3: "Fizz", 5: "Buzz"}

    for num in range(1, last_num + 1):
        result = ""
        for n, symbol in SYMBOLS.items():
            if num % n == 0:
                result += symbol
        if result:
            print(f"{num}: {result}")
        else:
            print(num)


play_fizz_buzz(20)

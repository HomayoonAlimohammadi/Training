def get_n_permutations(coins: list[int], target: int) -> int:
    cache = {}
    coins = sorted(coins)

    def pick_coin(amount_left: int):
        if amount_left < 0 or amount_left in cache:
            return 0
        if amount_left == 0:
            return 1

        n_ways = 0
        for new_coin in coins:
            if new_coin > amount_left:
                break
            n_ways += pick_coin(amount_left - new_coin)
        cache[amount_left] = n_ways
        return n_ways

    res = pick_coin(target)
    print(cache)
    return res


def change_ways(coins: list[int], target: int) -> int:
    board = []
    for _ in range(len(coins)):
        row = [1] + [0 for _ in range(target)]
        board.append(row)
    coins = sorted(coins)
    for i, coin in enumerate(coins):
        for left in range(1, target + 1):
            until_now = board[i - 1][left] if i - 1 >= 0 else 0
            if_pick = board[i][left - coin] if left - coin >= 0 else 0
            board[i][left] = if_pick + until_now
    return board[-1][-1]


def print_board(board: list[list[int]]) -> None:
    print("#################################")
    print("Board:")
    for row in board:
        row = [str(el) for el in row]
        print(", ".join(row))
    print("#################################")


coins = [1, 2, 5]
target = 5
print(change_ways(coins, target))

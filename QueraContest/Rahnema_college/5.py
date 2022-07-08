n = int(input())
friends = []
for _ in range(n):
    f, b, m = [int(num) for num in input().split()]
    friends.append((f, b, m))


def pick(idx: int, total: int, picked: list[int]) -> int:
    if idx >= len(friends):
        return total

    for p_idx in picked:
        if (
            # khodesh nesbat be kasi hese badi dare
            (
                friends[idx][0] < friends[p_idx][0]
                and friends[idx][1] < friends[p_idx][1]
            )
            # baghie nesbat behesh hese badi daran
            or (
                friends[idx][0] > friends[p_idx][0]
                and friends[idx][1] > friends[p_idx][1]
            )
        ):
            return total

    dont_pick = pick(idx + 1, total, picked.copy())
    do_pick = pick(idx + 1, total + friends[idx][2], picked + [idx])
    total = max(dont_pick, do_pick)

    return total


max_total = pick(0, 0, list())
print(max_total)

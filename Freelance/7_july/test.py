from location import location


def solution(location):
    fin_location = []
    for loc in location:
        result = []
        for idx in range(len(loc) - 1):
            result.append(loc[idx + 1] - loc[idx])
        fin_location.append(result)

    return fin_location


ans = solution(location)
with open("./ans.txt", "w") as f:
    f.write(str(ans))

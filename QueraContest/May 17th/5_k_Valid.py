def k_valid_ineff(n: int, k: int):

    results = []
    for i in range(2**(2*n)):
        candid = format(i, 'b').zfill(2 * n)
        if candid.count('0') != candid.count('1'):
            continue

        candid = k*'1' + candid + k*'0'
        candid_org = candid
        open_num = 0
        close_num = 0
        while candid:
            if close_num > open_num:
                break
            if candid[0] == '1':
                open_num += 1
                candid = candid[1:]

            elif candid[0] == '0':
                close_num += 1
                candid = candid[1:]
        else:
            result = ''
            for char in candid_org:
                if char == '0':
                    result += ')'
                elif char == '1':
                    result += '('
            results.append(result[1:-1])

    return results


def k_valid(n, k):

    stack = []
    results = []

    def backtrack(openNum, closeNum):

        if openNum == closeNum == n:
            results.append(''.join(stack))
            return

        if openNum < n:
            stack.append('(')
            backtrack(openNum+1, closeNum)
            stack.pop()

        if closeNum < openNum + k:
            stack.append(')')
            backtrack(openNum, closeNum+1)
            stack.pop()

    backtrack(0, 0)
    return len(results)


results = []
t = int(input())
for i in range(t):
    n, k = input().split()
    n, k = int(n), int(k)
    results.append(k_valid(n, k))

for result in results:
    print(result)

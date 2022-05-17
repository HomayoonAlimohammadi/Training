from collections import Counter


n, m = input().split()
n, m = int(n), int(m)
cnt = Counter(input().split())
del cnt[' ']
if cnt.most_common(1)[0][1] <= n / 2:
    print('YES')
else:
    print('NO')


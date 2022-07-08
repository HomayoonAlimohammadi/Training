n = int(input())
for _ in range(n):
    vatar = int(input())
    n_tri = 0
    for l1 in range(1, vatar):
        for l2 in range(l1, vatar):
            if l1**2 + l2**2 == vatar**2:
                n_tri += 1
    print(n_tri)

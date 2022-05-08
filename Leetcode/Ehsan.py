from time import time


# t0 = time()
N, M = 22, 2

# output = []
total = 0

for i in range(1, len(str(N)) - 2 * len(str(M))):

    for j in range(10**i):

        # output.append(int(str(M) + str(j).zfill(i) + str(M)))
        total += 1

# output.append(2 * str(M))
# output.append(str(M))
total += 2


print(total % (10**9 + 7))
# print(time() - t0)
    
    

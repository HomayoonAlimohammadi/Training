def calculateSn(n: int, cache={}) -> str:
    
    if n == 1:
        cache[1] = 1
        return 1

    if n in cache:
        del cache[n-1]
        return cache[n]

    total = 0
    for digit in str(n):
        total += int(digit)
    ans = total + 2 * calculateSn(n-1)
    cache[n] = ans
    return ans


n = int(input())
prime = 10**9 + 7

ans = calculateSn(n)
print(ans % prime)
   

import bisect

def serie_cal():
    n = int(input())
    line = [int(i) for i in input().split()]
    serie = []
    for i in line:
        bisect.insort(serie, i)

    prime = 10**9 + 7
    
    if len(serie) == 1:
        return serie[0] 
    if len(serie) == 2:
        return max(serie[0]*serie[1], serie[0]+serie[1]) % prime

    n1, n2 = serie[-1], serie[-2]
    for i in range(n-2):
        if serie[i] == 1:
            if n1 > n2:
                n2 += 1
            else:
                n1 += 1
        else:
            n1 *= serie[i]

    return (n1 * n2) % prime

print(serie_cal())



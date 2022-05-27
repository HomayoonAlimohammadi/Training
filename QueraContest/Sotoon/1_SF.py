def calculate(n, sf):
    for i in range(n):
        result = sf[i] + sf[i+n]
        if result != 'SF' and result != 'FS':
            return 'NO'
    return 'YES'

n = int(input())
sf = input()

print(calculate(n, sf))
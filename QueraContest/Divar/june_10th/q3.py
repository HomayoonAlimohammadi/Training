from functools import lru_cache 


@lru_cache
def is_prime(n):
    if n < 10:
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 

    return True 

m = input()
for i in range(len(m)-1):
    sub = m[i:i+2]
    if sub.isdigit():
        if is_prime(int(sub)):
            print(sub)
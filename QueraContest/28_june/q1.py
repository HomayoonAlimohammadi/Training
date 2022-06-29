def solution(a: int, b: int) -> str:
    if a == 0:
        return 'infinite' if b == 0 else 'invalid'
    return 'unique'
    


a, b = input().split()
print(solution(int(a), int(b)))

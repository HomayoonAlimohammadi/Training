from string import ascii_lowercase 

alph = ascii_lowercase

def gharine2(word):
    mapping = list(map(lambda x: alph.index(x), word))
    for i in range(len(mapping) // 2):
        if abs(mapping[i] - mapping[-i-1]) > 2 or \
            abs(mapping[i] - mapping[-i-1]) == 1:
            return False 

    return True
        
    
n = int(input())
for i in range(n):
    word = input()
    res = gharine2(word)
    if res:
        print('YES')
    else:
        print('NO')
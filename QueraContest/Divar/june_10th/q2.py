m = input() + '!'
result = ''

ref = m[0]
inc = 0
for i in m:
    if i == ref:
        inc += 1 
    else:
        result += str(inc) + str(ref)
        ref = i
        inc = 1

print(result)
    
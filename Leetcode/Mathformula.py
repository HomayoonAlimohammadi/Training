def MissingDigit(strParam):

    eq, ans = strParam.split('=')
    ans = ans.strip()
    
    signs = '-+*/'

    for sign in signs:
        if sign in eq:
            operator = sign
            left, right = eq.split(sign)
            left, right = left.strip(), right.strip()
            break

    ops = {
        '+': (lambda x,y: x+y),
        '-': (lambda x,y: x-y),
        '*': (lambda x,y: x*y),
        '/': (lambda x,y: x/y)
    }
    reverse_ops = {
        '+': ops['-'],
        '-': ops['+'],
        '*': ops['/'],
        '/': ops['*']
    }

    if 'x' in ans:
        left, right = float(left), float(right)
        ans_2 = ops[operator](left, right)
        try:
            const = float(ans.replace('x', ''))
        except ValueError as e:
            const = 1
        return ans_2 / const

    if 'x' in left:
        ans, right = float(ans), float(right)
        ans_2 = reverse_ops[operator](ans, right)
        const = float(left.replace('x', ''))
        return ans_2 / const

    if 'x' in right:
        ans, left = float(ans), float(left)
        const = float(right.replace('x', ''))
        if operator in '/-':
            ans_2 = ops[operator](left, ans)
        elif operator in '+*':
            ans_2 = reverse_ops[operator](ans, left)

        return ans_2 / const



eq = '3 / x = 10'
print(MissingDigit(eq))
        



        

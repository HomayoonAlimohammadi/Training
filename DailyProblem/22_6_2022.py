def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    def left(a, b):
        return a

    return pair(left)


def cdr(pair):
    def right(a, b):
        return b

    return pair(right)


print(car(cons(2, 3)))
print(cdr(cons(2, 3)))

from math import factorial


def combinate(n, m):
    if n >= 0 and m >= 0 and m <= n:
        return factorial(n) / (factorial(n - m) * factorial(m))
    else:
        return "ERROR"


def combinate_repeat(n, m):
    if n >= 0 and m >= 0 and m <= n:
        return factorial(n + m - 1) / ((factorial(n - 1) * factorial(m)))
    else:
        return "ERROR"


a = combinate(4, 2)
b = combinate_repeat(6, 2)
c = combinate_repeat(7, 1)
print(a, b, c)

from math import factorial


def accomodate(n, m):
    if m <= n:
        return factorial(n) / factorial(n - m)
    else:
        return "ERROR"


def accomodate_repeat(n, m):
    return pow(n, m)


a = accomodate(10, 3)
b = accomodate_repeat(30, 15)

print(a, b)

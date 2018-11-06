from functools import reduce


def add(x, y):
    return x + y


s = reduce(add, [1, 3, 5, 7, 9])
print(s)


def fn(x, y):
    return x * 10 + y


r = reduce(fn, [1, 3, 5, 7, 9])
print(r)


c = list(map(int, list(iter("12345"))))
print(c)

d = reduce(fn, list(map(int, list(iter("12345")))))
print(d)


e = reduce(lambda x, y: x * 10 + y, list(map(int, list(iter("12345")))))
print(e)


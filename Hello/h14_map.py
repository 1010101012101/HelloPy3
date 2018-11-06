def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(r)
l = list(r)
print(l)

sl = list(map(str, map(f, list(range(1, 10)))))
print(sl)
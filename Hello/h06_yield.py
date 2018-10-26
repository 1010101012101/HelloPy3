
def func():
   for i in range(10):
        yield i


f = func()

print(f.__next__())

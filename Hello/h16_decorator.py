import functools

def now():
    print("2018-11-06")


f = now

f()

print(now.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print("2018-11-06")

now()
print(now.__name__)
print(now.__code__)
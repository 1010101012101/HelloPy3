def log(text):
    print("HHHA:0====>")
    def decorator(func):
        print("HHHA:0.1====>")
        def wrapper(*args, **kw):
            print("HHHA:0.1.1====>")
            return func(*args, **kw)
        print("HHHA:0.2====>")
        return wrapper
    print("HHHA:1====>")
    return decorator


@log('execute')
def now():
    print('HHHB:=====>test')


now()

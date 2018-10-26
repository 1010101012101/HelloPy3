TENSORFLOW_API_NAME = 'tensorflow'

class partial:

    def __new__(*args, **keywords):
        print("HHHA:0====>");
        if not args:
            raise TypeError("descriptor '__new__' of partial needs an argument")
        if len(args) < 2:
            raise TypeError("type 'partial' takes at least one argument")
        cls, func, *args = args
        if not callable(func):
            raise TypeError("the first argument must be callable")
        args = tuple(args)

        if hasattr(func, "func"):
            args = func.args + args
            tmpkw = func.keywords.copy()
            tmpkw.update(keywords)
            keywords = tmpkw
            del tmpkw
            func = func.func

        self = super(partial, cls).__new__(cls)

        self.func = func
        self.args = args
        self.keywords = keywords

        return self

    def __call__(*args, **keywords):
        if not args:
            raise TypeError("descriptor '__call__' of partial needs an argument")
        self, *args = args
        newkeywords = self.keywords.copy()
        newkeywords.update(keywords)
        print("HHHB:0====>");
        return self.func(*self.args, *args, **newkeywords)


def add(a, b):
    print("HHHF:0====>")
    return a + b


#addOne = partial(add, 1)

class api_export(object):  # pylint: disable=invalid-name
    """Provides ways to export symbols to the TensorFlow API."""

    def __init__(self, *args, **kwargs):
        print("HHHC:0====>");


    def __call__(self, func):
        print("HHHD:0====>");
        return func;


tf_export = partial(api_export, api_name=TENSORFLOW_API_NAME)


@tf_export('test.test_src_dir_path')
def hello_func(para=None):
    print("HHHE:0====>", para)


if __name__ == "__main__":
    print("Hello")
    #hello_func("YYY")
    #print(addOne(1))

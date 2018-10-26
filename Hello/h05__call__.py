class Person(object):
    def __new__(cls, aa):
        self = super(Person, cls).__new__(cls)
        print("HHHA:====>")
        return self

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print('My name is %s...' % self.name)
        print('My friend is %s...' % friend)

class ClassA(object):
    def __new__(cls, *args, **kwargs):
        object = super(ClassA, cls).__new__(cls)
        print("in New")
        return object

    def __init__(self, *args, **kwargs):
        print("in init")

    def __call__(self, func):
        print('HHHA:0====>', )
        return func

#p = Person("mc", "male")
@ClassA("Tim")
def hello():
    print("hello")

hello()

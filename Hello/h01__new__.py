class ClassA(object):
     def __new__(cls, *args, **kwargs):
         object = super(ClassA, cls).__new__(cls)
         print("in New")
         #return object


     def __init__(self, *args, **kwargs):
         print("in init")

ClassA()


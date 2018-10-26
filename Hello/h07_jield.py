import types
from collections import Iterable
#from inspect import isgeneratorfunction

def helloYield(n):
    print("HHHA:0====>")
    for i in range(n):
        print("HHHA:0.1====>")
        n = yield i
        print("HHHA:0.2====>", n)
    print("HHHA:1====>")


print("HHHH:0========>")
yieldReval = helloYield(5)
print("HHHH:1========>")
print("yieldReval is GeneratorType ? : ", isinstance(yieldReval, types.GeneratorType))
print("yieldReval is Iterable ? : ", isinstance(yieldReval, Iterable))
#print("Iterable ? : ", isgeneratorfunction(yieldObj))
print("HHHH:2========>")

for i in yieldReval:
    print("HHHB:0====>i=", i)
    if i == 1:
        print("HHHB:0.1====>send(99)")
        yieldReval.send(99)


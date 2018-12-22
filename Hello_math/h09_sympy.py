import numpy as np

from sympy import *


init_printing(use_unicode=True)
a,Wax,x,Waa,a_prev,b = symbols('a Wax x Waa a_prev b')  #用符号代表变量，多个变量可以空格，可以逗号隔开。
expr = tanh(Wax*x + Waa*a_prev + b)
expanded_expr = expand(x*expr) #expand 展开

#print("dx:",diff(expr, x))
print("dWax:",diff(expr, Wax))
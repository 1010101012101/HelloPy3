#from  sympy import *
import  sympy

from sympy import *
init_printing(use_unicode=True)
x,y = symbols('x y')  #用符号代表变量，多个变量可以空格，可以逗号隔开。
expr = x + 2*y
expanded_expr = expand(x*expr) #expand 展开
print(expanded_expr)


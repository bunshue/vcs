"""

python_king06_sympy

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
#SymPy-符號運算好幫手

from sympy import *

cc = E**(I*pi) + 1
print(cc)

x = symbols("x")
cc = expand( E**(I*x) )
print(cc)

cc = expand(exp(I*x), complex=True)
print(cc)

x = Symbol("x", real=True)
cc = expand(exp(I*x), complex=True)
print(cc)

tmp = series(exp(I*x), x, 0, 10)
print(tmp)

print(re(tmp))

cc = series(cos(x), x, 0, 10)
print(cc)

cc = im(tmp)
print(cc)

cc = series(sin(x), x, 0, 10)
print(cc)

#球體體積

cc = integrate(x*sin(x), x)
print(cc)

cc = integrate(x*sin(x), (x, 0, 2*pi))
print(cc)

x, y = symbols('x, y')
r = symbols('r', positive=True)
circle_area = 2 * integrate(sqrt(r**2 - x**2), (x, -r, r))
cc = circle_area
print(cc)

circle_area = circle_area.subs(r, sqrt(r**2 - x**2))
cc = circle_area
print(cc)

cc = integrate(circle_area, (x, -r, r))
print(cc)


#數值微分

x = symbols('x', real=True)
h = symbols('h', positive=True)
f = symbols('f', cls=Function)

f_diff = f(x).diff(x, 1)
print(f_diff)

""" no function
expr_diff = as_finite_diff(f_diff, [x, x-h, x-2*h, x-3*h])
print(expr_diff)
"""

sym_dexpr = f_diff.subs(f(x), x*exp(-x**2)).doit()
print(sym_dexpr)

sym_dfunc = lambdify([x], sym_dexpr, modules="numpy")
cc = sym_dfunc(np.array([-1, 0, 1]))
print(cc)

#array([-0.36787944,  1.        , -0.36787944])

#print(expr_diff.args)

#(-3*f(-h + x)/h, -f(-3*h + x)/(3*h), 3*f(-2*h + x)/(2*h), 11*f(x)/(6*h))

"""
w = Wild("w")
c = Wild("c")
patterns = [arg.match(c * f(w)) for arg in expr_diff.args]
print(patterns[0])
"""
#{w_: -h + x, c_: -3/h}

#coefficients = [t[c] for t in sorted(patterns, key=lambda t:t[w])]
#print(coefficients)

#coeff_arr = np.array([float(coeff.subs(h, 1e-3)) for coeff in coefficients])
#print(coeff_arr)

def moving_window(x, size):
    from numpy.lib.stride_tricks import as_strided    
    x = np.ascontiguousarray(x)
    return as_strided(x, shape=(x.shape[0] - size + 1, size), 
                      strides=(x.itemsize, x.itemsize))

x_arr = np.arange(-2, 2, 1e-3)
y_arr = x_arr * np.exp(-x_arr * x_arr)
# NG num_res = (moving_window(y_arr, 4) * coeff_arr).sum(axis=1)
sym_res = sym_dfunc(x_arr[3:])

# NG print(np.max(abs(num_res - sym_res)))
""" NG
def finite_diff_coefficients(f_diff, order, h):
    v = f_diff.variables[0]
    points = [x - i * h for i in range(order)]
    expr_diff = as_finite_diff(f_diff, points)
    w = Wild("w")
    c = Wild("c")
    patterns = [arg.match(c*f(w)) for arg in expr_diff.args]
    coefficients = np.array([float(t[c]) 
                             for t in sorted(patterns, key=lambda t:t[w])])
    return coefficients

#%figonly=比較不同點數的數值微分的誤差
fig, ax = pl.subplots(figsize=(8, 4))

for order in range(2, 5):
    c = finite_diff_coefficients(f_diff, order, 1e-3)
    num_diff = (moving_window(y_arr, order) * c).sum(axis=1)
    sym_diff = sym_dfunc(x_arr[order-1:])
    error = np.abs(num_diff - sym_diff)
    ax.semilogy(x_arr[order-1:], error, label=str(order))
    
ax.legend(loc="best");

plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sympy import *

#數學表達式
#符號

print(var("x0,y0,x1,y1"))

print(type(x0))
print(x0.name)
print(type(x0.name))

x1, y1 = symbols("x1, y1")
type(x1)

x2 = Symbol("x2")

t = x0
a, b = symbols("alpha, beta")
cc = sin(a) + sin(b) + t
print(cc)

m, n = symbols("m, n", integer=True)
x = Symbol("x", positive=True)   

cc =  [attr for attr in dir(x) if attr.startswith("is_") and attr.lower() == attr]

print(cc)

print(x.is_Symbol)
print(x.is_positive)
print(x.is_imaginary)
print(x.is_complex)

cc = x.assumptions0
print(cc)

cc = Symbol.mro()
print(cc)

#數值

print(1/2 + 1/3)
print(S(1)/2 + 1/S(3))

type(S(5)/6)

cc = Rational(5, 10) # 有理數會自動進行約分處理
print(cc)

print(N(0.1, 60))
print(N(10000.1, 60))

print(N(Float(0.1, 60), 60)) #用浮點數建立Real物件時，精度和浮點數相同
print(N(Float("0.1", 60), 60)) #用字串建立Real物件時，所特殊的精度有效
print(N(Float("0.1", 60), 65)) #精度再高，也不是完全精確的

print(N(pi, 50))
print(N(sqrt(2), 50))

#運算符和函數

var("x, y, z")
Add(x, y, z)

cc = Add(Mul(x, y, z), Pow(x, y), sin(z))
print(cc)

cc = x*y*z + x**y + sin(z)
print(cc)

t = x - y
print(t.func)
print(t.args)
print(t.args[0].func)
print(t.args[0].args)

#%fig=表達式的樹狀結構
from sympy.printing.dot import dotprint
graph = dotprint(x * y * sqrt(x ** 2 - y ** 2) / (x + y))
#%dot -f svg graph

#b'\r\n\r\n\r\n\r\nMulxyPowPowAdd-1yxAdd1/2MulPow-1Powy2x2

f = Function("f")

cc = issubclass(f, Function)
print(cc)

#True

t = f(x, y)
print(type(t))
print(t.func)
print(t.args)

t + t * t

"""
#通配符

    TIP
    執行SymPy提供的init_printing()可以使用數學符號顯示運算結果。
    但它會將Python的內建物件也轉換成LateX顯示。為了撰寫方便，本書使用一般文字顯示內建物件，
    而用本書提供的%sympy_latex魔法方法將內建物件轉為LaTeX。
"""

x, y = symbols("x, y")
a = Wild("a")
b = Wild("b")

cc = (3 * x * (x + y)**2).match(a * b**2)
print(cc)

expr = expand((x + y)**3)
print(expr)
print(expr.find(a * b**2))

def find_match(expr, pattern):
    return [e.match(pattern) for e in expr.find(pattern)]

  
find_match(expr, a * b**2);

#表達式 	比對結果

a = Wild("a", exclude=[1])
b = Wild("b", exclude=[1, Pow])

find_match(expr, a * b**2);

#表達式 	比對結果

expr.replace(a * b**2, (a + b)**2)

expr = sqrt(x) / sin(y**2) + abs(exp(x) * x)

find_match(expr, f);

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sympy import *
import sympy
from IPython.display import Latex

#%init_sympy_printing
x, y, z = symbols("x, y, z")
a, b = symbols("a, b")
f = Function("f")

#符號運算
#表達式變換和化簡

cc = simplify((x + 2) ** 2 - (x + 1) ** 2)
print(cc)

cc = radsimp(1 / (sqrt(5) + 2 * sqrt(2)))
print(cc)

cc = radsimp(1 / (y * sqrt(x) + x * sqrt(y)))
print(cc)

cc = ratsimp(x / (x + y) + y / (x - y))
print(cc)

print(fraction(ratsimp(1 / x + 1 / y)))

print(fraction(1 / x + 1 / y))

cc = cancel((x ** 2 - 1) / (1 + x))
print(cc)

s = symbols("s")
trans_func = 1/(s**3 + s**2 + s + 1)
cc = apart(trans_func)
print(cc)

cc = trigsimp(sin(x) ** 2 + 2 * sin(x) * cos(x) + cos(x) ** 2)
print(cc)

cc = expand_trig(sin(2 * x + y))
print(cc)

from tabulate import tabulate
from IPython.display import Markdown, display_markdown
flags = ["mul", "log", "multinomial", "power_base", "power_exp"]
expressions = [x * (y + z), log(x * y ** 2), (x + y) ** 3, (x * y) ** z, x ** (y + z)]
infos =[u"展開乘法", u"展開對數函數的參數中的乘積和冪運算", 
        u"展開加減法表達式的整數次冪", u"展開冪函數的底數乘積", u"展開對冪函數的指數和"]
table = []
for flag, expression, info in zip(flags, expressions, infos):
    table.append(["`{}`".format(flag), 
                  "`expand({})`".format(expression), 
                  "${}$".format(latex(expand(expression))),
                 info])

display_markdown(Markdown(tabulate(table, [u"標志", u"表達式", u"結果", u"說明"], "pipe")))


x, y, z = symbols("x,y,z", positive=True)
cc = expand(x * log(y * z), mul=False)
print(cc)

from tabulate import tabulate
from IPython.display import Markdown

flags = ["complex", "func", "trig"]
expressions = [x * y, gamma(1 + x), sin(x + y)]
infos =[u"展開乘法", u"展開對數函數的參數中的乘積和冪運算", 
        u"展開加減法表達式的整數次冪", u"展開冪函數的底數乘積", u"展開對冪函數的指數和"]
table = []
for flag, expression, info in zip(flags, expressions, infos):
    table.append(["`{}`".format(flag), 
                  "`expand({})`".format(expression), 
                  "${}$".format(latex(expand(expression))),
                 info])

display_markdown(Markdown(tabulate(table, [u"標志", u"表達式", u"結果", u"說明"], "pipe")))

x, y = symbols("x,y", complex=True)
cc = expand(x * y, complex=True)
print(cc)

cc = expand(gamma(1 + x), func=True)
print(cc)

cc = expand(sin(x + y), trig=True)
print(cc)

cc = factor(15 * x ** 2 + 2 * y - 3 * x - 10 * x * y)
print(cc)

eq = (1 + a * x) ** 3 + (1 + b * x) ** 2
eq2 = expand(eq)
cc = collect(eq2, x)
print(cc)

p = collect(eq2, x, evaluate=False)
print(p[S(1)])
print(p[x**2])

print(eq2.coeff(x, 0))
print(eq2.coeff(x, 2))

cc = collect(a * sin(2 * x) + b * sin(2 * x), sin(2 * x))
print(cc)

#方程式

a, b, c = symbols("a,b,c")
print(solve(a * x ** 2 + b * x + c, x))

print(solve((x ** 2 + x * y + 1, y ** 2 + x * y + 2), x, y))

print(roots(x**3 - 3*x**2 + x + 1))

#微分

t = Derivative(sin(x), x)
print(t)

cc = t.doit()
print(cc)

cc = diff(sin(2*x), x)
print(cc)

cc = Derivative(f(x), x)
print(cc)

cc = Derivative(f(x), x, x, x) # 也可以寫作Derivative(f(x), x, 3)
print(cc)

cc = Derivative(f(x, y), x, 2, y, 3)
print(cc)

cc = diff(sin(x * y), x, 2, y, 3)
print(cc)


#微分方程式

x=symbols('x')
f=symbols('f', cls=Function)
cc = dsolve(Derivative(f(x), x) - f(x), f(x))
print(cc)

eq = Eq(f(x).diff(x) + f(x), (cos(x) - sin(x)) * f(x)**2)
cc = classify_ode(eq, f(x))
print(cc)

cc = dsolve(eq, f(x))
print(cc)

cc = dsolve(eq, f(x), hint="lie_group")
print(cc)

cc = dsolve(eq, f(x), hint="all")
print(cc)

"""
cc = sympy.ode.allhints
print(cc)
"""

#積分

e = Integral(x*sin(x), x)
print(e)

cc = e.doit()
print(cc)

e2 = Integral(sin(x)/x, (x, 0, 1))
cc = e2.doit()
print(cc)

print(e2.evalf())
print(e2.evalf(50)) # 可以指定精度

e3 = Integral(sin(x)/x, (x, 0, oo))
cc = e3.evalf()
print(cc)

cc = e3.doit()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sympy import *
import sympy
from IPython.display import Latex
#%init_sympy_printing

x, y, z = symbols("x, y, z")
a, b = symbols("a, b")
f = Function("f")

#輸出符號表達式
#lambdify

a, b, c, x = symbols("a, b, c, x", real=True)
quadratic_roots = solve(a*x**2 + b*x + c, x)
lam_quadratic_roots_real = lambdify([a, b, c], quadratic_roots)
lam_quadratic_roots_real(2, -3, 1)

#[1.0, 0.5]

import cmath
lam_quadratic_roots_complex = lambdify((a, b, c), quadratic_roots, modules=cmath)
lam_quadratic_roots_complex(2, 2, 1)

#[(-0.5+0.5j), (-0.5-0.5j)]

lam_quadratic_roots_numpy = lambdify((a, b, c), quadratic_roots, modules="numpy")
A = np.array([2, 2, 1, 2], np.complex) 
B = np.array([1, 4, 2, 1], np.complex) 
C = np.array([1, 1, 1, 2], np.complex)
cc = lam_quadratic_roots_numpy(A, B, C)
print(cc)

#用autowrap()編譯表達式
""" NG
from sympy.utilities.autowrap import autowrap
matrix_roots = Matrix(quadratic_roots)
quadratic_roots_f2py   = autowrap(matrix_roots, args=[a, b, c], tempdir=r".\tmp")
quadratic_roots_cython = autowrap(matrix_roots, args=[a, b, c], tempdir=r".\tmp",
                                 backend="cython", flags=["-I" + np.get_include()])

print(quadratic_roots_f2py(2, -3, 1))
print(quadratic_roots_cython(2, -3, 1))

from sympy.utilities.autowrap import ufuncify
quadratic_roots_ufunc = ufuncify((a, b, c), quadratic_roots[0], tempdir=r".\tmp")

quadratic_roots_ufunc([1, 2, 10.0], [6, 7, 12.0], [4, 5, 1.0])

array([-0.76393202, -1.        , -0.09009805])

from sympy.utilities.codegen import codegen
(c_name, c_code), (h_name, c_header) = codegen(
    [("root0", quadratic_roots[0]), 
     ("root1", quadratic_roots[1]), 
     ("roots", matrix_roots)], 
    language="C", 
    prefix="quadratic_roots", 
    header=False)
print(h_name)
print("-" * 40)
print(c_header)
print()
print(c_name)
print("-" * 40)
print(c_code)

print(ccode(matrix_roots, assign_to="y"))

#使用cse()分步輸出表達式

replacements, reduced_exprs = cse(quadratic_roots)
print(replacements)

print(reduced_exprs)

replacements, reduced_exprs = cse(quadratic_roots, symbols=numbered_symbols("tmp"))
print(replacements)

def cse_quadratic_roots(a, b, c):
    from math import sqrt
    _tmp0 = 0.5/a
    _tmp1 = sqrt((b)**(2.0) - 4.0*a*c)
    return (_tmp0*(_tmp1 - b), -_tmp0*(_tmp1 + b))

cse_quadratic_roots(1, -4, 2)

#(3.41421356237, 0.585786437627)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
from matplotlib import pyplot as plt
from sympy import *
#%init_sympy_printing

#機械運動類比
#推導系統的微分方程式

from sympy.physics.mechanics import *

I = ReferenceFrame('I')                # 定義慣性參照系
O = Point('O')                         # 定義原點
O.set_vel(I, 0)                        # 設定點O在參照系I中的速度為0
g = symbols("g")


"""
    LINK

    http://www.pydy.org/

    本節只介紹mechanics模組最基本的用法，若讀者對使用SymPy求解多剛系統統感興趣，
    可以參考PyDy延伸庫。
"""
q = dynamicsymbols("q")
u = dynamicsymbols("u")
m1 = symbols("m1")
P1 = Point('P1')                    
P1.set_pos(O, q * I.x)              # 點P1的位置相對於點O，沿著參照系I的X軸偏移q
P1.set_vel(I, u * I.x)              # 點P1在參照系I中的速度為X軸方向，大小為u
box = Particle('box', P1, m1)       # 在點P1處放置質量為m1的方塊box

print(q, u)

th = dynamicsymbols("theta")
w  = dynamicsymbols("omega")
B = I.orientnew('B', 'Axis', [th, I.z])  # 將I圍繞Z軸旋轉theta得到參照系B
B.set_ang_vel(I, w * I.z)                # 設定B的角速度

l, m2 = symbols("l,m2")
P2 = P1.locatenew('P2', -l * B.y)  # P2相對於P1沿著B的Y軸負方向偏移l
P2.v2pt_theory(P1, I, B)           # 使用二點理論設定P2在I中的速度
ball = Particle('ball', P2, m2)    # 在P2處放置質量為m2的小球 

cc = P2.vel(I) #顯示P2在I中的速度
print(cc)

eqs = [q.diff() - u, th.diff() - w] #q的導數為u，th的導數為w
kane = KanesMethod(I, q_ind=[q, th], u_ind=[u, w], kd_eqs=eqs)

""" NG
particles = [box, ball]  #系統包括的所有質點
forces = [(P1, -m1*g*I.y), (P2, -m2*g*I.y)] #系統所受的外力
fr, frstar = kane.kanes_equations(forces, particles)

print(Eq(fr[0] + frstar[0], 0))
print(Eq(fr[1] + frstar[1], 0))

from IPython import display
status = Matrix([[q],[th],[u],[w]])
display.Math(latex(kane.mass_matrix_full) + latex(status.diff()) + 
             "=" + latex(kane.forcing_full))
#將符號表達式轉為程式

diff_status = kane.mass_matrix_full.inv() * kane.forcing_full

from sympy.utilities.autowrap import autowrap
status_symbols = [Symbol(sym.func.__name__) for sym in status] #❶
expr = diff_status.subs(zip(status, status_symbols)) #❷

from sympy.utilities.autowrap import autowrap
_func_diff_status = autowrap(expr, args=[m1, m2, l, g] + status_symbols, tempdir=r".\tmp_mechanics") #❸

def func_diff_status(status, t, m1, m2, l, g):
    q, th, u, w = status
    return _func_diff_status(m1, m2, l, g, q, th, u, w).ravel()

init_status = np.array([0, np.deg2rad(45), 0, 0])
args = 1.0, 2.0, 1.0, 9.8
func_diff_status(init_status, 0, *args)

#array([  0.        ,   0.        ,   4.9       , -10.39446968])

#%fig=使用`odeint()`計算的運動軌跡
from scipy.integrate import odeint

t = np.linspace(0, 10, 500)
res = odeint(func_diff_status, init_status, t, args=args)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, res[:, 0], label=u"$q$")
ax1.legend()
ax2.plot(t, res[:, 1], label=u"$\\theta$")
ax2.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

#動畫示範

from matplotlib import animation
from matplotlib.patches import Rectangle, Circle
from matplotlib.lines import Line2D

def animate_system(t, states, blit=True):
    q, th, u, w = states.T
    fig = plt.figure()
    w, h = 0.2, 0.1
    ax = plt.axes(xlim=(-0.5, 1.5), ylim=(-1.5, 0.5), aspect='equal')

    rect = Rectangle([q[0], 0,  - w / 2.0, - h / 2],
        w, h, fill=True, color='red', ec='black', axes=ax, animated=blit)
    ax.add_patch(rect)
    
    line = Line2D([], [], lw=2, marker='o', markersize=6, animated=blit, axes=ax)
    ax.add_artist(line)
    
    circle = Circle((0, 0), 0.1, axes=ax, animated=blit)
    ax.add_patch(circle)

    def animate(i):
        x1, y1 = q[i], 0
        l = 1.0
        x2, y2 = l*sin(th[i]) + x1, -l*cos(th[i]) + y1
        rect.set_xy((x1-w*0.5, y1))
        line.set_data([x1, x2], [y1, y2])
        circle.center = x2, y2
        return rect, line, circle
    
    anim = animation.FuncAnimation(fig, animate, frames=len(t),
            interval=t[-1] / len(t) * 1000, blit=blit, repeat=False)
        
    return anim

anim = animate_system(t, res);
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



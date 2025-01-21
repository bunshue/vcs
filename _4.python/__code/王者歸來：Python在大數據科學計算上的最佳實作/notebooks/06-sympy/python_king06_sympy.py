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

from sympy import *
import sympy
from IPython.display import Latex  # 用IPython
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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個



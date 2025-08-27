"""
ortools

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
汽车排程问题
一定数量的汽车需要在一条装配线上进行装配，每个汽车有不同的装配选项，例如空调、导航等。装配线依次通过多个安装不同选项的装配点，每个装配点需要一定的时间完成一个装配项目的装配，装备所需要的时间使用汽车的间隔数标准化，例如空调的装配每两辆车能装配一辆车。
所谓汽车排序问题就是找到一个装配线上排列顺序，使得它满足每个装配点间隔要求。在下表中，一共有5个装配选项，每个装配选项所需的工作时间由m/N指定，即每N辆车能够装配m个。例如Option 2的m/N为2/3表示每3辆车能够装配两个。Car Class为车型，本例中有6种车型，表中列出了每个车型对应的装配选项。例如Car Class 4需要装配Option 2和Option 4。最后Number of Cars给出了每种车型的数量。
"""

from ortools.constraint_solver import pywrapcp
from itertools import chain
from IPython.display import display_html
import numpy as np


#下面首先定义前表中的各种数据。

n_car_types = 6
n_options = 5
car_demand = [1, 1, 2, 2, 2, 2]
n_slots = sum(car_demand)

car_types = list(range(n_car_types))
options = list(range(n_options))
slots = list(range(n_slots))

car_option = [
#car 0  1  2  3  4  5
    [1, 0, 0, 0, 1, 1],  # option 1
    [0, 0, 1, 1, 0, 1],  # option 2
    [1, 0, 0, 0, 1, 0],  # option 3
    [1, 1, 0, 1, 0, 0],  # option 4
    [0, 0, 1, 0, 0, 0]   # option 5
]

option_car = list(zip(*car_option))

capacity = [
  (1, 2),
  (2, 3),
  (1, 3),
  (2, 5),
  (1, 5)
]

# 为了方便后续添加约束条件，vars_all是一个嵌套列表，其中的每个元素是表示每个时隙(slot)对应的汽车型号的布尔变量列表，该列表的长度为汽车型号数。

solver = pywrapcp.Solver("Car sequence")
vars_all = [[solver.IntVar(0, 1, "slot[%d, %d]" % (i, j)) for j in car_types] for i in slots]
vars_all_flat = list(chain.from_iterable(vars_all))

# vars_all中的每个列表中的所有变量中，有且只有一个变量为1。

for vars_slot in vars_all:
    solver.Add(solver.Sum(vars_slot) == 1)    

# 每种型号出现的次数应该等于demand，这里使用zip(*vars_all)对vars_all进行转置，得到嵌套列表长度为n_car_types，每个元素是一个长度为n_slots的列表，表示每个时隙是否为某种型号。

for vars_type, demand in zip(zip(*vars_all), car_demand):
    solver.Add(solver.Sum(vars_type) == demand)

# 对于每个选项，添加capacity的约束条件：连续N个时隙中只能最多出现m次。这里对所有可能的连续N时隙进行循环，将每个时隙上汽车型号通过car_option转换为其对应的选项，并添加进vars_option中。vars_option中所有变量的和就是该型号出现的次数。

for i, option in enumerate(car_option):
    m, N = capacity[i]
    for start in range(n_slots - N + 1):
        vars_option = []
        for vars_ in vars_all[start:start + N]:
            vars_option.extend([v for k, v in enumerate(vars_) if option[k]])
        solver.Add(solver.Sum(vars_option) <= m)

# 下面计算所有的解，并将得到的布尔数组转换为其对应的型号，以及每个型号对应的选项。由结果可知，Opt0连续2个时隙一个为1，Opt1连续3个时隙最多只有两个为1，它们都满足capacity给定的约束条件。

import pandas as pd

db = solver.Phase(vars_all_flat,
                    solver.CHOOSE_FIRST_UNBOUND,
                    solver.ASSIGN_MIN_VALUE)

solver.NewSearch(db)
columns = ["S%d" % s for s in slots]
index = ["Type"] + ["Opt%d" % o for o in options]

while solver.NextSolution():
    solution = [[v.Value() for v in vars_slot].index(1) for vars_slot in vars_all]
    option_seq = [option_car[c] for c in solution]
    data = np.vstack((solution, np.array(option_seq).T))
    df = pd.DataFrame(data, index=index, columns=columns)
    display_html(df)
solver.EndSearch()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ortools的约束求解器入门-解硬币问题

# ortools是Google公司开发的组合优化工具，它提供了约束求解器、线性规划、图相关算法、背包算法以及解决旅行推销员等问题的组合优化算法。本文简单介绍其约束求解器的用法。

# 基本用法

# 可以从PyPI下载whl二进制包，然后使用pip install py3_ortools-....whl安装。然后使用下面的import命令载入constraint_solver库。

from ortools.constraint_solver import pywrapcp

# 求解约束问题从创建Solver对象solver开始，其后调用solver的方法创建各种所需的对象。下面创建四个IntVar变量，并将其保存于列表x中。IntVar()的参数为取值范围的开始值、结束值以及变量名。

solver = pywrapcp.Solver("test")

x = [solver.IntVar(0, 3, "x%d" % i) for i in range(4)]
print(x)

# [x0(0..3), x1(0..3), x2(0..3), x3(0..3)]

cs = solver.AllDifferent(x)
solver.Add(cs)
print(cs)

#BoundsAllDifferent(x0(0..3), x1(0..3), x2(0..3), x3(0..3))

#下面创建Assignment对象保存解，并创建解收集器AllSolutionCollector收集所有的解。

solution = solver.Assignment()
solution.Add(x)
collector = solver.AllSolutionCollector(solution)

#下面创建搜索用的Phase对象，其参数为需要进行搜索的变量列表，变量选择算法，值选择算法。

phase = solver.Phase(x, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
print(phase)

#ChooseFirstUnbound_SelectMinValue(x0(0..3), x1(0..3), x2(0..3), x3(0..3))

#最后调用Solve()方法对Phase对象求解，并收集解，返回True表示找到了解。

print(solver.Solve(phase, [collector]))

#True

"""
下面使用collector提供的各种方法提取所有的解。

    SolutionCount()返回解的数量
    Solution(i)返回第i个解

每个解是一个Assignment对象。通过其IntVarContainer()获取包含解中的所有变量的IntContainer对象。该对象的Size()方法获取其中的元素个数，Element(i)获取其第i个元素。每个元素是一个IntVarElement对象，其Value()方法获取该元素对应的解，Val()方法获取该元素对应的IntVar变量。

这里显示的解就是整数0, 1, 2, 3的全排列。
"""

for i in range(collector.SolutionCount()):
    s = collector.Solution(i)
    sc = s.IntVarContainer()
    res = []
    for j in range(sc.Size()):
        el = sc.Element(j)
        print("{}={}".format(el.Var().Name(), el.Value()), end=" ")
    print()

"""
x0=0 x1=1 x2=2 x3=3 
x0=0 x1=1 x2=3 x3=2 
x0=0 x1=2 x2=1 x3=3 
x0=0 x1=2 x2=3 x3=1 
x0=0 x1=3 x2=1 x3=2 
x0=0 x1=3 x2=2 x3=1 
x0=1 x1=0 x2=2 x3=3 
x0=1 x1=0 x2=3 x3=2 
x0=1 x1=2 x2=0 x3=3 
x0=1 x1=2 x2=3 x3=0 
x0=1 x1=3 x2=0 x3=2 
x0=1 x1=3 x2=2 x3=0 
x0=2 x1=0 x2=1 x3=3 
x0=2 x1=0 x2=3 x3=1 
x0=2 x1=1 x2=0 x3=3 
x0=2 x1=1 x2=3 x3=0 
x0=2 x1=3 x2=0 x3=1 
x0=2 x1=3 x2=1 x3=0 
x0=3 x1=0 x2=1 x3=2 
x0=3 x1=0 x2=2 x3=1 
x0=3 x1=1 x2=0 x3=2 
x0=3 x1=1 x2=2 x3=0 
x0=3 x1=2 x2=0 x3=1 
x0=3 x1=2 x2=1 x3=0 
"""

# 给了使用更Python化的语法，下面为SolutionCollector和IntContainer类添加__len__()和__getitem__()方法。为Assignment类添加intvars属性，为IntVarElement类添加name和value属性。

def SolutionCollector__len__(self):
    return self.SolutionCount()

def SolutionCollector__getitem__(self, index):
    if index < len(self):
        return self.Solution(index)
    else:
        raise IndexError("index out of range {} of {}".format(index, len(self)))

def IntContainer__getitem__(self, index):
    if index < len(self):
        return self.Element(index)
    else:
        raise IndexError("index out of range {} of {}".format(index, len(self)))
        
pywrapcp.SolutionCollector.__len__ = lambda self: self.SolutionCount()
pywrapcp.SolutionCollector.__getitem__ = SolutionCollector__getitem__

""" NG
pywrapcp.Assignment.intvars = property(lambda self: self.IntVarContainer())
pywrapcp.IntContainer.__len__ = lambda self: self.Size()
pywrapcp.IntContainer.__getitem__ = IntContainer__getitem__
pywrapcp.IntVarElement.name = property(lambda self: self.Var().Name())
pywrapcp.IntVarElement.value = property(lambda self: self.Value())

# 于是我们可以使用下面的程序获取所有的解：

for sl in collector:
    print([(el.name, el.value) for el in sl.intvars])
"""

"""
[('x0', 0), ('x1', 1), ('x2', 2), ('x3', 3)]
[('x0', 0), ('x1', 1), ('x2', 3), ('x3', 2)]
[('x0', 0), ('x1', 2), ('x2', 1), ('x3', 3)]
[('x0', 0), ('x1', 2), ('x2', 3), ('x3', 1)]
[('x0', 0), ('x1', 3), ('x2', 1), ('x3', 2)]
[('x0', 0), ('x1', 3), ('x2', 2), ('x3', 1)]
[('x0', 1), ('x1', 0), ('x2', 2), ('x3', 3)]
[('x0', 1), ('x1', 0), ('x2', 3), ('x3', 2)]
[('x0', 1), ('x1', 2), ('x2', 0), ('x3', 3)]
[('x0', 1), ('x1', 2), ('x2', 3), ('x3', 0)]
[('x0', 1), ('x1', 3), ('x2', 0), ('x3', 2)]
[('x0', 1), ('x1', 3), ('x2', 2), ('x3', 0)]
[('x0', 2), ('x1', 0), ('x2', 1), ('x3', 3)]
[('x0', 2), ('x1', 0), ('x2', 3), ('x3', 1)]
[('x0', 2), ('x1', 1), ('x2', 0), ('x3', 3)]
[('x0', 2), ('x1', 1), ('x2', 3), ('x3', 0)]
[('x0', 2), ('x1', 3), ('x2', 0), ('x3', 1)]
[('x0', 2), ('x1', 3), ('x2', 1), ('x3', 0)]
[('x0', 3), ('x1', 0), ('x2', 1), ('x3', 2)]
[('x0', 3), ('x1', 0), ('x2', 2), ('x3', 1)]
[('x0', 3), ('x1', 1), ('x2', 0), ('x3', 2)]
[('x0', 3), ('x1', 1), ('x2', 2), ('x3', 0)]
[('x0', 3), ('x1', 2), ('x2', 0), ('x3', 1)]
[('x0', 3), ('x1', 2), ('x2', 1), ('x3', 0)]

为了今后使用方便，在ortoolshelp模块中除了定义了下面两个函数。

    iter_solution(collector): 返回所有解的生成器。
    solve(solver, variables, collector_name): 对solver中的variables求解，collector_name指定解收集器。First表示搜集一个解，All表示搜集所有解。
"""

def iter_solutions(collector):
    for assignment in collector:
        yield [(el.name, el.value) for el in assignment.intvars]

def solve(solver, variables, collector_name="First"):
    solution = solver.Assignment()
    solution.Add(variables)
    collector = getattr(solver, collector_name + "SolutionCollector")(solution)
    phase = solver.Phase(variables, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
    if solver.Solve(phase, [collector]):
        return iter_solutions(collector)
    else:
        return ()

"""
硬币问题

下面看一个实际的组合问题。

用面值为1, 2, 5, 10, 25, 50的硬币凑齐100，列举所有硬币枚数小于等于7的所有可能。

下面的x列表保存每种硬币出现的次数，次数的取值范围为0到max_coins。ScalProd(x, coins)将x和coins中的对应元素相乘，并计算总和，它返回的是一个包含IntVar变量的表达式。然后使用==比较运算符创建约束条件，并添加进solver。Sum(x)计算x的元素和，它得到的也是一个表达式，然后使用<=运算符创建约束条件。
"""

coins = [1, 2, 5, 10, 25, 50]
total = 100
max_coins = 7
n = len(coins)

solver = pywrapcp.Solver("coins")
x = [solver.IntVar(0, max_coins, "%d" % c) for c in coins]
solver.Add(total == solver.ScalProd(x, coins))
solver.Add(solver.Sum(x) <= max_coins)

""" NG
for sol in solve(solver, x, collector_name="All"):
    print(", ".join("{}:{}".format(*item) for item in sol if item[1] > 0))
"""

"""
50:2
25:2, 50:1
25:4
10:5, 50:1
10:5, 25:2
5:1, 10:2, 25:1, 50:1
5:1, 10:2, 25:3
5:2, 10:4, 50:1
5:3, 10:1, 25:1, 50:1
5:3, 10:1, 25:3
5:5, 25:1, 50:1
1:1, 2:2, 10:2, 25:1, 50:1
"""

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用SearchMonitor观察ortools的搜索过程

from ortools.constraint_solver import pywrapcp

# ortools中提供了SearchMonitor用以观察搜索过程，下面的LogMonitor类从SearchMonitor继承，显示所有的搜索事件。

# 显示所有的搜索事件

class LogMonitor(pywrapcp.SearchMonitor):
    def EnterSearch(self):
        print("EnterSearch")

    def RestartSearch(self):
        print("RestartSearch")

    def ExitSearch(self):
        print("ExitSearch")

    def BeginNextDecision(self, b):
        print("BeginNextDecision", b)

    def EndNextDecision(self, b, d):
        print("EndNextDecision", b, d)

    def ApplyDecision(self, d):
        print("ApplyDecision", d)

    def RefuteDecision(self, d):
        print("RefuteDecision", d)

    def AfterDecision(self, d, apply):
        print("AfterDecision", d, apply)

    def BeginFail(self):
        print("BeginFail")

    def EndFail(self):
        print("EndFail")

    def BeginInitialPropagation(self):
        print("BeginInitialPropagation")

    def EndInitialPropagation(self):
        print("EndInitialPropagation")

    def AcceptSolution(self):
        print("AcceptSolution")
        return super().AcceptSolution()

    def AtSolution(self):
        print("AtSolution")
        return super().AtSolution()

    def NoMoreSolutions(self):
        print("NoMoreSolutions")

# 下面显示三个整数全排列的搜索过程。

solver = pywrapcp.Solver("test")
x = [solver.IntVar(1, 3, name) for name in "ABC"]
solver.Add(solver.AllDifferent(x))

log_monitor = LogMonitor(solver)

# 观察搜索树

class TreeMonitor(pywrapcp.SearchMonitor):
    def EnterSearch(self):
        self.from_node = []
        self.edge = []
        self.graph = []
        self.ignore_next_fail = False
        self.fail_count = 0
        
    def BeginNextDecision(self, b):
        node_text = str(b)
        node_text = node_text[node_text.index("("):][1:-1]
        if self.from_node and self.edge:
            self.graph.append([self.from_node[-1], self.edge[-1], node_text])
        self.from_node.append(node_text)
        
    def ApplyDecision(self, d):
        self.edge.append(str(d)[1:-1])
        
    def EndNextDecision(self, b, d):
        pass
        
    def RefuteDecision(self, d):
        edge = str(d)[1:-1]
        while self.edge[-1] != edge:
            self.edge.pop()
            self.from_node.pop()
        self.edge.pop()
        self.from_node.pop()
        self.edge.append("!" + edge)
        
    def AcceptSolution(self):
        self.ignore_next_fail = True
        return True
        
    def BeginFail(self):
        if not self.ignore_next_fail:
            self.fail_count += 1
            node_text = "Fail{}".format(self.fail_count)
            if self.from_node and self.edge:
                self.graph.append([self.from_node[-1], self.edge[-1], node_text])
            self.from_node.append(node_text)
            
        self.ignore_next_fail = False

# 下面再次执行求解器，并使用TreeMonitor创建树状图。

solver = pywrapcp.Solver("test")
x = [solver.IntVar(1, 3, name) for name in "ABC"]
solver.Add(solver.AllDifferent(x))

tree_monitor = TreeMonitor(solver)

# SEND + MORE = MONEY

# 下面使用上面的方法显示SEND + MORE = MONEY数字谜题的搜索树。在等式中每个字母表示一个不同的数字，单词的首字母的不是0。找到一组字母与数字的映射，保证前面的等式成立。

solver = pywrapcp.Solver("SEND MORE MONEY")
all_variables = S, E, N, D, M, O, R, Y = [solver.IntVar(0, 9, name) for name in "SENDMORY"]
solver.Add(solver.AllDifferent(all_variables))
solver.Add(S > 0)
solver.Add(M > 0)
solver.Add(S*1000 + E*100 + N*10 + D + M*1000 + O*100 + R*10 + E == M*10000 + O*1000 + N*100 + E*10 + Y)
tree_monitor = TreeMonitor(solver)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

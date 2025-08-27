"""
puzzle

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
#广度搜索解华容道

#华容道游戏的目的是找到一个最短的移动方法，让最大的一个方块移到底部出口。这是一个计算图的最短路径的问题，可以使用广度搜索求解。该问题的困难之处是如何图中的一个节点(各个方块的位置)，以及两个节点之间的联系(各种移动方式)。

from itertools import product
from collections import defaultdict
from os import path
import pickle

W, H = 4, 5

Positions = list(product(range(H), range(W)))

Blocks = {
    "A": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "B": [(0, 0), (1, 0)],
    "C": [(0, 0), (0, 1)],
    "D": [(0, 0)],
}

BlockSizes = {key: (blocks[-1][0] + 1, blocks[-1][1] + 1) for key, blocks in Blocks.items()}


D = 1, 0
U = -1, 0
R = 0, 1
L = 0, -1

Direct = {
    "D": D,
    "U": U,
    "R": R,
    "L": L,
}

Moves = {
    "A": {"D": [(2, 0), (2, 1)],
          "U": [(-1, 0), (-1, 1)],
          "R": [(0, 2), (1, 2)],
          "L": [(0, -1), (1, -1)]},

    "B": {"D": [(2, 0)],
          "U": [(-1, 0)],
          "DD": [(2, 0), (3, 0)],
          "UU": [(-1, 0), (-2, 0)],
          "R": [(0, 1), (1, 1)],
          "L": [(0, -1), (1, -1)]},

    "C": {"D": [(1, 0), (1, 1)],
          "U": [(-1, 0), (-1, 1)],
          "R": [(0, 2)],
          "L": [(0, -1)],
          "RR": [(0, 2), (0, 3)],
          "LL": [(0, -1), (0, -2)]},

    "D": {"D": [(1, 0)],
          "DD": [(1, 0), (2, 0)],
          "U": [(-1, 0)],
          "UU": [(-1, 0), (-2, 0)],
          "R": [(0, 1)],
          "RR": [(0, 1), (0, 2)],
          "L": [(0, -1)],
          "LL": [(0, -1), (0, -2)],
          "DL": [(1, 0), (1, -1)],
          "DR": [(1, 0), (1, 1)],
          "UL": [(-1, 0), (-1, -1)],
          "UR": [(-1, 0), (-1, 1)],
          "LD": [(0, -1), (1, -1)],
          "LU": [(0, -1), (-1, -1)],
          "RD": [(0, 1), (1, 1)],
          "RU": [(0, 1), (-1, 1)]}
}

def to_rect(block_type, r, c):
        h, w =BlockSizes[block_type]
        y = r
        x = c
        y = 5 - y
        return x, y, w, h


def compress_node(node):
    cells = node[0]
    return "".join([cells[pos] if cells[pos] is not None else " " for pos in Positions])


def status_to_positions(status):
    status = list(status)
    positions = []
    spaces = []
    for r in range(H):
        for c in range(W):
            idx = r * W + c
            block_type = status[idx]
            if block_type in Blocks:
                positions.append((block_type, r, c))
                for dr, dc in Blocks[block_type]:
                    delta = dr * W + dc
                    status[idx + delta] = ""
            elif block_type == " ":
                spaces.append((r, c))
    return positions, spaces


def find_all_nodes(blocks):
    nodes = []
    positions = []
    cells = {pos: None for pos in Positions}
    last_positions = defaultdict(list)

    for block in Blocks:
        last_positions[block].append((-1, -1))

    def is_empty(name, r, c):
        return all(cells[r + r2, c + c2] is None for r2, c2 in Blocks[name])

    def set_cells(name, r, c, value):
        for r2, c2 in Blocks[name]:
            cells[r + r2, c + c2] = value

    def solve(blocks):
        if not blocks:
            nodes.append((cells.copy(), positions[:]))
            return

        block = blocks[0]
        h, w = BlockSizes[block]
        last_pos = last_positions[block][-1]

        for pos in Positions:
            r, c = pos
            if r <= H - h and c <= W - w and pos > last_pos and is_empty(block, r, c):
                set_cells(block, r, c, block)
                positions.append(pos)
                last_positions[block].append(pos)

                solve(blocks[1:])

                set_cells(block, r, c, None)
                last_positions[block].pop()
                positions.pop()

    solve(blocks)
    return nodes

def get_moves(node, blocks):
    _Moves = Moves
    block_moves = [_Moves[c] for c in blocks]
    cells, positions = node
    empty = {key for key, value in cells.items() if value is None}
    possible_pos = set()
    for r, c in empty:
        for dr, dc in Direct.values():
            possible_pos.add((r + dr, c + dc))
            possible_pos.add((r + dr * 2, c + dc * 2))

    for i in range(len(positions)):
        pos = positions[i]
        if pos not in possible_pos:
            continue
        r, c = pos
        moves = block_moves[i]
        for move, offsets in moves.items():
            if empty.issuperset([(r + r2, c + c2) for (r2, c2) in offsets]):
                yield pos, move


def get_neighbour(node, move):
    cells, positions = node
    cells = cells.copy()
    pos, direct = move
    name = cells[pos]
    r, c = pos
    from_pos = [(r + r2, c + c2) for r2, c2 in Blocks[name]]

    dr = dc = 0
    for cmd in direct:
        dr2, dc2 = Direct[cmd]
        dr += dr2
        dc += dc2

    to_pos = [(r + dr, c + dc) for r, c in from_pos]
    for key in from_pos:
        cells[key] = None
    for key in to_pos:
        cells[key] = name
    return compress_node((cells, None))


def cnode_str(cnode):
    return "\n".join(cnode[i * W:i * W + W] for i in range(H))


def dump_graph(blocks):
    nodes = find_all_nodes(blocks)
    compressed_nodes = [compress_node(node) for node in nodes]
    node_ids = {node: i for i, node in enumerate(compressed_nodes)}

    edges = []
    moves = []
    for i, node in enumerate(nodes):
        for move in get_moves(node, blocks):
            edge = i, node_ids[get_neighbour(node, move)]
            edges.append(edge)
            moves.append(move)

    fn = "%s.pickle" % blocks
    with open(fn, "wb") as f:
        pickle.dump({"nodes": compressed_nodes, "edges": edges}, f)

    print(fn, "saved")

dump_graph("ABBBBCDDDD")

# ABBBBCDDDD.pickle saved

from collections import deque


def flat_path(status):
    path = []
    while True:
        path.append(status[0])
        status = status[1]
        if status is None:
            break
    return path[::-1]


def breadth_first_search(start_node, edges, is_solved):
    todo = deque([(start_node, None)])
    checked = set([start_node])

    while todo:
        status = todo.popleft()
        node = status[0]
        if is_solved(node):
            return flat_path(status)

        for next_node in edges[node]:
            if next_node not in checked:
                todo.append((next_node, status))
                checked.add(next_node)

def load_graph(blocks):
    full_path = path.join(FOLDER, "%s.pickle" % blocks)
    if path.exists(full_path):
        with open(full_path, "rb") as f:
            return pickle.load(f)
    else:
        raise IOError("graph %s not found" % blocks)
        
        
class HrdSolver:
    def __init__(self):
        with open("ABBBBCDDDD.pickle", "rb") as f:
            data = pickle.load(f)
            self.nodes = data["nodes"]
            self.edges = data["edges"]

        node_edges = defaultdict(list)
        for n1, n2 in self.edges:
            node_edges[n1].append(n2)
            node_edges[n2].append(n1)

        self.node_edges = node_edges

    def is_solved(self, node):
        status = self.nodes[node]
        return status[13:15] == "AA" and status[17:19] == "AA"

    def solve(self, start_status):
        start_node = self.nodes.index(start_status)
        shortest_path = breadth_first_search(start_node, self.node_edges, self.is_solved)
        return [self.nodes[node] for node in shortest_path]

    def get_moves(self, start_status):
        steps = self.solve(start_status)
        last_positions, last_spaces = status_to_positions(steps[0])
        rectangles = {(r, c): i for i, (name, r, c) in enumerate(last_positions)}
        moves = []

        for step in steps[1:]:
            positions, spaces = status_to_positions(step)
            set_prev = set(last_positions)
            set_next = set(positions)

            if set_prev == set_next:
                continue

            from_pos = (set_prev - set_next).pop()[1:]
            to_pos = (set_next - set_prev).pop()[1:]

            rect = rectangles[from_pos]
            del rectangles[from_pos]
            rectangles[to_pos] = rect

            is_corner = from_pos[0] - to_pos[0] != 0 and from_pos[1] - to_pos[1] != 0
            if not is_corner:
                moves.append((rect,) + from_pos + to_pos)
            else:
                middle_positions = {(from_pos[0], to_pos[1]), (to_pos[0], from_pos[1])}
                target = (middle_positions & set(last_spaces)).pop()
                moves.append((rect,) + from_pos + target)
                moves.append((rect,) + target + to_pos)
            last_positions, last_spaces = positions, spaces

        return moves

    def get_bokeh_data(self, start_status):
        import random
        def random_color():
            return "#{:02x}{:02x}{:02x}".format(*(random.randint(100, 250) for _ in range(3)))

        moves = self.get_moves(start_status)
        positions, spaces = status_to_positions(start_status)
        blocks = [item[0] for item in positions]

        x, y, w, h = list(zip(*[to_rect(*item) for item in positions]))

        rects = dict(x=x, y=y, w=w, h=h, c=[random_color() for _ in range(len(x))])

        block_moves = []
        for block_id, r1, c1, r2, c2 in moves:
            block = blocks[block_id]
            x1, y1, _, _ = to_rect(block, r1, c1)
            x2, y2, _, _ = to_rect(block, r2, c2)
            block_moves.append([block_id, x1, y1, x2, y2])

        return rects, block_moves        

solver = HrdSolver()
start_status = 'BAABBAABBCCBBDDBD  D'
rects, moves = solver.get_bokeh_data(start_status)

# from embedjs import embed_resources
# from py2js import py2js_call
# embed_resources("raphael")

def draw_hrd_js(uid, parameter):
    rects = parameter.rects
    moves = parameter.moves

    def draw(Raphael):
        paper = Raphael(uid, 400, 500)
        blocks = []
        step = -1
        for i in range(len(rects.c)):
            rect = paper.rect(rects.x[i]*100, 500-rects.y[i]*100, rects.w[i]*100, rects.h[i]*100).attr({"fill":rects.c[i]})
            blocks.append(rect)
            
        def animate():
            nonlocal step
            step += 1
            if step >= len(moves):
                return
            bid, x1, y1, x2, y2 = moves[step]
            blocks[bid].animate({"x":x2*100, "y":500-y2*100}, 500, "linear", animate)
        
        animate()

    require(['raphael'], draw)

# py2js_call(draw_hrd_js, {"rects":rects, "moves":moves})

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#用PicoSAT解数织游戏


def paint_numbers(numbers, count):
    if sum(numbers) + len(numbers) - 1 > count:
        return
    elif len(numbers) == 1:
        for i in range(0, count - numbers[0] + 1):
            yield [-1] * i + [1] * numbers[0] + [-1] * (count - i - numbers[0])
    else:
        for res in paint_numbers(numbers[1:], count - numbers[0] - 1):
            yield [1] * numbers[0] + [-1] + res
        for res in paint_numbers(numbers, count - 1):
            yield [-1] + res
     

# 下面是12个方格填写[2, 1, 5]时的所有解:

for line in paint_numbers([2, 1, 5], 12):
    print([int(x > 0) for x in line])
     

# DNF To CNF


def dnf_to_cnf(dnf, new_vars=None):
    if new_vars is None:
        start = max(max(map(abs, term)) for term in dnf) + 1
        new_vars = iter(range(start, start + len(dnf)))
    zlist = []
    cnf = []
    for term in dnf:
        z = next(new_vars)
        zlist.append(z)
        cnf.append([z] + [-v for v in term])
        for v in term:
            cnf.append([-z, v])
    cnf.append(zlist)
    return cnf
     

dnf = [[-1, 2, 3], [1, -2, 3], [1, 2, -3]]
cnf = dnf_to_cnf(dnf)
print(cnf)
     
"""
# 然后用cycosat求解。由解答可知CNF表达式引进了3个新的变量，而三个原始变量的解满足只有一个为False的约束条件。

import cycosat
sat = cycosat.CoSAT()
sat.add_clauses(cnf)
for sol in sat.iter_solve():
    print([int(x > 0) for x in sol])
     

solution = list(paint_numbers([2, 1, 5], 12))
     

# 然后将解转换为DNF表达式：

variables = list(range(1, 13))
dnf = []
for term in solution:
    dnf.append([v * t for v, t in zip(variables, term)])
print(dnf)
     
# 将dnf转换为CNF表达式并使用CoSAT求解，将两个解排序之后比较它们是否相同。

sat = cycosat.CoSAT()
sat.add_clauses(dnf_to_cnf(dnf))
solution_cnf = [res[:12] for res in sat.iter_solve()]
cc = sorted(solution) == sorted(solution_cnf)
print(cc)

#True
"""

""" NG
#解数织游戏

#有了前面的准备之后，让我们看看如何解数织游戏。对每一组数字计算其对应的解，并通过解和该组数字对应的布尔变量产生DNF表达式，然后将DNF表达式转换为CNF表达式。将每行每列的CNF表达式连接在一起就得到了整个数织游戏的CNF表达式。

import numpy as np
from itertools import count

class Nonogram:
    def __init__(self, rows, cols, width=None, height=None):
        if width is None:
            width = len(cols)
        if height is None:
            height = len(rows)
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.var_count = self.width * self.height
        self.vars = np.arange(1, self.var_count + 1).reshape(-1, self.width)
        self.new_vars = count(self.var_count + 2)
        
        self.cnf = []
        
        for i, row in enumerate(self.rows):
            self.add_constraints(row, self.width, self.vars[i, :].tolist())
            
        for j, col in enumerate(self.cols):
            self.add_constraints(col, self.height, self.vars[:, j].tolist())
            
    def add_constraints(self, numbers, count, variables):
        dnf = []
        for pattern in paint_numbers(numbers, count):
            dnf.append([v * p for v, p in zip(variables, pattern)])
        self.cnf.extend(dnf_to_cnf(dnf, new_vars = self.new_vars))
        
    def solve(self):
        sat = cycosat.CoSAT()
        sat.add_clauses(self.cnf)
        self.solution = np.array(sat.solve()[:self.var_count]).reshape(self.height, -1)
        self.solution[self.solution == -1] = 0
        return self
    
    def to_json(self):
        return {"rows":self.rows, "cols":self.cols, "cells":self.solution.tolist()}   
     

# 下面的程序用于显示数织游戏的解。

#from py2js import draw_nonogram
#from embedjs import embed_resources
#embed_resources("raphael")
     

# 下面让用Nonogram解一个简单的谜题：

rows = [
    [3],
    [2,1],
    [2],
    [7],
    [9],
    [2, 3, 2],
    [4, 4],
    [9],
    [2, 3, 2],
    [3, 3],
    [7],
    [5]
]

cols = [
    [6],
    [8],
    [2, 2, 3],
    [8, 2],
    [6, 2, 2],
    [1, 6, 2],
    [2, 2, 2, 3],
    [8],
    [6]
]
pbn = Nonogram(rows, cols)
pbn.solve()
draw_nonogram(pbn.to_json())
     

# 在本文件的路径下有三个从www.nonograms.org 下载的谜题。下面是用本书提供的puzzle.nonogram.read_puzzle()读入谜题，并显示其解。

from puzzle import nonogram

def solve_and_paint(fn):
    rows, cols = nonogram.read_puzzle(fn)
    pbn = Nonogram(rows, cols)
    pbn.solve()
    draw_nonogram(pbn.to_json())
    
solve_and_paint("nonogram01.txt")
     

# Wall time: 45.5 ms

# 稍微复杂一点的谜题就需要很长时间求解。而本文中的算法无法解决nonogram03.txt中的60x45大小的谜题。其原因在于，当方格数和数字增加，每一行或每一列的所有解的数目急剧增加，即需要增加的变量数以及CNF表达式的项也急剧增加。像nonogram03.txt中的谜题会用光所有的内存。在下一章我们会介绍一种更聪明的方法减少每行列对应的CNF表达式的项数。

solve_and_paint("nonogram02.txt")
     

# Wall time: 23.6 s
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 用PicoSAT解数织游戏-提高解题速度

import itertools

def start_pos(numbers, count):
    s = 0
    for i, n in enumerate(numbers):
        yield s
        s += n + 1

def end_pos(numbers, count):
    width = sum(numbers) + len(numbers) - 1
    start = count - width
    for pos in start_pos(numbers, count):
        yield start + pos
        
def create_position_variables(numbers, count, new_bool_variables):
    pos_variables = []
    for i, (a, b) in enumerate(zip(start_pos(numbers, count), end_pos(numbers, count))):
        pos_variables.append({j:next(new_bool_variables) for j in range(a, b + 1)})
    return pos_variables

numbers = [1, 2, 3]
count = 10
pos_variables = create_position_variables(numbers, count, itertools.count(1))
print(pos_variables)


def only_one_true(variables):
    yield list(variables)
    for i, j in itertools.combinations(variables, 2):
        yield [-i, -j]
        
def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)        

def position_variables_constraint(pos_variables, numbers):
    cnf = []
    # 每个数字对应的所有位置变量中只能有一个为真
    for i, pos_var in enumerate(pos_variables):
        cnf.extend(only_one_true(pos_var.values()))

    # 两个连续的数字num1, num2的位置pos1, pos2必须满足pos2 >= pos1 + num1
    for i, (pos_var1, pos_var2) in enumerate(pairwise(pos_variables)):
        width = numbers[i] + 1
        for pos1, pos2 in itertools.product(pos_var1, pos_var2):
            if pos2 < pos1 + width:
                cnf.append([-pos_var1[pos1], -pos_var2[pos2]])
    return cnf

cnf = position_variables_constraint(pos_variables, numbers)
print(cnf)

import cycosat
sat = cycosat.CoSAT()
sat.add_clauses(cnf)
for sol in sat.iter_solve():
    print([int(x > 0) for x in sol])

# 使用位置变量设置方格填充变量的值


def cell_variables_constraint(pos_variables, cell_variables, numbers, count):
    cnf = []
    # cell[j] == 1 for all pos[i] <= j < pos[i] + num[i]
    for i, pos_var in enumerate(pos_variables):
        for pos, var in pos_var.items():
            for j in range(numbers[i]):
                cnf.append([-var, cell_variables[pos + j]])

    # cell[j] == 0, for all j < pos[0]
    for pos, var in pos_variables[0].items():
        for j in range(0, pos):
            cnf.append([-var, -cell_variables[j]])

    # cell[j] == 0, for all j >= pos[-1] + num[-1]
    for pos, var in pos_variables[-1].items():
        for j in range(pos + numbers[-1], count):
            cnf.append([-var, -cell_variables[j]])

    # cell[j] == 0 for all pos[i] + num[i] <= j < pos[i+1]
    for i, (pos_var1, pos_var2) in enumerate(pairwise(pos_variables)):
        for pos1, pos2 in itertools.product(pos_var1, pos_var2):
            if pos2 > pos1 + numbers[i]:
                for j in range(pos1 + numbers[i], pos2):
                    cnf.append([-pos_var1[pos1], -pos_var2[pos2], -cell_variables[j]])
    return cnf

# 下面创建10个方格填充变量和表示每个数字位置的变量，并计算出表示所有约束条件的CNF表达式。

numbers = [1, 2, 3]
count = 10
cell_variables = list(range(1, count + 1))
pos_variables = create_position_variables(numbers, count, itertools.count(count + 1))
cnf = position_variables_constraint(pos_variables, numbers)
cnf += cell_variables_constraint(pos_variables, cell_variables, numbers, count)

# 对上面的cnf表达式求解，输出方格填充变量的解。可以看到这些解包含了所有的可能性：

import cycosat
sat = cycosat.CoSAT()
sat.add_clauses(cnf)
for sol in sat.iter_solve():
    print([int(x > 0) for x in sol[:count]])

# 能解大规模数织游戏的程序

# 下面的Nonogram类使用前面的函数对数织游戏求解。

import numpy as np

class Nonogram:
    def __init__(self, rows, cols, width=None, height=None):
        if width is None:
            width = len(cols)
        if height is None:
            height = len(rows)
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.var_count = self.width * self.height
        self.vars = np.arange(1, self.var_count + 1).reshape(-1, self.width)
        self.new_vars = itertools.count(self.var_count + 1)
        
        self.cnf = []
        
        for i, row in enumerate(self.rows):
            self.add_constraints(row, self.width, self.vars[i, :].tolist())
            
        for j, col in enumerate(self.cols):
            self.add_constraints(col, self.height, self.vars[:, j].tolist())
            
    def add_constraints(self, numbers, count, cell_variables):
        pos_variables = create_position_variables(numbers, count, self.new_vars)
        self.cnf.extend(position_variables_constraint(pos_variables, numbers))
        self.cnf.extend(cell_variables_constraint(pos_variables, cell_variables, numbers, count))
        
    def solve(self):
        sat = cycosat.CoSAT()
        sat.add_clauses(self.cnf)
        self.solution = np.array(sat.solve()[:self.var_count]).reshape(self.height, -1)
        self.solution[self.solution == -1] = 0
        return self
        
    def to_json(self):
        return {"rows":self.rows, "cols":self.cols, "cells":self.solution.tolist()}   

# 下面看看Nonogram的能力，首先载入显示和文件读取相关的函数。

from py2js import draw_nonogram
from embedjs import embed_resources
from puzzle import nonogram
embed_resources("raphael")

# 然后对三个谜题求解：

def solve_and_paint(fn):
    rows, cols = nonogram.read_puzzle(fn)
    pbn = Nonogram(rows, cols)
    pbn.solve()
    draw_nonogram(pbn.to_json())

solve_and_paint("nonogram01.txt")

# Wall time: 61.5 ms

solve_and_paint("nonogram02.txt")

# Wall time: 371 ms

solve_and_paint("nonogram03.txt")

# Wall time: 6.03 s

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

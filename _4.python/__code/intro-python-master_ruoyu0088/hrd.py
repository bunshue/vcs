# -*- coding: utf-8 -*-
from os import path
from collections import defaultdict
from itertools import product
import pickle
import time
import random
from search import breadth_first_search


FOLDER = path.dirname(__file__)

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
        y = r + h * 0.5
        x = c + w * 0.5
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

    fn = path.join(FOLDER, "%s.pickle" % blocks)
    with open(fn, "wb") as f:
        pickle.dump({"nodes": compressed_nodes, "edges": edges}, f)

    print(fn, "saved")


def load_graph(blocks):
    full_path = path.join(FOLDER, "%s.pickle" % blocks)
    if path.exists(full_path):
        with open(full_path, "rb") as f:
            return pickle.load(f)
    else:
        raise IOError("graph %s not found" % blocks)


def create_graphs():
    for i in range(1, 5):
        blocks = "A" + "B" * i + "C" * (5 - i) + "D"*4
        dump_graph(blocks)


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


if __name__ == '__main__':
    import sys
    dump_graph(sys.argv[1])

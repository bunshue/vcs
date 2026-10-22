import json
import numpy as np


def solve_eq(triangle1, triangle2):
    x0, y0 = triangle1[0]
    x1, y1 = triangle1[1]
    x2, y2 = triangle1[2]

    a = np.zeros((6, 6), dtype=np.float)
    b = triangle2.reshape(-1)
    a[0, 0:3] = x0, y0, 1
    a[1, 3:6] = x0, y0, 1
    a[2, 0:3] = x1, y1, 1
    a[3, 3:6] = x1, y1, 1
    a[4, 0:3] = x2, y2, 1
    a[5, 3:6] = x2, y2, 1

    x = np.linalg.solve(a, b)
    x.shape = (2, 3)
    return x


def triangle_area(triangle):
    A, B, C = triangle
    AB = A - B
    AC = A - C
    return np.abs(np.cross(AB, AC)) / 2.0


class IFS:
    def __init__(self, data):
        self.points = np.array(data["points"])
        self.cmap = data["cmap"]

    def get_eqs(self):
        eqs = []
        for i in range(1, len(self.points) // 3):
            eqs.append(solve_eq(self.points[:3, :], self.points[i * 3:i * 3 + 3, :]))
        return np.vstack(eqs)

    def get_areas(self):
        areas = []
        for i in range(1, len(self.points) // 3):
            areas.append(triangle_area(self.points[i * 3:i * 3 + 3, :]))
        s = sum(areas)
        return [x / s for x in areas]


with open("data/ifsdesigner.json") as f:
    IFS_DATA = [IFS(data) for _, data in json.load(f)]



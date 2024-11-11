"""

python_king08-tvtk_mayavi.py



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

from tvtk.api import tvtk
from mayavi import mlab

print("------------------------------------------------------------")  # 60個


'''
"""
#TVTK與Mayavi-資料的3D可視化

from tvtk.tools import tvtk_doc
cc = tvtk_doc.main()
print(cc)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#VTK的管線(Pipeline)
#顯示圓錐

# 建立一個圓錐資料源，並且同時設定其高度，底面半徑和底面圓的解析度(用36邊形近似)
cs = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36) #❷
# 使用PolyDataMapper將資料轉為圖形資料
m = tvtk.PolyDataMapper(input_connection=cs.output_port) #❸
# 建立一個Actor
a = tvtk.Actor(mapper=m) #❹
# 建立一個Renderer，將Actor加入進去
ren = tvtk.Renderer(background=(1, 1, 1)) #❺
ren.add_actor(a)
# 建立一個RenderWindow(視窗)，將Renderer加入進去
rw = tvtk.RenderWindow(size=(300,300)) #❻
rw.add_renderer(ren)
# 建立一個RenderWindowInteractor（視窗的互動工具)
rwi = tvtk.RenderWindowInteractor(render_window=rw) #❼
# 開啟互動
rwi.initialize()
rwi.start()

print("------------------------------------------------------------")  # 60個

cs = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)
m = tvtk.PolyDataMapper(input_connection=cs.output_port)
a = tvtk.Actor(mapper=m)
ren = tvtk.Renderer(background=(1, 1, 1))
ren.add_actor(a)

cc = cs.trait_names()
print(cc)


print(cs.height)
print(cs.radius)
print(cs.resolution)

print(type(cs.output))
print(cs.output is m.input)

print(a.mapper is m)
print(a.scale) # Actor物件的scale屬性表示各個軸的縮放比例

cc = ren.actors
print(cc)

#用ivtk觀察管線

cs = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)
m = tvtk.PolyDataMapper(input_connection=cs.output_port)
a = tvtk.Actor(mapper=m)

#實體

a.edit_traits() # a是表示圓錐的Actor物件

axe = tvtk.AxesActor(total_length=(3,3,3)) # 在場景中加入座標軸

a.property.edit_traits() # a是表示圓錐的Actor物件;

print("------------------------------------------------------------")  # 60個

#資料集
#ImageData

img = tvtk.ImageData(spacing=(0.1,0.1,0.1), origin=(0.1,0.2,0.3), dimensions=(3,4,5))

for n in range(6):
    print("%.1f, %.1f, %.1f" % img.get_point(n))

cc = img.point_data
print(cc)

print(img.point_data.scalars) # 沒有資料
img.point_data.scalars = np.arange(0.0, img.number_of_points)
print(type(img.point_data.scalars))
cc = img.point_data.scalars
print(cc)

a = img.point_data.scalars.to_array()
print(a)
a[:2] = 10, 11
print(img.point_data.scalars[0], img.point_data.scalars[1])

img.point_data.scalars.number_of_tuples

img.point_data.scalars.name = 'scalars'

data = tvtk.DoubleArray() # 建立一個空的DoubleArray陣列
data.from_array(np.zeros(img.number_of_points))

data.name = "zerodata"

print(img.point_data.add_array(data))
print(repr(img.point_data.get_array(1))) # 獲得第1個陣列
print(img.point_data.get_array_name(1)) # 獲得第1個陣列的名字
print(repr(img.point_data.get_array(0))) # 獲得第0個陣列
print(img.point_data.get_array_name(0)) # 獲得第0個陣列的名字

img.point_data.remove_array("zerodata") # 移除名為"zerodata"的陣列
img.point_data.number_of_arrays

vectors = np.arange(0.0, img.number_of_points*3).reshape(-1, 3)
img.point_data.vectors = vectors
print(repr(img.point_data.vectors))
print(type(img.point_data.vectors))
print(img.point_data.vectors[0])


print(img.point_data.vectors.number_of_tuples)
print(img.point_data.vectors.number_of_components)

cell = img.get_cell(0)
print(repr(cell))

print(cell.number_of_points)
print(cell.number_of_edges)
print(cell.number_of_faces)

print(repr(cell.point_ids))
cc = cell.points.to_array()
print(cc)

cc = img.number_of_cells
print(cc)

a = tvtk.IdList()
img.get_point_cells(3, a)
print("cells of point 3:", repr(a))
img.get_cell_points(0, a)
print("points of cell 0:", repr(a)) # 和cell.point_ids的值相同

a = tvtk.IdList()
a.from_array([1,2,3])
a.append(4)
a.extend([5,6])
print(repr(a))

cc = img.cell_data
print(cc)

#RectilinearGrid

#繪制ref:fig-prev的程式。

#%hide
#%exec_python -m scpy2.tvtk.figure_rectilineargrid

x = np.array([0,3,9,15])
y = np.array([0,1,5])
z = np.array([0,2,3])
r = tvtk.RectilinearGrid()
r.x_coordinates = x #❶
r.y_coordinates = y
r.z_coordinates = z
r.dimensions = len(x), len(y), len(z) #❷

r.point_data.scalars = np.arange(0.0,r.number_of_points) #❸
r.point_data.scalars.name = 'scalars'

for i in range(6):
    print(r.get_point(i))

c = r.get_cell(1)
print("points of cell 1:", repr(c.point_ids))
print(c.points.to_array())

#StructuredGrid

#繪制ref:fig-prev的程式。

#%hide
#%exec_python -m scpy2.tvtk.figure_structuredgrid

def make_points_array(x, y, z):
    return np.c_[x.ravel(), y.ravel(), z.ravel()]
    
z, y, x = np.mgrid[:3.0, :5.0, :4.0] #❶
x *= (4-z)/3 #❷
y *= (4-z)/3 
s1 = tvtk.StructuredGrid()
s1.points = make_points_array(x, y, z) #❸
s1.dimensions = x.shape[::-1] #❹
s1.point_data.scalars = np.arange(0, s1.number_of_points)
s1.point_data.scalars.name = 'scalars'

cc = s1.get_cell(2).point_ids
print(cc)

#[2, 3, 7, 6, 22, 23, 27, 26]

c = s1.get_cell(2)
print("cell type:", type(c))
print("number_of_faces:", c.number_of_faces) #單元的面數
f = c.get_face(0) #獲得第0個面
print("face type:", type(f)) #每個面用一個Quad物件表示
print("points of face 0:", repr(f.point_ids)) #構成第0面的四個點的索引
print("edge count of cell:", c.number_of_edges) # 單元的邊數
e = c.get_edge(0) #獲得第0個邊
print("edge type:", type(e))
print("points of edge 0:", repr(e.point_ids)) #構成第0邊的兩個點的索引

r, theta, z2 = np.mgrid[2:3:3j, -np.pi/2:np.pi/2:6j, 0:4:7j]
x2 = np.cos(theta)*r
y2 = np.sin(theta)*r

s2 = tvtk.StructuredGrid(dimensions=x2.shape[::-1])
s2.points = make_points_array(x2, y2, z2)
s2.point_data.scalars = np.arange(0, s2.number_of_points)
s2.point_data.scalars.name = 'scalars'

#PolyData

source = tvtk.ConeSource(resolution = 4)
source.update() # 讓source計算其輸出資料
cone = source.output
cc = type(cone)
print(cc)

#tvtk.tvtk_classes.poly_data.PolyData

print(np.array_str(cone.points.to_array(), suppress_small=True))

print(type(cone.polys))
print(cone.polys.number_of_cells) # 圓錐有5個面
print(cone.polys.to_array())

p1 = tvtk.PolyData()
p1.points = [(1,1,0),(1,-1,0),(-1,-1,0),(-1,1,0),(0,0,2)] #❶
faces = [ 
    4,0,1,2,3,
    3,4,0,1,
    3,4,1,2,
    3,4,2,3,
    3,4,3,0
    ]
cells = tvtk.CellArray() #❷
cells.set_cells(5, faces) #❸ 
p1.polys = cells
p1.point_data.scalars = np.linspace(0.0, 1.0, len(p1.points))

#繪制ref:fig-prev的程式。

#%hide
#%exec_python -m scpy2.tvtk.figure_polydata

print(repr(p1.get_cell(0).point_ids))
print(repr(p1.get_cell(1).point_ids))

N = 10
a, b = np.mgrid[0:np.pi:N*1j, 0:np.pi:N*1j]
x = np.sin(a)*np.cos(b)
y = np.sin(a)*np.sin(b)
z = np.cos(a)

points = make_points_array(x, y, z) #❶
faces = np.zeros(((N-1)**2, 4), np.int) #❷
t1, t2 = np.mgrid[:(N-1)*N:N, :N-1]
faces[:,0] = (t1+t2).ravel()
faces[:,1] = faces[:,0] + 1
faces[:,2] = faces[:,1] + N
faces[:,3] = faces[:,0] + N

p2 = tvtk.PolyData(points = points, polys = faces)
p2.point_data.scalars = np.linspace(0.0, 1.0, len(p2.points))

cc = p2.polys.to_array()[:20]
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#TVTK的改進

#%%python

# -*- coding: utf-8 -*-
import vtk

# 建立一個圓錐資料源
cone = vtk.vtkConeSource( )
cone.SetHeight( 3.0 )
cone.SetRadius( 1.0 )
cone.SetResolution(10)
# 使用PolyDataMapper將資料轉為圖形資料
coneMapper = vtk.vtkPolyDataMapper( )
coneMapper.SetInputConnection( cone.GetOutputPort( ) )
# 建立一個Actor
coneActor = vtk.vtkActor( )
coneActor.SetMapper ( coneMapper )
# 用線框模式顯示圓錐
coneActor.GetProperty( ).SetRepresentationToWireframe( )
# 建立Renderer和視窗
ren1 = vtk.vtkRenderer( )
ren1.AddActor( coneActor )
ren1.SetBackground( 0.1 , 0.2 , 0.4 )
renWin = vtk.vtkRenderWindow( )
renWin.AddRenderer( ren1 )
renWin.SetSize(300 , 300)
# 建立互動工具
iren = vtk.vtkRenderWindowInteractor( )
iren.SetRenderWindow( renWin )
iren.Initialize( )
iren.Start( )


#TVTK的基本用法

cs = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)
m = tvtk.PolyDataMapper(input_connection = cs.output_port)
a = tvtk.Actor(mapper=m)
ren = tvtk.Renderer(background=(1, 1, 1))
ren.add_actor(a)
rw = tvtk.RenderWindow(size=(300,300))
rw.add_renderer(ren)
rwi = tvtk.RenderWindowInteractor(render_window=rw) 
rwi.initialize()
rwi.start()

#Trait屬性

p = tvtk.Property()
p.set(opacity=0.5, color=(1,0,0), representation="w")

p.edit_traits()

print(p.representation)
p_vtk = tvtk.to_vtk(p)
p_vtk.SetRepresentationToSurface()
print(p.representation)

#序列化

import pickle
p = tvtk.Property()
p.representation = "w"
s = pickle.dumps(p)
del p
q = pickle.loads(s)
q.representation

#'wireframe'

p = tvtk.Property()
p.interpolation = "flat"
d = p.__getstate__()
del p
q = tvtk.Property()
print(q.interpolation)
q.__setstate__(d)
print(q.interpolation)

#gouraud
#flat

#集合迭代

ac = tvtk.ActorCollection()
print(len(ac))
ac.append(tvtk.Actor())
ac.append(tvtk.Actor())
print(len(ac))

for a in ac:
    print(repr(a))

del ac[0]
print(len(ac))

import vtk
ac = vtk.vtkActorCollection()
print(ac.GetNumberOfItems())
ac.AddItem(vtk.vtkActor())
ac.AddItem(vtk.vtkActor())
print(ac.GetNumberOfItems())

ac.InitTraversal()
for i in range(ac.GetNumberOfItems()):
    print(repr(ac.GetNextItem()))
    
ac.RemoveItem(0)
print(ac.GetNumberOfItems())

#陣列動作

pts = tvtk.Points()
p_array = np.eye(3)
pts.from_array(p_array)
pts.print_traits()
pts.to_array()

points = np.array([[0,0,0],[1,0,0],[0,1,0],[0,0,1]], 'f')
triangles = np.array([[0,1,3],[0,3,2],[1,2,3],[0,2,1]])
values = np.array([1.1, 1.2, 2.1, 2.2])
mesh = tvtk.PolyData(points=points, polys=triangles)
mesh.point_data.scalars = values
print(repr(mesh.points))
print(repr(mesh.polys))
print(mesh.polys.to_array())
print(mesh.point_data.scalars.to_array())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pylab as pl

#TVTK可視化案例
#scpy2.tvtk.example_cut_plane：切面示範程式


def read_data():
    # 讀入資料
    plot3d = tvtk.MultiBlockPLOT3DReader( #❶
        xyz_file_name = "data/combxyz.bin",
        q_file_name = "data/combq.bin",
        scalar_function_number = 100, vector_function_number = 200
    )
    plot3d.update() #❷
    return plot3d

plot3d = read_data()
grid = plot3d.output.get_block(0) #❸

# 建立彩色映射表
lut = tvtk.LookupTable() #❹
lut.table = pl.cm.cool(np.arange(0,256))*255

print(type(plot3d.output))
print(type(plot3d.output.get_block(0)))

print("dimensions:", grid.dimensions)
print(grid.points.to_array())
print("cell arrays:", grid.cell_data.number_of_arrays)
print("point arrays:", grid.point_data.number_of_arrays)

print("arrays name:")
for i in range(grid.point_data.number_of_arrays):
    print("    ", grid.point_data.get_array_name(i))

print("scalars name:", grid.point_data.scalars.name)
print("vectors name:", grid.point_data.vectors.name)

# 顯示StructuredGrid中的一個網格面
plane = tvtk.StructuredGridGeometryFilter(extent = (0, 100, 0, 100, 6, 6)) #❶
plane.set_input_data(grid) #❷
plane_mapper = tvtk.PolyDataMapper(lookup_table = lut, input_connection = plane.output_port) #❸
plane_mapper.scalar_range = grid.scalar_range #❹
plane_actor = tvtk.Actor(mapper = plane_mapper) #❺

#TVTK庫沒有將SetInputData()轉換成input_data屬性，因此需要呼叫其對應的set_input_data()函數設定輸入資料集。

plane.update()
p = plane.output
type(p)

print(p.number_of_points, grid.dimensions[0] * grid.dimensions[1])

print(grid.dimensions)
points1 = grid.points.to_array().reshape((25,33,57,3))
points2 = p.points.to_array().reshape((33,57,3))
np.all(points1[6] == points2)

print(p.point_data.number_of_arrays)
print(p.point_data.scalars.name)

lut2 = tvtk.LookupTable()
lut2.table = pl.cm.cool(np.arange(0,256))*255
cut_plane = tvtk.Plane(origin = grid.center, normal=(-0.287, 0, 0.9579)) #❶
cut = tvtk.Cutter(cut_function = cut_plane) #❷
cut.set_input_data(grid)
cut_mapper = tvtk.PolyDataMapper(input_connection = cut.output_port, lookup_table = lut2)
cut_actor = tvtk.Actor(mapper = cut_mapper)

type(plane.output)

cut.update()
cut.output.number_of_points

cut.output.point_data.number_of_arrays

def make_outline(input_obj):
    from tvtk.common import configure_input
    outline = tvtk.StructuredGridOutlineFilter()
    configure_input(outline, input_obj)
    outline_mapper = tvtk.PolyDataMapper(input_connection = outline.output_port)
    outline_actor = tvtk.Actor(mapper = outline_mapper)
    outline_actor.property.color = 0.3, 0.3, 0.3
    return outline_actor

outline_actor = make_outline(grid)

#相等面
#使用相等面可視化純量場

contours = tvtk.ContourFilter()
contours.set_input_data(grid)
contours.generate_values(8, grid.point_data.scalars.range) #❶
mapper = tvtk.PolyDataMapper(input_connection = contours.output_port,
    scalar_range = grid.point_data.scalars.range) #❷
actor = tvtk.Actor(mapper = mapper)
actor.property.opacity = 0.3 #❸

outline_actor = make_outline(grid)

print(contours.get_value(0))

contours.set_value(0, 0.21)

#0.197813093662

plot3d = read_data()
plot3d.add_function(153) #❶
plot3d.update()
grid = plot3d.output.get_block(0)

contours = tvtk.ContourFilter()
contours.set_input_data(grid)
contours.set_value(0, 0.30) #❷
mapper = tvtk.PolyDataMapper(input_connection = contours.output_port,
    scalar_range = grid.point_data.get_array(4).range, #❸
    scalar_mode = "use_point_field_data") #❹
mapper.color_by_array_component("VelocityMagnitude", 0) #❺
actor = tvtk.Actor(mapper = mapper)
actor.property.opacity = 0.6 

outline_actor = make_outline(grid)


cc = grid.point_data.get_array_name(4)
print(cc)


#流線

#使用流線和箭頭可視化向量場

# 向量箭頭
mask = tvtk.MaskPoints(random_mode=True, on_ratio=50) #❶
mask.set_input_data(grid)

arrow_source = tvtk.ArrowSource() #❷
arrows = tvtk.Glyph3D(input_connection = mask.output_port, #❸
    scale_factor=2/np.max(grid.point_data.scalars.to_array()))
arrows.set_source_connection(arrow_source.output_port)
arrows_mapper = tvtk.PolyDataMapper(input_connection = arrows.output_port, 
    scalar_range = grid.point_data.scalars.range)
arrows_actor = tvtk.Actor(mapper = arrows_mapper)

print(grid.number_of_points)
mask.update()
print(type(mask.output))
print(mask.output.number_of_points)
print(mask.output.point_data.number_of_arrays )

# 由於TVTK沒有提供source_connection屬性，
# 因此只能透過set_source_connection()設定Glyph3D物件的輸入。

arrows.update()
print(arrow_source.output.number_of_points) # 一個箭頭有31個點
print(arrows.output.number_of_points) # 箭頭被複製了N份，因此有N*31個點

center = grid.center
sphere = tvtk.SphereSource(  #❶
    center=(2, center[1], center[2]), radius=2, 
    phi_resolution=6, theta_resolution=6)
sphere_mapper = tvtk.PolyDataMapper(input_connection=sphere.output_port)
sphere_actor = tvtk.Actor(mapper=sphere_mapper)
sphere_actor.property.set(
    representation = "wireframe", color=(0,0,0))


point_data = grid.point_data
point_data.scalars = np.sqrt(np.sum(point_data.vectors.to_array()**2, axis=-1))

# grid是資料集物件，而vnorm為Algorithm物件。
# 為了讓程式相容這兩種不同的輸入型態，可以使用tvtk.common.configure_input()。

vnorm = tvtk.VectorNorm()
vnorm.set_input_data(grid)

# 計算圓柱的相貫線

# scpy2.tvtk.example_tube_intersection：計算兩個圓管的相貫線，
# 可透過界面中的滑動區塊控制項修改圓管的內徑和外徑。

#%figonly=產生圓管的管線
graph = u"""
digraph structs {
rankdir="LR";        
node [shape=record,style=filled];
edge [fontsize=10, penwidth=2.0];
CylinderSource[label="CylinderSource\n(outer)"];
CylinderSource -> TriangleFilter;
TriangleFilter -> TransformFilter;
Transform -> TransformFilter [label="transform", penwidth=1.0];
TransformFilter -> BooleanOperationPolyDataFilter;
BooleanOperationPolyDataFilter[label="BooleanOperationPolyDataFilter\n(difference)"];

CylinderSource2[label="CylinderSource\n(inner)"];
TriangleFilter2[label=TriangleFilter];
TransformFilter2[label=TransformFilter];
Transform2[label=Transform];
CylinderSource2 -> TriangleFilter2;
TriangleFilter2 -> TransformFilter2;
Transform2 -> TransformFilter2 [label="transform", penwidth=1.0];
TransformFilter2 -> BooleanOperationPolyDataFilter;

//BooleanOperationPolyDataFilter -> Tube;
}
"""


def make_tube(height, radius, resolution, rx=0, ry=0, rz=0):
    cs1 = tvtk.CylinderSource(height=height, radius=radius[0], resolution=resolution) #❶
    cs2 = tvtk.CylinderSource(height=height+0.1, radius=radius[1], resolution=resolution)    
    triangle1 = tvtk.TriangleFilter(input_connection=cs1.output_port) #❷
    triangle2 = tvtk.TriangleFilter(input_connection=cs2.output_port)
    tr = tvtk.Transform()
    tr.rotate_x(rx)
    tr.rotate_y(ry)
    tr.rotate_z(rz)
    tf1 = tvtk.TransformFilter(transform=tr, input_connection=triangle1.output_port)   #❸
    tf2 = tvtk.TransformFilter(transform=tr, input_connection=triangle2.output_port)   
    bf = tvtk.BooleanOperationPolyDataFilter() #❹
    bf.operation = "difference"
    bf.set_input_connection(0, tf1.output_port)
    bf.set_input_connection(1, tf2.output_port)
    m = tvtk.PolyDataMapper(input_connection=bf.output_port, scalar_visibility=False)
    a = tvtk.Actor(mapper=m)
    a.property.color = 0.7, 0.7, 0.7
    return bf, a, tf1, tf2

tube1, tube1_actor, tube1_outer, tube1_inner = make_tube(5, [1, 0.8], 32)
tube2, tube2_actor, tube2_outer, tube2_inner = make_tube(5, [0.7, 0.55], 32, rx=90)

#%figonly=計算相貫線的管線
graph = """
digraph structs {
rankdir="LR";        
node [shape=record,style=filled];
edge [fontsize=10, penwidth=2.0];
tube1 -> BooleanOperationPolyDataFilter;
tube2_inner -> BooleanOperationPolyDataFilter;

tube2 -> BooleanOperationPolyDataFilter2;
tube1_inner -> BooleanOperationPolyDataFilter2;

BooleanOperationPolyDataFilter[label="BooleanOperationPolyDataFilter\n(difference)"];
BooleanOperationPolyDataFilter2[label="BooleanOperationPolyDataFilter\n(difference)"];

tube1 -> IntersectionPolyDataFilter;
tube2 -> IntersectionPolyDataFilter;

BooleanOperationPolyDataFilter -> PolyDataMapper1;
IntersectionPolyDataFilter -> PolyDataMapper2;
BooleanOperationPolyDataFilter2 -> PolyDataMapper3;

PolyDataMapper1[label=PolyDataMapper];
PolyDataMapper2[label=PolyDataMapper];
PolyDataMapper3[label=PolyDataMapper];

PolyDataMapper1 -> Actor1;
PolyDataMapper2 -> Actor2;
PolyDataMapper3 -> Actor3;

Actor1[label=Actor];
Actor2[label=Actor];
Actor3[label=Actor];

Actor1 -> Scene;
Actor2 -> Scene;
Actor3 -> Scene;
}
"""

def difference(pd1, pd2):
    bf = tvtk.BooleanOperationPolyDataFilter()
    bf.operation = "difference"
    bf.set_input_connection(0, pd1.output_port)
    bf.set_input_connection(1, pd2.output_port)
    m = tvtk.PolyDataMapper(input_connection=bf.output_port, scalar_visibility=False)
    a = tvtk.Actor(mapper=m)
    return bf, a

def intersection(pd1, pd2, color=(1.0, 0, 0), width=2.0):
    ipd = tvtk.IntersectionPolyDataFilter()
    ipd.set_input_connection(0, pd1.output_port)
    ipd.set_input_connection(1, pd2.output_port)
    m = tvtk.PolyDataMapper(input_connection=ipd.output_port)
    a = tvtk.Actor(mapper=m)
    a.property.diffuse_color = 1.0, 0, 0 #❶
    a.property.line_width = 2.0    
    return ipd, a

tube1_hole, tube1_hole_actor = difference(tube1, tube2_inner)
tube2_hole, tube2_hole_actor = difference(tube2, tube1_inner)
intersecting_line, intersecting_line_actor = intersection(tube1, tube2)

tube1_hole_actor.property.opacity = 0.8
tube2_hole_actor.property.opacity = 0.8
tube1_hole_actor.property.color = 0.5, 0.5, 0.5
tube2_hole_actor.property.color = 0.5, 0.5, 0.5


from scipy.spatial import distance

cpd = tvtk.CleanPolyData(tolerance_is_absolute=True, 
                         absolute_tolerance=1e-5,
                         input_connection=intersecting_line.output_port)
cpd.update()
cc = cpd.output.points.number_of_points
print(cc)


#%fig=用matplotlib繪制分析出的相貫線
from collections import defaultdict

def connect_lines(lines):
    edges = defaultdict(set)    
    for _, s, e in lines.to_array().reshape(-1, 3).tolist():
        edges[s].add(e)
        edges[e].add(s)

    while True:
        if not edges:
            break
        poly = [edges.iterkeys().next()]
        while True:
            e = poly[-1]
            neighbours = edges[e]
            if not neighbours:
                break
            n = neighbours.pop()
            try:
                edges[n].remove(e)
            except:
                pass
            poly.append(n)
        yield poly
        edges = {k:v for k,v in edges.iteritems() if v}
        
from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure(figsize=(5, 5))
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection="3d")

points = cpd.output.points.to_array()

ax.auto_scale_xyz([-1, 1], [-1, 1], [-1, 1])

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#用mlab快速繪圖

#點和線

from scipy.integrate import odeint 

def lorenz(w, t, p, r, b): 
    x, y, z = w
    return np.array([p*(y-x), x*(r-z)-y, x*y-b*z]) 

t = np.arange(0, 30, 0.01) 
track1 = odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0)) #❶

X, Y, Z = track1.T
mlab.plot3d(X, Y, Z, t, tube_radius=0.2) #❷
mlab.show()

print("------------------------------------------------------------")	#60個
""" NG
#Mayavi的管線

s = mlab.gcf() # 首先獲得目前的場景
print(s)
print(s.scene.background)

source = s.children[0] # 獲得場景的第一個子節點，也就是LineSource
print(repr(source))
print(source.name) # 節點的名字，也就管線中顯示的文字
print(repr(source.data.points)) # LineSource中的座標點
print(repr(source.data.point_data.scalars)) #每個點所對應的純量陣列

stripper = source.children[0]
print(stripper.filter.maximum_length)
print(stripper.outputs[0].number_of_points)
print(repr(stripper.outputs[0]))
print(stripper.outputs[0].number_of_lines)

tube = stripper.children[0] # 獲得Tube物件
print(repr(tube.outputs[0])) # tube的輸出是一個PolyData物件，它是一個3D圓管

manager = tube.children[0]
manager.scalar_lut_manager.lut_mode = 'Blues'
manager.scalar_lut_manager.show_legend = True

surface = manager.children[0]
surface.actor.property.representation = 'wireframe'    
surface.actor.property.opacity = 0.6    

cc = surface.actor.property.line_width
print(cc)

"""
print("------------------------------------------------------------")	#60個

#二維圖形的可視化

x, y = np.ogrid[-2:2:20j, -2:2:20j] #❶
z = x * np.exp( - x**2 - y**2) #❷

face = mlab.surf(x, y, z, warp_scale=2) #❸
axes = mlab.axes(xlabel='x', ylabel='y', zlabel='z', color=(0, 0, 0)) #❹
outline = mlab.outline(face, color=(0, 0, 0))
#%hide
fig = mlab.gcf()
fig.scene.background = 1, 1, 1
axis_color = 0.4, 0.4, 0.4
outline.actor.property.color = axis_color
axes.actors[0].property.color = axis_color
axes.title_text_property.color = axis_color
axes.label_text_property.color = axis_color
mlab.show()

print("------------------------------------------------------------")	#60個
""" NG
data = mlab.gcf().children[0]
img = data.outputs[0]
img

print(img.origin) # X,Y,Z軸的起點
print(img.spacing) # X,Y,Z軸上的點的間隔
print(img.dimensions) # X,Y,Z軸上的點的個數
print(repr(img.point_data.scalars)) # 每個點所對應的純量值

data.children[0].outputs[0]
"""
print("------------------------------------------------------------")	#60個

x, y = np.ogrid[-10:10:100j, -1:1:100j]
z = np.sin(5*((x/10)**2+y**2))

mlab.surf(x, y, z)
mlab.axes();

mlab.surf(x, y, z, extent=(-1,1,-1,1,-0.5,0.5))
mlab.axes(nb_labels=5);

mlab.surf(x, y, z, extent=(-1,1,-1,1,-0.5,0.5))
mlab.axes(ranges=(x.min(),x.max(),y.min(),y.max(),z.min(),z.max()), nb_labels=5);

x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x**2 - y**2)

mlab.imshow(x, y, z)
mlab.show()

mlab.contour_surf(x,y,z,warp_scale=2,contours=20);

face.enable_contours = True
face.contour.number_of_contours = 20

print("------------------------------------------------------------")	#60個

#網格面mesh

from numpy import sin, cos

dphi, dtheta = np.pi/80.0, np.pi/80.0
phi, theta = np.mgrid[0:np.pi+dphi*1.5:dphi, 0:2*np.pi+dtheta*1.5:dtheta]
m0, m1, m2, m3, m4, m5, m6, m7 = 4,3,2,3,6,2,6,4
r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7 #❶
x = r*sin(phi)*cos(theta) #❷
y = r*cos(phi)
z = r*sin(phi)*sin(theta)
s = mlab.mesh(x, y, z) #❸

mlab.show()

x = [[-1,1,1,-1,-1],
     [-1,1,1,-1,-1]]

y = [[-1,-1,-1,-1,-1],
     [ 1, 1, 1, 1, 1]]

z = [[1,1,-1,-1,1],
     [1,1,-1,-1,1]]

box = mlab.mesh(x, y, z, representation="surface")
mlab.axes(xlabel='x', ylabel='y', zlabel='z')
mlab.outline(box)
mlab.show()

rho, theta = np.mgrid[0:1:40j, 0:2*np.pi:40j] #❶

z = rho*rho #❷

x = rho*np.cos(theta) #❸
y = rho*np.sin(theta) 

s = mlab.mesh(x,y,z)
mlab.show()

x, y = np.mgrid[-2:2:20j, -2:2:20j] #❶
z = x * np.exp( - x**2 - y**2)
z *= 2
c = 2*x + y #❷

pl = mlab.mesh(x, y, z, scalars=c) #❸
mlab.axes(xlabel='x', ylabel='y', zlabel='z')
mlab.outline(pl)
mlab.show()

#修改和建立管線

x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x**2 - y**2)

face = mlab.surf(x, y, z, warp_scale=2)
mlab.axes(xlabel='x', ylabel='y', zlabel='z')
mlab.outline(face);

source = mlab.gcf().children[0]
print(source)
img = source.image_data
print(repr(img))

print("------------------------------------------------------------")	#60個

c = 2*x + y # 表示彩色的純量陣列
array_id = img.point_data.add_array(c.T.ravel())
img.point_data.get_array(array_id).name = "color"

source.update()
source.pipeline_changed = True

print(z[:3,:3]) # 原始的二維陣列中元素
# ImageData中的純量值的順序
print(img.point_data.scalars.to_array()[:3]) # 和陣列z的第0列的數值相同

print("------------------------------------------------------------")	#60個

normals = mlab.gcf().children[0].children[0].children[0]

# NG normals.outputs[0].point_data.scalars.to_array()[:3]

surf = normals.children[0]
del normals.children[0]

active_attr = mlab.pipeline.set_active_attribute(normals, point_scalars="color")

active_attr.children.append(surf)    

# NG normals.children[0].outputs[0].point_data.scalars.to_array()[:3]

src = mlab.pipeline.array2d_source(x, y, z) #建立ArraySource資料源
#加入color陣列
image = src.image_data
array_id = image.point_data.add_array(c.T.ravel())
image.point_data.get_array(array_id).name = "color"
src.update() #更新資料源的輸出

# 建立管線上後續物件
warp = mlab.pipeline.warp_scalar(src, warp_scale=2.0)
normals = mlab.pipeline.poly_data_normals(warp)
active_attr = mlab.pipeline.set_active_attribute(normals,
    point_scalars="color")
surf = mlab.pipeline.surface(active_attr)
mlab.axes()
mlab.outline()
mlab.show()

print("------------------------------------------------------------")	#60個

#純量場

#使用相等面、體素呈像和切面可視化純量場

x, y, z = np.ogrid[-2:2:40j, -2:2:40j, -2:0:40j]
s = 2/np.sqrt((x-1)**2 + y**2 + z**2) + 1/np.sqrt((x+1)**2 + y**2 + z**2)

surface = mlab.contour3d(s)

surface.contour.maximum_contour = 15 # 相等面的上限值為15
surface.contour.number_of_contours = 10 # 在最小值到15之間繪制10個相等面
surface.actor.property.opacity = 0.4 # 透明度為0.4

field = mlab.pipeline.scalar_field(s)
mlab.pipeline.volume(field);

mlab.pipeline.volume(field, vmin=1.5, vmax=10);

cut = mlab.pipeline.scalar_cut_plane(field.children[0], plane_orientation="y_axes")

cut.enable_contours = True # 開啟等高線顯示
cut.contour.number_of_contours = 40 # 等高線的數目為40

#向量場

#scpy2.tvtk.mlab_vector_field：使用向量箭頭、切片、等梯度面和流線顯示向量場

#%hide
#%exec_python -m scpy2.tvtk.mlab_vector_field

p, r, b = (10.0, 28.0, 3.0)
x, y, z = np.mgrid[-17:20:20j, -21:28:20j, 0:48:20j]
u, v, w = p*(y-x), x*(r-z)-y, x*y-b*z

vectors = mlab.quiver3d(x, y, z, u, v, w)

vectors.glyph.mask_input_points = True  # 開啟使用部分資料的選項
vectors.glyph.mask_points.on_ratio = 20 # 隨機選取原始資料中的1/20個點進行描繪
vectors.glyph.glyph.scale_factor = 5.0 # 設定箭頭的縮放比例

src = mlab.pipeline.vector_field(x, y, z, u, v, w)
cut_plane = mlab.pipeline.vector_cut_plane(src, scale_factor=3)
cut_plane.glyph.mask_points.maximum_number_of_points = 10000
cut_plane.glyph.mask_points.on_ratio = 2
cut_plane.glyph.mask_input_points = True

magnitude = mlab.pipeline.extract_vector_norm(src)

surface = mlab.pipeline.iso_surface(magnitude)
surface.actor.property.opacity = 0.3

#print(repr(magnitude.outputs[0].point_data.scalars))
#print(repr(magnitude.outputs[0].point_data.vectors))

mlab.flow(x, y, z, u, v, w);
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#將TVTK和Mayavi內嵌到界面中
#TVTK場景的內嵌

#示範如何將TVTK的場景內嵌進TraitsUI界面，可透過界面中的控制項調節圓管的內徑和外徑。

#%hide
#%exec_python -m scpy2.tvtk.example_tube

#%%include python tvtk/example_tube.py 1

from traits.api import HasTraits, Instance, Range, on_trait_change
from traitsui.api import View, Item, VGroup, HGroup, Controller
from tvtk.pyface.scene_editor import SceneEditor
from tvtk.pyface.scene import Scene
from tvtk.pyface.scene_model import SceneModel


class TVTKSceneController(Controller):
    def position(self, info):
        super(TVTKSceneController, self).position(info)
        self.model.plot() #❸


class TubeDemoApp(HasTraits):
    radius1 = Range(0, 1.0, 0.8)
    radius2 = Range(0, 1.0, 0.4)
    scene = Instance(SceneModel, ()) #❶
    view = View(
                VGroup(
                    Item(name="scene", editor=SceneEditor(scene_class=Scene)), #❷
                    HGroup("radius1", "radius2"),
                    show_labels=False),
                resizable=True, height=500, width=500)
        
    def plot(self):
        r1, r2 = min(self.radius1, self.radius2), max(self.radius1, self.radius2)
        self.cs1 = cs1 = tvtk.CylinderSource(height=1, radius=r2, resolution=32)
        self.cs2 = cs2 = tvtk.CylinderSource(height=1.1, radius=r1, resolution=32)
        triangle1 = tvtk.TriangleFilter(input_connection=cs1.output_port)
        triangle2 = tvtk.TriangleFilter(input_connection=cs2.output_port)
        bf = tvtk.BooleanOperationPolyDataFilter()
        bf.operation = "difference"
        bf.set_input_connection(0, triangle1.output_port)
        bf.set_input_connection(1, triangle2.output_port)
        m = tvtk.PolyDataMapper(input_connection=bf.output_port, scalar_visibility=False)
        a = tvtk.Actor(mapper=m)
        a.property.color = 0.5, 0.5, 0.5
        self.scene.add_actors([a])
        self.scene.background = 1, 1, 1
        self.scene.reset_zoom()
    
    @on_trait_change("radius1, radius2") #❹
    def update_radius(self):
        self.cs1.radius = max(self.radius1, self.radius2)
        self.cs2.radius = min(self.radius1, self.radius2)
        self.scene.render_window.render()        


if __name__ == "__main__":
    app = TubeDemoApp()
    app.configure_traits(handler=TVTKSceneController(app))

print("------------------------------------------------------------")  # 60個

#Mayavi場景的內嵌

#純量場觀察器，示範如何將Mayavi的場景內嵌到TraitsUI的界面中

from traits.api import HasTraits, Float, Int, Bool, Range, Str, Button, Instance
from traitsui.api import View, HSplit, Item, VGroup, EnumEditor, RangeEditor
from tvtk.pyface.scene_editor import SceneEditor 
from mayavi.tools.mlab_scene_model import MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene

class FieldViewer(HasTraits):
    
    # 三個軸的取值範圍
    x0, x1 = Float(-5), Float(5)
    y0, y1 = Float(-5), Float(5)
    z0, z1 = Float(-5), Float(5)
    points = Int(50) # 分割點數
    autocontour = Bool(True) # 是否自動計算相等面
    v0, v1 = Float(0.0), Float(1.0) # 相等面的取值範圍
    contour = Range("v0", "v1", 0.5) # 相等面的值
    function = Str("x*x*0.5 + y*y + z*z*2.0") # 純量場函數
    function_list = [
        "x*x*0.5 + y*y + z*z*2.0",
        "x*y*0.5 + np.sin(2*x)*y +y*z*2.0",
        "x*y*z",
        "np.sin((x*x+y*y)/z)"
    ]
    plotbutton = Button(u"描畫")
    scene = Instance(MlabSceneModel, ()) #❶
    
    """ NG
    view = View(
        HSplit(
            VGroup(
                "x0","x1","y0","y1","z0","z1",
                Item('points', label=u"點數"),
                Item('autocontour', label=u"自動相等"),
                Item('plotbutton', show_label=False),
            ),
            VGroup(
                Item('scene', 
                    editor=SceneEditor(scene_class=MayaviScene), #❷
                    resizable=True,
                    height=300,
                    width=350
                ), 
                Item('function', 
                    editor=EnumEditor(name='function_list', evaluate=lambda x:x)),
                Item('contour', 
                    editor=RangeEditor(format="%1.2f",
                        low_name="v0", high_name="v1")
                ), show_labels=False
            )
        ),
        width = 500, resizable=True, title=u"3D純量場觀察器"
    )
    """
      
    def _plotbutton_fired(self):
        self.plot()

    def plot(self):
        # 產生3D網格
        x, y, z = np.mgrid[ #❸
            self.x0:self.x1:1j*self.points, 
            self.y0:self.y1:1j*self.points, 
            self.z0:self.z1:1j*self.points]
            
        # 根據函數計算純量場的值
        scalars = eval(self.function)  #❹
        self.scene.mlab.clf() # 清理目前場景
        
        # 繪制相等平面
        g = self.scene.mlab.contour3d(x, y, z, scalars, contours=8, transparent=True) #❺
        g.contour.auto_contours = self.autocontour
        self.scene.mlab.axes(figure=self.scene.mayavi_scene) # 加入座標軸

        # 加入一個X-Y的切面
        s = self.scene.mlab.pipeline.scalar_cut_plane(g)
        cutpoint = (self.x0+self.x1)/2, (self.y0+self.y1)/2, (self.z0+self.z1)/2
        s.implicit_plane.normal = (0,0,1) # x cut
        s.implicit_plane.origin = cutpoint
        
        self.g = g #❻
        self.scalars = scalars
        # 計算純量場的值的範圍
        self.v0 = np.min(scalars)
        self.v1 = np.max(scalars)
        
    def _contour_changed(self): #❼
        if hasattr(self, "g"):
            if not self.g.contour.auto_contours:
                self.g.contour.contours = [self.contour]
                
    def _autocontour_changed(self): #❽
        if hasattr(self, "g"):
            self.g.contour.auto_contours = self.autocontour
            if not self.autocontour:
                self._contour_changed()


if __name__ == '__main__':
    app = FieldViewer()
    app.configure_traits()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""

print xxxx
print(

b'\n\n\n

plt.show()

print("------------------------------------------------------------")  # 60個

<matplotlib.ticker.NullLocator object at 0x08364F50>

<a list of 2 mcoll.LineCollection objects>


with open(filename, "r", encoding='UTF-8-sig') as f:



"""

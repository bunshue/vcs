"""
# 只會顯示最後一張圖

Bokeh 可视化（八）主题图形

image_rgba 用一组RGBA格式的数组渲染图像
image 通过 numpy 对标量数组进行颜色渲染
image_origin_anchor 对图像进行水平和垂直方向的移动和翻转
contour_simple 等高线的颜色填充
contour 在相邻轮廓的线层之间填充多边形
contour_polar 极坐标下的等高线图
hexbin 将数据分箱到六边形网格，并实现每个网格的悬停交互
ridgeplot 用山脊图来刻画可能性
scatter_jitter 基于github提交历史的分类散点图
les_mis 数据可视化的经典之《悲惨世界》
heatmap_unemployment 基于失业数据的分类热力图
periodic 元素周期表
treemap
crosstab 相邻条形图
texas_hover_map 基于失业数据的地图用法展示
tile_source 瓦片数据的使用
tile_xyzservices 选择不同地图数据供应方
tile_demo 不同图源和图层的对比
from_networkx
node_and_edge_attributes 鼠标悬停查看节点、关系、属性 的graph
candlestick 股价变动的烛形图
pie 饼图
donut 甜甜圈
burtin 抗生素的效用历史
histogram 高斯分布直方图
kde2d 双变量核密度估计
splom 用散点图矩阵 (SPLOM)进行三个变量的相关性分析
boxplot 箱线图
"""

import sys
import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.plotting import show

print("------------------------------------------------------------")  # 60個

print("image_rgba 用一组RGBA格式的数组渲染图像")

N = 20
img = np.empty((N, N), dtype=np.uint32)
view = img.view(dtype=np.uint8).reshape((N, N, 4))
for i in range(N):
    for j in range(N):
        view[i, j, 0] = int(i / N * 255)
        view[i, j, 1] = 158
        view[i, j, 2] = int(j / N * 255)
        view[i, j, 3] = 255

p = figure(width=400, height=400)
p.x_range.range_padding = p.y_range.range_padding = 0

# must give a vector of images
p.image_rgba(image=[img], x=0, y=0, dw=10, dh=10)

show(p)

print("------------------------------------------------------------")  # 60個

print("image 通过 numpy 对标量数组进行颜色渲染")

x = np.linspace(0, 10, 300)
y = np.linspace(0, 10, 300)
xx, yy = np.meshgrid(x, y)
d = np.sin(xx) * np.cos(yy)

p = figure(width=400, height=400)
p.x_range.range_padding = p.y_range.range_padding = 0

# must give a vector of image data for image parameter
p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="Sunset11", level="image")
p.grid.grid_line_width = 0.5

show(p)

print("------------------------------------------------------------")  # 60個

print("image_origin_anchor 对图像进行水平和垂直方向的移动和翻转")

from bokeh.core.enums import Anchor, ImageOrigin
from bokeh.models import ColumnDataSource, Select
from bokeh.palettes import Sunset4
from bokeh.plotting import column

Sunset4_RGBA = [[0xFF9A4B36, 0xFFE5D2A5], [0xFF72C0FD, 0xFF2600A5]]
img = np.array(Sunset4_RGBA, dtype=np.uint32)

p = figure(
    title="Different anchors and origins for image placed at coordinates (0, 0)",
    tools="",
    toolbar_location=None,
    x_range=(-10, 10),
    y_range=(-10, 10),
    background_fill_color="#efefef",
)
r = p.image_rgba(image=[img], x=0, y=0, dw=8.5, dh=8.5)
p.circle(0, 0, size=12, fill_color="black", line_color="white", line_width=3)

# a legend to identify the image pixel i, j coordinates
source = ColumnDataSource(
    data=dict(
        color=Sunset4,
        coord=["img[0,0]", "img[0,1]", "img[1,0]", "img[1,1]"],
    )
)
p.square(0, 0, color="color", legend_group="coord", source=source, visible=False)
p.legend.location = "bottom_center"
p.legend.orientation = "horizontal"
p.legend.glyph_height = 30
p.legend.glyph_width = 30
p.legend.padding = 3
p.legend.margin = 5
p.legend.label_standoff = 0
p.legend.spacing = 25
p.legend.background_fill_color = None
p.legend.border_line_color = None

anchor = Select(title="anchor", options=list(Anchor), value=r.glyph.anchor)
anchor.js_link("value", r.glyph, "anchor")

origin = Select(title="origin", options=list(ImageOrigin), value=r.glyph.origin)
origin.js_link("value", r.glyph, "origin")

show(column(p, anchor, origin))

print("------------------------------------------------------------")  # 60個

print("contour_simple 等高线的颜色填充")

from bokeh.palettes import Sunset8

# Data to contour is the sum of two Gaussian functions.
x, y = np.meshgrid(np.linspace(0, 3, 40), np.linspace(0, 2, 30))
z = 1.3 * np.exp(-2.5 * ((x - 1.3) ** 2 + (y - 0.8) ** 2)) - 1.2 * np.exp(
    -2 * ((x - 1.8) ** 2 + (y - 1.3) ** 2)
)

p = figure(width=550, height=300, x_range=(0, 3), y_range=(0, 2))

levels = np.linspace(-1, 1, 9)
contour_renderer = p.contour(x, y, z, levels, fill_color=Sunset8, line_color="black")

colorbar = contour_renderer.construct_color_bar()
p.add_layout(colorbar, "right")

show(p)

print("------------------------------------------------------------")  # 60個

print("contour 在相邻轮廓的线层之间填充多边形")

from bokeh.palettes import OrRd
from bokeh.plotting import curdoc

x, y = np.meshgrid(np.linspace(0, 4, 33), np.linspace(0, 3, 25))
z = np.sin(np.pi * x) + np.cos(np.pi * y)
levels = np.linspace(-2.0, 2.0, 9)

fig = figure(
    width=600,
    height=500,
    toolbar_location=None,
    x_range=(0, 4),
    y_range=(0, 3),
    title=r"$$\text{Contour plot of } z = \sin(\pi x) + \cos(\pi y)$$",
)

contour_renderer = fig.contour(
    x,
    y,
    z,
    levels,
    fill_color=OrRd,
    line_color=["white"] * 4 + ["black"] * 5,
    line_dash=["solid"] * 5 + ["dashed"] * 4,
    line_width=2,
)

colorbar = contour_renderer.construct_color_bar()
fig.add_layout(colorbar, "right")

curdoc().theme = "dark_minimal"

show(fig)

print("------------------------------------------------------------")  # 60個

print("contour_polar 极坐标下的等高线图")

from bokeh.palettes import Cividis

# Data to contour is a 2D sin wave on a polar grid.
radius, angle = np.meshgrid(np.linspace(0, 1, 20), np.linspace(0, 2 * np.pi, 120))
x = radius * np.cos(angle)
y = radius * np.sin(angle)
z = 1 + np.sin(3 * angle) * np.sin(np.pi * radius)

p = figure(width=550, height=400)

levels = np.linspace(0, 2, 11)

contour_renderer = p.contour(
    x=x,
    y=y,
    z=z,
    levels=levels,
    fill_color=Cividis,
    hatch_pattern=["x"] * 5 + [""] * 5,
    hatch_color="white",
    hatch_alpha=0.5,
    line_color=["white"] * 5 + ["black"] + ["red"] * 5,
    line_dash=["solid"] * 6 + ["dashed"] * 5,
    line_width=[1] * 6 + [2] * 5,
)

colorbar = contour_renderer.construct_color_bar(title="Colorbar title")
p.add_layout(colorbar, "right")

show(p)

print("------------------------------------------------------------")  # 60個

print("hexbin 将数据分箱到六边形网格，并实现每个网格的悬停交互")

from bokeh.models import HoverTool

n = 500
x = 2 + 2 * np.random.standard_normal(n)
y = 2 + 2 * np.random.standard_normal(n)

p = figure(
    title="Hexbin for 500 points",
    match_aspect=True,
    tools="wheel_zoom,reset",
    background_fill_color="#440154",
)
p.grid.visible = False

r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

p.circle(x, y, color="white", size=1)

p.add_tools(
    HoverTool(
        tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
        mode="mouse",
        point_policy="follow_mouse",
        renderers=[r],
    )
)

show(p)

print("------------------------------------------------------------")  # 60個

print("ridgeplot 用山脊图来刻画可能性")

import colorcet as cc
from numpy import linspace
from scipy.stats import gaussian_kde

from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter
from bokeh.sampledata.perceptions import probly


def ridge(category, data, scale=20):
    return list(zip([category] * len(data), scale * data))


cats = list(reversed(probly.keys()))

palette = [cc.rainbow[i * 15] for i in range(17)]

x = linspace(-20, 110, 500)

source = ColumnDataSource(data=dict(x=x))

p = figure(y_range=cats, width=900, x_range=(-5, 105), toolbar_location=None)

for i, cat in enumerate(reversed(cats)):
    pdf = gaussian_kde(probly[cat])
    y = ridge(cat, pdf(x))
    source.add(y, cat)
    p.patch("x", cat, color=palette[i], alpha=0.6, line_color="black", source=source)

p.outline_line_color = None
p.background_fill_color = "#efefef"

p.xaxis.ticker = FixedTicker(ticks=list(range(0, 101, 10)))
p.xaxis.formatter = PrintfTickFormatter(format="%d%%")

p.ygrid.grid_line_color = None
p.xgrid.grid_line_color = "#dddddd"
p.xgrid.ticker = p.xaxis.ticker

p.axis.minor_tick_line_color = None
p.axis.major_tick_line_color = None
p.axis.axis_line_color = None

p.y_range.range_padding = 0.12

show(p)

print("------------------------------------------------------------")  # 60個

print("scatter_jitter 基于github提交历史的分类散点图")

from bokeh.models import ColumnDataSource
from bokeh.sampledata.commits import data
from bokeh.transform import jitter

DAYS = ["Sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"]

source = ColumnDataSource(data)

p = figure(
    width=800,
    height=300,
    y_range=DAYS,
    x_axis_type="datetime",
    title="Commits by Time of Day (US/Central) 2012-2016",
)

p.scatter(
    x="time", y=jitter("day", width=0.6, range=p.y_range), source=source, alpha=0.3
)

p.xaxis.formatter.days = "%Hh"
p.x_range.range_padding = 0
p.ygrid.grid_line_color = None

show(p)

print("------------------------------------------------------------")  # 60個

print("les_mis 数据可视化的经典之《悲惨世界》")

from bokeh.sampledata.les_mis import data

nodes = data["nodes"]
names = [node["name"] for node in sorted(data["nodes"], key=lambda x: x["group"])]

N = len(nodes)
counts = np.zeros((N, N))
for link in data["links"]:
    counts[link["source"], link["target"]] = link["value"]
    counts[link["target"], link["source"]] = link["value"]

colormap = [
    "#444444",
    "#a6cee3",
    "#1f78b4",
    "#b2df8a",
    "#33a02c",
    "#fb9a99",
    "#e31a1c",
    "#fdbf6f",
    "#ff7f00",
    "#cab2d6",
    "#6a3d9a",
]

xname = []
yname = []
color = []
alpha = []
for i, node1 in enumerate(nodes):
    for j, node2 in enumerate(nodes):
        xname.append(node1["name"])
        yname.append(node2["name"])

        alpha.append(min(counts[i, j] / 4.0, 0.9) + 0.1)

        if node1["group"] == node2["group"]:
            color.append(colormap[node1["group"]])
        else:
            color.append("lightgrey")

data = dict(
    xname=xname,
    yname=yname,
    colors=color,
    alphas=alpha,
    count=counts.flatten(),
)

p = figure(
    title="Les Mis Occurrences",
    x_axis_location="above",
    tools="hover,save",
    x_range=list(reversed(names)),
    y_range=names,
    tooltips=[("names", "@yname, @xname"), ("count", "@count")],
)

p.width = 800
p.height = 800
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "7px"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = np.pi / 3

p.rect(
    "xname",
    "yname",
    0.9,
    0.9,
    source=data,
    color="colors",
    alpha="alphas",
    line_color=None,
    hover_line_color="black",
    hover_color="colors",
)

show(p)

print("------------------------------------------------------------")  # 60個

print("heatmap_unemployment 基于失业数据的分类热力图")

from math import pi

from bokeh.models import BasicTicker, PrintfTickFormatter
from bokeh.sampledata.unemployment1948 import data
from bokeh.transform import linear_cmap

data["Year"] = data["Year"].astype(str)
data = data.set_index("Year")
data.drop("Annual", axis=1, inplace=True)
data.columns.name = "Month"

years = list(data.index)
months = list(reversed(data.columns))

# reshape to 1D array or rates with a month and year for each row.
df = pd.DataFrame(data.stack(), columns=["rate"]).reset_index()

# this is the colormap from the original NYTimes plot
colors = [
    "#75968f",
    "#a5bab7",
    "#c9d9d3",
    "#e2e2e2",
    "#dfccce",
    "#ddb7b1",
    "#cc7878",
    "#933b41",
    "#550b1d",
]

TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

p = figure(
    title=f"US Unemployment ({years[0]} - {years[-1]})",
    x_range=years,
    y_range=months,
    x_axis_location="above",
    width=900,
    height=400,
    tools=TOOLS,
    toolbar_location="below",
    tooltips=[("date", "@Month @Year"), ("rate", "@rate%")],
)

p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "7px"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = pi / 3

r = p.rect(
    x="Year",
    y="Month",
    width=1,
    height=1,
    source=df,
    fill_color=linear_cmap("rate", colors, low=df.rate.min(), high=df.rate.max()),
    line_color=None,
)

p.add_layout(
    r.construct_color_bar(
        major_label_text_font_size="7px",
        ticker=BasicTicker(desired_num_ticks=len(colors)),
        formatter=PrintfTickFormatter(format="%d%%"),
        label_standoff=6,
        border_line_color=None,
        padding=5,
    ),
    "right",
)

show(p)

print("------------------------------------------------------------")  # 60個

print("periodic 元素周期表")

from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge, factor_cmap

periods = ["I", "II", "III", "IV", "V", "VI", "VII"]
groups = [str(x) for x in range(1, 19)]

df = elements.copy()
df["atomic mass"] = df["atomic mass"].astype(str)
df["group"] = df["group"].astype(str)
df["period"] = [periods[x - 1] for x in df.period]
df = df[df.group != "-"]
df = df[df.symbol != "Lr"]
df = df[df.symbol != "Lu"]

cmap = {
    "alkali metal": "#a6cee3",
    "alkaline earth metal": "#1f78b4",
    "metal": "#d93b43",
    "halogen": "#999d9a",
    "metalloid": "#e08d49",
    "noble gas": "#eaeaea",
    "nonmetal": "#f1d4Af",
    "transition metal": "#599d7A",
}

TOOLTIPS = [
    ("Name", "@name"),
    ("Atomic number", "@{atomic number}"),
    ("Atomic mass", "@{atomic mass}"),
    ("Type", "@metal"),
    ("CPK color", "$color[hex, swatch]:CPK"),
    ("Electronic configuration", "@{electronic configuration}"),
]

p = figure(
    title="Periodic Table (omitting LA and AC Series)",
    width=1000,
    height=450,
    x_range=groups,
    y_range=list(reversed(periods)),
    tools="hover",
    toolbar_location=None,
    tooltips=TOOLTIPS,
)

r = p.rect(
    "group",
    "period",
    0.95,
    0.95,
    source=df,
    fill_alpha=0.6,
    legend_field="metal",
    color=factor_cmap("metal", palette=list(cmap.values()), factors=list(cmap.keys())),
)

text_props = dict(source=df, text_align="left", text_baseline="middle")

x = dodge("group", -0.4, range=p.x_range)

p.text(x=x, y="period", text="symbol", text_font_style="bold", **text_props)

p.text(
    x=x,
    y=dodge("period", 0.3, range=p.y_range),
    text="atomic number",
    text_font_size="11px",
    **text_props,
)

p.text(
    x=x,
    y=dodge("period", -0.35, range=p.y_range),
    text="name",
    text_font_size="7px",
    **text_props,
)

p.text(
    x=x,
    y=dodge("period", -0.2, range=p.y_range),
    text="atomic mass",
    text_font_size="7px",
    **text_props,
)

p.text(
    x=["3", "3"],
    y=["VI", "VII"],
    text=["LA", "AC"],
    text_align="center",
    text_baseline="middle",
)

p.outline_line_color = None
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_standoff = 0
p.legend.orientation = "horizontal"
p.legend.location = "top_center"
p.hover.renderers = [r]  # only hover element boxes

show(p)

print("------------------------------------------------------------")  # 60個

print("treemap")

from squarify import normalize_sizes, squarify

from bokeh.sampledata.sample_superstore import data
from bokeh.transform import factor_cmap

data = data[["City", "Region", "Sales"]]

regions = ("West", "Central", "South", "East")

sales_by_city = data.groupby(["Region", "City"]).sum("Sales")
sales_by_city = sales_by_city.sort_values(by="Sales").reset_index()

sales_by_region = sales_by_city.groupby("Region").sum("Sales").sort_values(by="Sales")


def treemap(df, col, x, y, dx, dy, *, N=100):
    sub_df = df.nlargest(N, col)
    normed = normalize_sizes(sub_df[col], dx, dy)
    blocks = squarify(normed, x, y, dx, dy)
    blocks_df = pd.DataFrame.from_dict(blocks).set_index(sub_df.index)
    return sub_df.join(blocks_df, how="left").reset_index()


x, y, w, h = 0, 0, 800, 450

blocks_by_region = treemap(sales_by_region, "Sales", x, y, w, h)

dfs = []
for index, (Region, Sales, x, y, dx, dy) in blocks_by_region.iterrows():
    df = sales_by_city[sales_by_city.Region == Region]
    dfs.append(treemap(df, "Sales", x, y, dx, dy, N=10))
blocks = pd.concat(dfs)

p = figure(
    width=w,
    height=h,
    tooltips="@City",
    toolbar_location=None,
    x_axis_location=None,
    y_axis_location=None,
)
p.x_range.range_padding = p.y_range.range_padding = 0
p.grid.grid_line_color = None

p.block(
    "x",
    "y",
    "dx",
    "dy",
    source=blocks,
    line_width=1,
    line_color="white",
    fill_alpha=0.8,
    fill_color=factor_cmap("Region", "MediumContrast4", regions),
)

p.text(
    "x",
    "y",
    x_offset=2,
    text="Region",
    source=blocks_by_region,
    text_font_size="18pt",
    text_color="white",
)

blocks["ytop"] = blocks.y + blocks.dy
p.text(
    "x",
    "ytop",
    x_offset=2,
    y_offset=2,
    text="City",
    source=blocks,
    text_font_size="6pt",
    text_baseline="top",
    text_color=factor_cmap("Region", ("black", "white", "black", "white"), regions),
)

show(p)

print("------------------------------------------------------------")  # 60個

print("crosstab 相邻条形图")

from bokeh.core.properties import value
from bokeh.plotting import ColumnDataSource
from bokeh.sampledata.sample_superstore import data as df
from bokeh.transform import cumsum, factor_cmap

rows = pd.crosstab(
    df.Category, df.Region, aggfunc="sum", values=df.Sales, normalize="index"
)

source = ColumnDataSource(rows.T)

cats = ["Office Supplies", "Furniture", "Technology"]
regions = source.data["Region"]

p = figure(
    y_range=cats,
    x_range=(-0.55, 1.02),
    height=400,
    width=700,
    tools="",
    x_axis_location=None,
    toolbar_location=None,
    outline_line_color=None,
)
p.grid.grid_line_color = None
p.yaxis.fixed_location = 0
p.axis.major_tick_line_color = None
p.axis.major_label_text_color = None
p.axis.axis_line_color = "#4a4a4a"
p.axis.axis_line_width = 6

source.data["color"] = ["#dadada", "#dadada", "#4a4a4a", "#dadada"]
for y in cats:
    left, right = cumsum(y, include_zero=True), cumsum(y)

    p.hbar(
        y=value(y),
        left=left,
        right=right,
        source=source,
        height=0.9,
        color=factor_cmap("Region", "MediumContrast4", regions),
    )

    pcts = source.data[y]
    source.data[f"{y} text"] = [f"{r}\n{x*100:0.1f}%" for r, x in zip(regions, pcts)]

    p.text(
        y=value(y),
        x=left,
        text=f"{y} text",
        source=source,
        x_offset=10,
        text_color="color",
        text_baseline="middle",
        text_font_size="15px",
    )

totals = pd.crosstab(
    df.Category,
    df.Region,
    margins=True,
    aggfunc="sum",
    values=df.Sales,
    normalize="columns",
).All

p.hbar(right=0, left=-totals, y=totals.index, height=0.9, color="#dadada")

text = [f"{name} ({totals.loc[name]*100:0.1f}%)" for name in cats]
p.text(
    y=cats,
    x=0,
    text=text,
    text_baseline="middle",
    text_align="right",
    x_offset=-12,
    text_color="#4a4a4a",
    text_font_size="20px",
    text_font_style="bold",
)

show(p)

print("------------------------------------------------------------")  # 60個

print("texas_hover_map 基于失业数据的地图用法展示")

from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.sampledata.unemployment import data as unemployment
from bokeh.sampledata.us_counties import data as counties

palette = tuple(reversed(palette))

counties = {
    code: county for code, county in counties.items() if county["state"] == "tx"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county["name"] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)

data = dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
)

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="Texas Unemployment, 2009",
    tools=TOOLS,
    x_axis_location=None,
    y_axis_location=None,
    tooltips=[
        ("Name", "@name"),
        ("Unemployment rate", "@rate%"),
        ("(Long, Lat)", "($x, $y)"),
    ],
)
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches(
    "x",
    "y",
    source=data,
    fill_color={"field": "rate", "transform": color_mapper},
    fill_alpha=0.7,
    line_color="white",
    line_width=0.5,
)

show(p)

print("------------------------------------------------------------")  # 60個

print("tile_source 瓦片数据的使用")

# range bounds supplied in web mercator coordinates
p = figure(
    x_range=(-2000000, 2000000),
    y_range=(1000000, 7000000),
    x_axis_type="mercator",
    y_axis_type="mercator",
)

p.add_tile("CartoDB Positron", retina=True)

show(p)

print("------------------------------------------------------------")  # 60個

print("tile_xyzservices 选择不同地图数据供应方")

import xyzservices.providers as xyz

# range bounds supplied in web mercator coordinates
p = figure(
    x_range=(-2000000, 6000000),
    y_range=(-1000000, 7000000),
    x_axis_type="mercator",
    y_axis_type="mercator",
)
p.add_tile(xyz.OpenStreetMap.Mapnik)

show(p)

print("------------------------------------------------------------")  # 60個

# NG
print("tile_demo 不同图源和图层的对比")

from bokeh.layouts import layout
from bokeh.models.widgets import Div


# helper function for coordinate conversion between lat/lon in decimal degrees to web mercator
def lnglat_to_meters(longitude, latitude):
    """Projects the given (longitude, latitude) values into Web Mercator
    coordinates (meters East of Greenwich and meters North of the Equator).

    """
    origin_shift = np.pi * 6378137
    easting = longitude * origin_shift / 180.0
    northing = np.log(np.tan((90 + latitude) * np.pi / 360.0)) * origin_shift / np.pi
    return (easting, northing)


description = Div(
    text="""<b><code>tile_demo.py</code></b> - Bokeh tile provider examples. Linked Pan and Zoom on all maps!"""
)

# Lady Bird Lake, Austin Texas
lat = 30.268801
lon = -97.763347

EN = lnglat_to_meters(lon, lat)
dE = 1000  # (m) Easting  plus-and-minus from map center
dN = 1000  # (m) Northing plus-and-minus from map center

x_range = (EN[0] - dE, EN[0] + dE)  # (m) Easting  x_lo, x_hi
y_range = (EN[1] - dN, EN[1] + dN)  # (m) Northing y_lo, y_hi

providers = [
    "CartoDB Positron",
    "CartoDB Positron retina",
    "Stamen Terrain",
    "Stamen Terrain retina",
    "Stamen Toner",
    "Stamen Toner Background",
    "Stamen Toner Labels",
    "OpenStreetMap Mapnik",
    "Esri World Imagery",
]

plots = []
for i, vendor_name in enumerate(providers):
    plot = figure(
        x_range=x_range,
        y_range=y_range,
        toolbar_location=None,
        x_axis_type="mercator",
        y_axis_type="mercator",
        height=250,
        width=300,
        title=vendor_name,
    )
    # plot.add_tile(vendor_name)
    plots.append(plot)

layout = layout(
    [
        [description],
        plots[0:3],
        plots[3:6],
        plots[6:9],
    ]
)

show(layout)

print("------------------------------------------------------------")  # 60個

print("from_networkx")

import networkx as nx

from bokeh.palettes import Category20_20
from bokeh.plotting import from_networkx

G = nx.desargues_graph()  # always 20 nodes

p = figure(
    x_range=(-2, 2),
    y_range=(-2, 2),
    x_axis_location=None,
    y_axis_location=None,
    tools="hover",
    tooltips="index: @index",
)
p.grid.grid_line_color = None

graph = from_networkx(G, nx.spring_layout, scale=1.8, center=(0, 0))
p.renderers.append(graph)

# Add some new columns to the node renderer data source
graph.node_renderer.data_source.data["index"] = list(range(len(G)))
graph.node_renderer.data_source.data["colors"] = Category20_20

graph.node_renderer.glyph.update(size=20, fill_color="colors")

show(p)

print("------------------------------------------------------------")  # 60個

print("node_and_edge_attributes 鼠标悬停查看节点、关系、属性 的graph")

import networkx as nx

from bokeh.models import Circle, MultiLine
from bokeh.plotting import from_networkx

G = nx.karate_club_graph()

SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "darkgrey", "red"

edge_attrs = {}
for start_node, end_node, _ in G.edges(data=True):
    edge_color = (
        SAME_CLUB_COLOR
        if G.nodes[start_node]["club"] == G.nodes[end_node]["club"]
        else DIFFERENT_CLUB_COLOR
    )
    edge_attrs[(start_node, end_node)] = edge_color

nx.set_edge_attributes(G, edge_attrs, "edge_color")

plot = figure(
    width=400,
    height=400,
    x_range=(-1.2, 1.2),
    y_range=(-1.2, 1.2),
    x_axis_location=None,
    y_axis_location=None,
    toolbar_location=None,
    title="Graph Interaction Demo",
    background_fill_color="#efefef",
    tooltips="index: @index, club: @club",
)
plot.grid.grid_line_color = None

graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="lightblue")
graph_renderer.edge_renderer.glyph = MultiLine(
    line_color="edge_color", line_alpha=1, line_width=2
)
plot.renderers.append(graph_renderer)

show(plot)

print("------------------------------------------------------------")  # 60個

print("candlestick 股价变动的烛形图")

from bokeh.models import BoxAnnotation
from bokeh.sampledata.stocks import MSFT

df = pd.DataFrame(MSFT)[60:120]
df["date"] = pd.to_datetime(df["date"])

inc = df.close > df.open
dec = df.open > df.close

non_working_days = df[["date"]].assign(diff=df["date"].diff() - pd.Timedelta("1D"))
non_working_days = non_working_days[non_working_days["diff"] >= pd.Timedelta("1D")]

df["date"] += pd.Timedelta("12H")  # move candles to the center of the day

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(
    x_axis_type="datetime",
    tools=TOOLS,
    width=1000,
    height=400,
    title="MSFT Candlestick",
    background_fill_color="#efefef",
)
p.xaxis.major_label_orientation = 0.8  # radians

boxes = [
    BoxAnnotation(fill_color="#bbbbbb", fill_alpha=0.2, left=date - diff, right=date)
    for date, diff in non_working_days.values
]
p.renderers.extend(boxes)

p.segment(df.date, df.high, df.date, df.low, color="black")

p.vbar(df.date[dec], pd.Timedelta("16H"), df.open[dec], df.close[dec], color="#eb3c40")
p.vbar(
    df.date[inc],
    pd.Timedelta("16H"),
    df.open[inc],
    df.close[inc],
    fill_color="white",
    line_color="#49a3a3",
    line_width=2,
)

show(p)

print("------------------------------------------------------------")  # 60個

print("pie 饼图")

from math import pi
from bokeh.palettes import Category20c
from bokeh.transform import cumsum

x = {
    "United States": 157,
    "United Kingdom": 93,
    "Japan": 89,
    "China": 63,
    "Germany": 44,
    "India": 42,
    "Italy": 40,
    "Australia": 35,
    "Brazil": 32,
    "France": 31,
    "Taiwan": 31,
    "Spain": 29,
}

data = pd.Series(x).reset_index(name="value").rename(columns={"index": "country"})
data["angle"] = data["value"] / data["value"].sum() * 2 * pi
data["color"] = Category20c[len(x)]

p = figure(
    height=350,
    title="Pie Chart",
    toolbar_location=None,
    tools="hover",
    tooltips="@country: @value",
    x_range=(-0.5, 1.0),
)

p.wedge(
    x=0,
    y=1,
    radius=0.4,
    start_angle=cumsum("angle", include_zero=True),
    end_angle=cumsum("angle"),
    line_color="white",
    fill_color="color",
    legend_field="country",
    source=data,
)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)

print("------------------------------------------------------------")  # 60個

print("donut 甜甜圈")

from math import pi

from bokeh.io import show
from bokeh.models import (
    AnnularWedge,
    ColumnDataSource,
    Legend,
    LegendItem,
    Plot,
    Range1d,
)
from bokeh.sampledata.browsers import browsers_nov_2013 as df

xdr = Range1d(start=-2, end=2)
ydr = Range1d(start=-2, end=2)

plot = Plot(x_range=xdr, y_range=ydr)
plot.title.text = "Web browser market share (November 2013)"
plot.toolbar_location = None

colors = {
    "Chrome": "seagreen",
    "Firefox": "tomato",
    "Safari": "orchid",
    "Opera": "firebrick",
    "IE": "skyblue",
    "Other": "lightgray",
}

aggregated = df.groupby("Browser").sum(numeric_only=True)
selected = aggregated[aggregated.Share >= 1].copy()
selected.loc["Other"] = aggregated[aggregated.Share < 1].sum()
browsers = selected.index.tolist()

angles = selected.Share.map(lambda x: 2 * pi * (x / 100)).cumsum().tolist()

browsers_source = ColumnDataSource(
    dict(
        start=[0] + angles[:-1],
        end=angles,
        colors=[colors[browser] for browser in browsers],
    )
)

glyph = AnnularWedge(
    x=0,
    y=0,
    inner_radius=0.9,
    outer_radius=1.8,
    start_angle="start",
    end_angle="end",
    line_color="white",
    line_width=3,
    fill_color="colors",
)
r = plot.add_glyph(browsers_source, glyph)

legend = Legend(location="center")
for i, name in enumerate(colors):
    legend.items.append(LegendItem(label=name, renderers=[r], index=i))
plot.add_layout(legend, "center")

show(plot)

print("------------------------------------------------------------")  # 60個

print("burtin 抗生素的效用历史")

from numpy import arange, array, cos, log, pi, sin, sqrt
from bokeh.models import ColumnDataSource, Legend, LegendItem
from bokeh.sampledata.antibiotics import data as df

DRUGS = ("penicillin", "streptomycin", "neomycin")
COLORS = ("#0d3362", "#c64737", "#000000")
GRAM = dict(
    [
        ("negative", "#e69584"),
        ("positive", "#aeaeb8"),
    ]
)

big_angle = 2 * pi / (len(df) + 1)
angles = pi / 2 - 3 * big_angle / 2 - array(df.index) * big_angle

df["start"] = angles
df["end"] = angles + big_angle
df["colors"] = [GRAM[gram] for gram in df.gram]

source = ColumnDataSource(df)

# Burtin's unusual inverted radial sqrt-log scale
micmin = sqrt(log(0.001 * 1e4))
micmax = sqrt(log(1000 * 1e4))


def scale(mic):
    return -sqrt(log(mic * 1e4)) + (micmin + micmax)


p = figure(
    width=800,
    height=800,
    title=None,
    tools="",
    toolbar_location=None,
    x_axis_type=None,
    y_axis_type=None,
    match_aspect=True,
    min_border=0,
    outline_line_color="black",
    background_fill_color="#f0e1d2",
)

# large wedges for bacteria
br = p.annular_wedge(
    0,
    0,
    micmax,
    micmin,
    "start",
    "end",
    fill_color="colors",
    line_color="#f0e1d2",
    source=source,
)

# circular axes and labels
radii = scale(10.0 ** arange(-3, 4))
p.circle(0, 0, radius=radii, fill_color=None, line_color="#f0e1d2")
p.text(
    0,
    radii,
    ["0.001", "0.01", "0.1", "1", "10", "100", "1000"],
    text_font_size="12px",
    anchor="center",
)

# small wedges for drugs
small_angle = big_angle / 7
for i, drug in enumerate(DRUGS):
    start = angles + (5 - 2 * i) * small_angle
    end = angles + (6 - 2 * i) * small_angle
    p.annular_wedge(
        0,
        0,
        micmin,
        scale(df[drug]),
        start,
        end,
        color=COLORS[i],
        line_color=None,
        legend_label=drug,
    )

# bacteria labels
r = radii[0] * 1.1
xr = r * cos(angles + big_angle / 2)
yr = r * sin(angles + big_angle / 2)
p.text(
    xr,
    yr,
    ["\n".join(x.split()) for x in df.bacteria],
    text_font_size="13px",
    anchor="center",
)

p.legend.location = "center"
p.legend.background_fill_alpha = 0
p.legend.glyph_width = 45
p.legend.glyph_height = 20

p.x_range.range_padding = 0.2
p.y_range.range_padding = 0.2

p.grid.grid_line_color = None

legend = Legend(
    items=[
        LegendItem(label="Gram-positive", renderers=[br], index=10),
        LegendItem(label="Gram-negative", renderers=[br], index=0),
    ],
    location="bottom",
    orientation="horizontal",
    background_fill_alpha=0,
)
p.add_layout(legend, "center")

show(p)

print("------------------------------------------------------------")  # 60個

print("histogram 高斯分布直方图")

rng = np.random.default_rng()
x = rng.normal(loc=0, scale=1, size=1000)

p = figure(
    width=670, height=400, toolbar_location=None, title="Normal (Gaussian) Distribution"
)

# Histogram
bins = np.linspace(-3, 3, 40)
hist, edges = np.histogram(x, density=True, bins=bins)
p.quad(
    top=hist,
    bottom=0,
    left=edges[:-1],
    right=edges[1:],
    fill_color="skyblue",
    line_color="white",
    legend_label="1000 random samples",
)

# Probability density function
x = np.linspace(-3.0, 3.0, 100)
pdf = np.exp(-0.5 * x**2) / np.sqrt(2.0 * np.pi)
p.line(
    x, pdf, line_width=2, line_color="navy", legend_label="Probability Density Function"
)

p.y_range.start = 0
p.xaxis.axis_label = "x"
p.yaxis.axis_label = "PDF(x)"

show(p)

print("------------------------------------------------------------")  # 60個

print("kde2d 双变量核密度估计")

from scipy.stats import gaussian_kde
from bokeh.palettes import Blues9
from bokeh.sampledata.autompg import autompg as df


def kde(x, y, N):
    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()

    X, Y = np.mgrid[xmin : xmax : N * 1j, ymin : ymax : N * 1j]
    positions = np.vstack([X.ravel(), Y.ravel()])
    values = np.vstack([x, y])
    kernel = gaussian_kde(values)
    Z = np.reshape(kernel(positions).T, X.shape)

    return X, Y, Z


x, y, z = kde(df.hp, df.mpg, 300)

p = figure(
    height=400,
    x_axis_label="hp",
    y_axis_label="mpg",
    background_fill_color="#fafafa",
    tools="",
    toolbar_location=None,
    title="Kernel density estimation plot of HP vs MPG",
)
p.grid.level = "overlay"
p.grid.grid_line_color = "black"
p.grid.grid_line_alpha = 0.05

palette = Blues9[::-1]
levels = np.linspace(np.min(z), np.max(z), 10)
p.contour(x, y, z, levels[1:], fill_color=palette, line_color=palette)

show(p)

print("------------------------------------------------------------")  # 60個

print("splom 用散点图矩阵 (SPLOM)进行三个变量的相关性分析")

# noqa: E501
from itertools import product

from bokeh.io import show
from bokeh.layouts import gridplot
from bokeh.models import (
    BasicTicker,
    Circle,
    ColumnDataSource,
    DataRange1d,
    Grid,
    LassoSelectTool,
    LinearAxis,
    PanTool,
    Plot,
    ResetTool,
    WheelZoomTool,
)
from bokeh.sampledata.penguins import data
from bokeh.transform import factor_cmap

df = data.copy()
df["body_mass_kg"] = df["body_mass_g"] / 1000

SPECIES = sorted(df.species.unique())
ATTRS = ("bill_length_mm", "bill_depth_mm", "body_mass_kg")
N = len(ATTRS)

source = ColumnDataSource(data=df)

xdrs = [DataRange1d(bounds=None) for _ in range(N)]
ydrs = [DataRange1d(bounds=None) for _ in range(N)]

plots = []

for i, (y, x) in enumerate(product(ATTRS, reversed(ATTRS))):
    p = Plot(
        x_range=xdrs[i % N],
        y_range=ydrs[i // N],
        background_fill_color="#fafafa",
        border_fill_color="white",
        width=200,
        height=200,
        min_border=5,
    )

    if i % N == 0:  # first column
        p.min_border_left = p.min_border + 4
        p.width += 40
        yaxis = LinearAxis(axis_label=y)
        yaxis.major_label_orientation = "vertical"
        p.add_layout(yaxis, "left")
        yticker = yaxis.ticker
    else:
        yticker = BasicTicker()
    p.add_layout(Grid(dimension=1, ticker=yticker))

    if i >= N * (N - 1):  # last row
        p.min_border_bottom = p.min_border + 40
        p.height += 40
        xaxis = LinearAxis(axis_label=x)
        p.add_layout(xaxis, "below")
        xticker = xaxis.ticker
    else:
        xticker = BasicTicker()
    p.add_layout(Grid(dimension=0, ticker=xticker))

    circle = Circle(
        x=x,
        y=y,
        fill_alpha=0.6,
        size=5,
        line_color=None,
        fill_color=factor_cmap("species", "Category10_3", SPECIES),
    )
    r = p.add_glyph(source, circle)
    p.x_range.renderers.append(r)
    p.y_range.renderers.append(r)

    # suppress the diagonal
    if (i % N) + (i // N) == N - 1:
        r.visible = False
        p.grid.grid_line_color = None

    p.add_tools(PanTool(), WheelZoomTool(), ResetTool(), LassoSelectTool())

    plots.append(p)

show(gridplot(plots, ncols=N))

print("------------------------------------------------------------")  # 60個

print("boxplot 箱线图")

from bokeh.models import ColumnDataSource, Whisker
from bokeh.sampledata.autompg2 import autompg2
from bokeh.transform import factor_cmap

df = autompg2[["class", "hwy"]].rename(columns={"class": "kind"})

kinds = df.kind.unique()

# compute quantiles
qs = df.groupby("kind").hwy.quantile([0.25, 0.5, 0.75])
qs = qs.unstack().reset_index()
qs.columns = ["kind", "q1", "q2", "q3"]
df = pd.merge(df, qs, on="kind", how="left")

# compute IQR outlier bounds
iqr = df.q3 - df.q1
df["upper"] = df.q3 + 1.5 * iqr
df["lower"] = df.q1 - 1.5 * iqr

source = ColumnDataSource(df)

p = figure(
    x_range=kinds,
    tools="",
    toolbar_location=None,
    title="Highway MPG distribution by vehicle class",
    background_fill_color="#eaefef",
    y_axis_label="MPG",
)

# outlier range
whisker = Whisker(base="kind", upper="upper", lower="lower", source=source)
whisker.upper_head.size = whisker.lower_head.size = 20
p.add_layout(whisker)

# quantile boxes
cmap = factor_cmap("kind", "TolRainbow7", kinds)
p.vbar("kind", 0.7, "q2", "q3", source=source, color=cmap, line_color="black")
p.vbar("kind", 0.7, "q1", "q2", source=source, color=cmap, line_color="black")

# outliers
outliers = df[~df.hwy.between(df.lower, df.upper)]
p.scatter("kind", "hwy", source=outliers, size=6, color="black", alpha=0.3)

p.xgrid.grid_line_color = None
p.axis.major_label_text_font_size = "14px"
p.axis.axis_label_text_font_size = "12px"

show(p)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

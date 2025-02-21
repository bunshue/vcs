"""
module_bokeh_官網範例

看似只能一次顯示一圖


https://docs.bokeh.org/en/latest/docs/reference/sampledata.html#

"""

import sys

print("------------------------------------------------------------")  # 60個

from bokeh.plotting import figure, show
from bokeh.sampledata.iris import flowers

# iris

colormap = {"setosa": "red", "versicolor": "green", "virginica": "blue"}
colors = [colormap[x] for x in flowers["species"]]

p = figure(title="Iris Morphology")
p.xaxis.axis_label = "Petal Length"
p.yaxis.axis_label = "Petal Width"

p.scatter(
    flowers["petal_length"],
    flowers["petal_width"],
    color=colors,
    fill_alpha=0.2,
    size=10,
)

show(p)


print("------------------------------------------------------------")  # 60個

"""
# titanic
import numpy as np

from bokeh.models import CustomJSTickFormatter, Label
from bokeh.palettes import DarkText, Vibrant3 as colors
from bokeh.plotting import figure, show
# NG from bokeh.sampledata.titanic import data as df

sex_group = df.groupby("sex")

female_ages = sex_group.get_group("female")["age"].dropna()
male_ages = sex_group.get_group("male")["age"].dropna()

bin_width = 5
bins = np.arange(0, 72, bin_width)
m_hist, edges = np.histogram(male_ages, bins=bins)
f_hist, edges = np.histogram(female_ages, bins=bins)

p = figure(title="Age population pyramid of titanic passengers, by gender", height=400, width=600,
           x_range=(-90, 90), x_axis_label="count")

p.hbar(right=f_hist, y=edges[1:], height=bin_width*0.8, color=colors[0], line_width=0)

p.hbar(right=m_hist * -1, y=edges[1:], height=bin_width*0.8, color=colors[1], line_width=0)

# add text to every other bar
for i, (count, age) in enumerate(zip(f_hist, edges[1:])):
    if i % 2 == 1:
        continue
    p.text(x=count, y=edges[1:][i], text=[f"{age-bin_width}-{age}yrs"],
           x_offset=5, y_offset=7, text_font_size="12px", text_color=DarkText[5])

# customise x-axis and y-axis
p.xaxis.ticker = (-80, -60, -40, -20, 0, 20, 40, 60, 80)
p.xaxis.major_tick_out = 0
p.y_range.start = 3
p.ygrid.grid_line_color = None
p.yaxis.visible = False

# format tick labels as absolute values for the two-sided plot
p.xaxis.formatter = CustomJSTickFormatter(code="return Math.abs(tick);")

# add labels
p.add_layout(Label(x=-40, y=70, text="Men", text_color=colors[1], x_offset=5))
p.add_layout(Label(x=20, y=70, text="Women", text_color=colors[0], x_offset=5))

show(p)
"""

print("------------------------------------------------------------")  # 60個

# periodic_table

from bokeh.plotting import figure, show
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
    **text_props
)

p.text(
    x=x,
    y=dodge("period", -0.35, range=p.y_range),
    text="name",
    text_font_size="7px",
    **text_props
)

p.text(
    x=x,
    y=dodge("period", -0.2, range=p.y_range),
    text="atomic mass",
    text_font_size="7px",
    **text_props
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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

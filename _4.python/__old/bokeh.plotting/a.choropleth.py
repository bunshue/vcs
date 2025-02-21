"""
choropleth 分級著色圖

"""

from os.path import abspath
import webbrowser
import pandas as pd
import holoviews as hv
from holoviews import opts

hv.extension("bokeh")

# import fail
# from bokeh.sampledata.us_counties import data as counties

df = pd.read_csv("census_data_popl_2010.csv", encoding="utf-8")

df = pd.DataFrame(
    df,
    columns=[
        "Target Geo Id2",
        "Geographic area.1",
        "Density per square mile of land area - Population",
    ],
)

df.rename(
    columns={
        "Target Geo Id2": "fips",
        "Geographic area.1": "County",
        "Density per square mile of land area - Population": "Density",
    },
    inplace=True,
)

print(f"\nInitial popl data:\n {df.head()}")
print(f"Shape of df = {df.shape}\n")

# 刪除無關的列
df = df[df["fips"] > 100]
print(f"Popl data with non-county rows removed:\n {df.head()}")
print(f"Shape of df = {df.shape}\n")

# 為州代碼和縣代碼創造新欄位
df["state_id"] = (df["fips"] // 1000).astype("int64")
df["cid"] = (df["fips"] % 1000).astype("int64")
print(f"Popl data with new ID columns:\n {df.head()}")
print(f"Shape of df = {df.shape}\n")
print("df info:")
print(df.info())  # 印出 DataFrame 的簡明摘要

# 印出第 500 列資料
print("\nPopl data at row 500:")
print(df.loc[500])

# 使地圖更加顯眼 (之後加上的)
# df.loc[df.Density >= 65, ['Density']] = 1000

# 準備用於繪圖的人口資料
state_ids = df.state_id.tolist()
cids = df.cid.tolist()
den = df.Density.tolist()
tuple_list = tuple(zip(state_ids, cids))
popl_dens_dict = dict(zip(tuple_list, den))

EXCLUDED = ("ak", "hi", "pr", "gu", "vi", "mp", "as")

# fail here
counties = [
    dict(county, Density=popl_dens_dict[cid])
    for cid, county in counties.items()
    if county["state"] not in EXCLUDED
]

# 建立區域密度圖
choropleth = hv.Polygons(
    counties, ["lons", "lats"], [("detailed name", "County"), "Density"]
)

choropleth.opts(
    opts.Polygons(
        logz=True,
        tools=["hover"],
        xaxis=None,
        yaxis=None,
        show_grid=False,
        show_frame=False,
        width=1100,
        height=700,
        colorbar=True,
        toolbar="above",
        color_index="Density",
        cmap="Greys",
        line_color=None,
        title="2010 Population Density per Square Mile of Land Area",
    )
)

# 儲存區域密度圖，並另開新分頁顯示
hv.save(choropleth, "tmp_choropleth.html", backend="bokeh")
url = abspath("tmp_choropleth.html")
webbrowser.open(url)

"""
測試 ipython
IPython 是一個強大的 Python 互動式命令列與計算環境。
它比預設的 Python 直譯器更好用，
提供語法突顯、自動完成、多行編輯以及神奇指令（Magic Commands），
也是 Jupyter Notebook 的核心基礎。

Tab 鍵自動完成：快速尋找變數、函數與物件屬性。
物件檢視：在變數或函數後加上問號 ? 查看說明，或用 ?? 查看原始碼。
神奇指令（Magic Commands）：使用 % 開頭的指令（如 %timeit 測量執行時間、%run 執行腳本）來控制環境。
系統指令整合：使用 ! 開頭直接執行終端機（Shell）指令。

安裝 : pip install ipython

在終端機中輸入 ipython 並按下 Enter 即可啟動啟動。

基本指令：%run script.py

測試「整支檔案」或「單行程式」的平均速度（%timeit）
這個指令會自動把程式重複執行很多次，並算出最準確的平均執行時間（適合測試微小的效能差異）。

測試整支檔案：python%timeit %run script.py

測試單行程式：python
%timeit [x**2 for x in range(1000)]


IPython.display 這個模組是設計給網頁型圖形前端（例如 Jupyter Notebook 或 JupyterLab）使用的。


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

"""
# 取得目前資料夾底下的檔案清單，並存進 Python 變數
files = !dir

# 現在 files 變成一個 Python 列表了，可以直接用 Python 處理它！
print(f"這個資料夾裡共有 {len(files)} 行系統輸出")
"""

print("------------------------------------------------------------")  # 60個

"""
from IPython.nbformat import read

links = []
for folder, _, filenames in os.walk("."):
    for filename in filenames:
        if re.match(r"\w+-[0-9a-zA-Z]\d\d-.+?\.ipynb$", filename):
            fullpath = path.join(folder, filename)
            print(fullpath)

            book = read(fullpath, 4)
            for cell in book.cells:
                if cell.cell_type == "markdown" and cell.source.startswith("#"):
                    title = cell.source.strip("# ")
                    name = path.splitext(filename)[0]
                    folder = path.basename(folder)
                    link = u"[{title} - {name}]({folder}/{name}.ipynb)".format(
                        title=title, name=name, folder=folder)
                    links.append(link)
                    break
"""



from IPython.display import display_markdown

# 定義一段包含 Markdown 語法的字串
markdown_content = """
# 🚀 歡迎來到 IPython 實驗室

這不是一般的純文字，而是**動態渲染**的排版！

### 📊 今日效能數據

| 項目 | 狀態 | 速度 |
| :--- | :--- | :--- |
| CPU | 正常 | 1.2 ms |
| GPU | 高速 | 0.5 ms |

### 💻 範例程式碼
```python
def hello():
    print("Hello IPython!")
```
---
*提示：您隨時可以使用 `%run` 來測試您的腳本。*
"""

# 使用 display_markdown 渲染並顯示
display_markdown(markdown_content, raw=True)


print("------------------------------------------------------------")  # 60個


"""
from IPython.nbformat import read

links = []
for folder, _, filenames in os.walk("."):
    for filename in filenames:
        if re.match(r"\w+-[0-9a-zA-Z]\d\d-.+?\.ipynb$", filename):
            fullpath = path.join(folder, filename)
            print(fullpath)

            book = read(fullpath, 4)
            for cell in book.cells:
                if cell.cell_type == "markdown" and cell.source.startswith("#"):
                    title = cell.source.strip("# ")
                    name = path.splitext(filename)[0]
                    folder = path.basename(folder)
                    link = u"[{title} - {name}]({folder}/{name}.ipynb)".format(
                        title=title, name=name, folder=folder)
                    links.append(link)
                    break
"""


from IPython.display import display_markdown  # 用IPython
from IPython.display import Markdown  # 用IPython

links = []

links.append("aaa")
links.append("bbb")
links.append("ccc")
display_markdown(Markdown("\n\n".join(links)))

print("------------------------------------------------------------")  # 60個


# from IPython.html import widgets
# from IPython.html.widgets import interact

slider = widgets.FloatSliderWidget(min=0, max=4, value=2)

# from IPython.html.widgets import interact

# NG interact(plot_3D, elev=[-90, 90], azip=(-180, 180))
# NG interact(plot_fit, degree=[1, 30], Npts=[2, 100])

# dimensionality reduction techniques
# Principal component analysis (PCA)
# Independent component analysis (ICA)
# Random projections (RP)


# 搜尋開始	python	 interact(
# NG interact(plot_svm, N=[10, 200], kernel='linear')
# NG interact(plot_3D, elev=[-90, 90], azip=(-180, 180))
# NG interact(plot_fit, degree=[1, 30], Npts=[2, 100])
# interact(fit_randomized_tree, random_state=[0, 100])
# 上面搜尋到的資料在檔案	D:\_git\vcs\_4.python\__code\data-science-ipython-notebooks-master\scikit-learn\scikit-learn01.py

interact(plot_pdfs, cohen_d=slider)
# 上面搜尋到的資料在檔案	D:\_git\vcs\_4.python\__code\data-science-ipython-notebooks-master\scipy\scipy_新進1.py

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



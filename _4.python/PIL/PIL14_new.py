"""

"""

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個



from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (360, 180))  # 建立色彩模式為 RGBA，尺寸 360x180 的空白圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 40)  # 設定字型與尺寸
draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
# 將文字畫入圖片
draw.text(
    (10, 120),
    "OXXO.STUDIO",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="red",
)
draw.text(
    xy=(50, 0),
    text="大家好\n哈哈",
    align="center",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="blue",
)
img.save("ok.png")  # 儲存為 png




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('完成')



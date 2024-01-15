import sys

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
font_filename = 'C:/_git/vcs/_1.data/______test_files5/taipei_sans_tc_beta.ttf'


print("------------------------------------------------------------")  # 60個



import sys

"""
#form PIL import Image

source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for file in allfiles:
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
"""
print("------------------------------------------------------------")  # 60個

import os
from PIL import Image

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
"""

post_html = """
</table>
</body>
</html>
"""
"""
table_html = ""

source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for file in allfiles:
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容            
            table_html += "<tr><td><a href='{}'><img src='{}'></a></td></tr>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

import os
from PIL import Image

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
<tr>
"""

post_html = """
</tr>
</table>
</body>
</html>
"""


table_html = ""
"""
source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for index, file in enumerate(allfiles):
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容         
            table_html += "<td><a href='{}'><img src='{}'></a></td>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
            if (index+1) % 3 == 0:
                table_html += "</tr><tr>"
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

from PIL import Image

def blue_to_red(image_path):
    img = Image.open(image_path)
    r, g, b = img.split() # 分離三個通道
    img = Image.merge("RGB",(b,g,r))# 將藍色通道和通道互換
    img.show()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#blue_to_red(filename)

print('------------------------------------------------------------')	#60個

"""
from PIL import Image

def blue_to_red2(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            #若該點的藍色成分明顯超過紅色及綠色,我們便將之視為藍色
            if b > r and b > g:
                #將藍色分轉為紅色
                pixels[x, y] = (b, g, r)
    img.show()
    
    
    
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
blue_to_red2(filename)
"""    


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

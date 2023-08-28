import keyword

print(keyword.kwlist)


import builtins
print(dir(builtins))


week = {
    'Sunday': "星期日", 
    'Monday': "星期一", 
    'Tuesday': "星期二", 
    'Wednesday': "星期三", 
    'Thursday': "星期四", 
    'Friday': "星期五", 
    'Saturday': "星期六", 
}
print(week)
print(week['Sunday'])
print(week.keys())
print(week.values())
print(week.items())



data = {'宋遠橋':56, '俞蓮舟':55, '俞岱嚴':53}
data['張松溪'] = 50
data['張翠山'] = 45
data['殷梨亭'] = 40
data['莫聲谷'] = 28
print(data)



data = {'Tom':2230, 'Richard':28000, 'Judy':1890, 'Mary':25430}
for name, bonus in data.items():
    print("{:15s}${:09.2f}".format(name, bonus))



import time
print(time.time())


import time
print(time.localtime())

import time
year, month, day, hour, minute, second, _, _, _ = time.localtime()
print("{}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second))


import time
print(time.asctime())

import time
print(time.strftime("%Y-%m-%d %H:%M:%S %a"))


'''
from datetime import datetime
now = datetime.now()
print("今天是{}".format(datetime.strftime(now, "%Y-%m-%d")))
date = input("請輸入一個日期（yyyy-mm-dd):")
target = datetime.strptime(date, "%Y-%m-%d")
diff = now-target
print("到今天共經過了{}天。".format(diff.days))


import calendar
print(calendar.month(2018,10))
print(calendar.calendar(2019))
'''



import sys
print(sys.version_info)
print("---")
print(sys.platform)
print("---")
print(sys.argv)
print("---")
print(sys.path)




import os
items = os.listdir()
print(os.path.exists('myprime.py'))
for item in items:
    print(os.path.abspath(item))



import os
fullpath = os.path.abspath('myprime.py')
print(fullpath)
print("os.path.basename:", os.path.basename(fullpath))
print("os.path.dirname:", os.path.dirname(fullpath))
print("os.path.getatime:", os.path.getatime(fullpath))
print("os.path.getmtime:", os.path.getmtime(fullpath))
print("os.path.getctime:", os.path.getctime(fullpath))
print("os.path.getsize:", os.path.getsize(fullpath))
print("os.path.isabs:", os.path.isabs(fullpath))
print("os.path.isfile:", os.path.isfile(fullpath))
print("os.path.isdir:", os.path.isdir(fullpath))
print("os.path.split:", os.path.split(fullpath))
print("os.path.splitdrive:", os.path.splitdrive(fullpath))
print("os.path.splitext:", os.path.splitext(fullpath))




import shutil
import os
fullpath = os.path.abspath('myprime.py')
path, filename = os.path.split(fullpath)
filename, extname = os.path.splitext(filename)
if not os.path.exists("test-dir"):
    os.mkdir("test-dir")
targetfullpath = os.path.join(path, os.path.join("test-dir", "00"+extname))
shutil.copy(fullpath, targetfullpath)

try:
    print("實際上預期可能會有例外的程式碼寫在這裡！")
    10 / 0
    print("在可能發生例外的指令之下的程式碼放在這邊！")
except Exception as e:
    print("發生錯誤了，錯誤訊息如下：")
    print(e)
else:
    print("沒有發生任何錯誤。")
finally:
    print("不管如何，都要執行這裡")

from PIL import Image
im = Image.open("myIS300.jpg")
print(im.format, im.size, im.mode)
im.close()



from PIL import Image
im = Image.open("myIS300.jpg")
smaller = im.resize((640,480))
smaller.show()
smaller.save("myIS300s.jpg")
im.close()




import os
print(os.getcwd())



import os
form PIL import Image

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


import os
from PIL import Image

pre_html = '''
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
'''

post_html = '''
</table>
</body>
</html>
'''

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


import os
from PIL import Image

pre_html = '''
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
<tr>
'''

post_html = '''
</tr>
</table>
</body>
</html>
'''

table_html = ""

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

    













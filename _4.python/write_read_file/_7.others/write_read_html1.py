import os
import sys

print("------------------------------------------------------------")  # 60個

print("python寫資料到 html 檔")

print("------------------------------------------------------------")  # 60個

html_filename = 'tmp_html_data1.html'

import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print(df)

df.to_html(html_filename)

print("------------------------------------------------------------")  # 60個

print("讀取一個 html 檔案 : " + html_filename)

import pandas as pd
data = pd.read_html(html_filename, encoding="utf-8-sig", index_col=0)

print(data[0])

print("------------------------------------------------------------")  # 60個

filename1 = 'C:/_git/vcs/_4.python/write_read_file/_7.others/images/book01.jpg'
filename2 = 'C:/_git/vcs/_4.python/write_read_file/_7.others/images/book02.jpg'
filename3 = 'C:/_git/vcs/_4.python/write_read_file/_7.others/images/book03.png'
filename4 = 'C:/_git/vcs/_4.python/write_read_file/_7.others/images/book04.png'
filename5 = 'C:/_git/vcs/_4.python/write_read_file/_7.others/images/book05.png'
filename6 = 'C:/_git/vcs/_4.python/write_read_file/_7.others/images/book06.png'
filename7 = 'C:/_git/vcs/_4.python/write_read_file/_7.others/images/book07.png'

all_list = [filename1, filename2, filename3, filename4, filename5, filename6, filename7]

html_filename = 'tmp_html_data2.html'
if os.path.exists(html_filename):  
    os.remove(html_filename)     # 若有 tmp_html_data2.html 網頁即刪除

print('製作html檔案')
fw=open(html_filename,'w',encoding='UTF-8')
fw.write('<!DOCTYPE html>\n')
fw.write('<html>\n')
fw.write('<head><meta charset="utf-8" />\n')
fw.write('<title>農村地方美食小吃特色料理</title>\n')
fw.write('</head>\n')
fw.write('<body>\n')

#網頁CSS樣式設定
style="""
<style> 
img { 
   border-radius: 4px 4px 0 0; height:180px; 
   width:100%; 
} 
.card { 
   box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); 
   width: 280px ; 
   border-radius: 5px; 
   border:1px #FFF2C1 solid; float: left; 
   margin:13px; 
} 
.card:hover { 
   box-shadow: 0 8px 16px 0 #FCC592; 
} 
.txt { 
   padding: 2px 16px; 
   height:110px;
   background-color:#FEE3AD; 
} 
</style>       
"""
fw.write('\n'+style+'\n')

#HTML標籤與開放資料整合成網頁內容
cnt = 0
for row in all_list:
    print("cnt = ", cnt)
    #網址用'/'分隔取最後一筆資料 => *.jpg
    picName = row.split('/')[-1]
    print('圖片網址：', row)
    print('圖片檔名：', picName)
    
    fw.write('<div class="card">\n') #設定外層div以及屬性
    # 設置圖片的相對路徑，路徑為 'images/檔名'
    fw.write('  <img src="'+ 'images' +'/'+ picName + '">\n')
    fw.write('  <div class="txt">\n') #設定文字div以及屬性
    #fw.write('     <h4><b>'+row['Name']+'</b></h4>\n') #寫入店家名稱
    fw.write('     <h4><b>'+"姓名姓名姓名姓名姓名"+'</b></h4>\n') #寫入資料
    fw.write('     <p>'+"地址地址地址地址地址"+'</p>\n') #寫入資料
    fw.write('  </div>\n') 
    fw.write('</div>\n\n')
    cnt += 1
    if cnt >= 10:
        break

fw.write('</body>\n') 
fw.write('</html>\n') 
fw.close()

#os.system(html_filename)  # 開啟網頁
print("%s 網頁建置完成" % (html_filename))

print("------------------------------------------------------------")  # 60個

pre_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>中油油價歷史資料</title>
</head>
<body>
<h2>中油油價歷史資料（取自中油官方網站）</h2>
<table width=600 border=1>
<tr><td>日期</td><td>92無鉛</td><td>95無鉛</td><td>98無鉛</td></tr>
"""

post_html = """
</table>
</body>
</html>
"""

prices = list()
#item = [cols[0].text, cols[1].text, cols[2].text, cols[3].text]
prices.append('1234')

html_body = ''
for p in prices:
    html_body += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".\
          format(p[0],p[1],p[2],p[3])
html_file = pre_html + html_body + post_html

fp = open('tmp_oilprice.html','w')
fp.write(html_file)
fp.close()

print("------------------------------------------------------------")  # 60個

from lxml import etree,html

# htm文件路径，以及读取文件
path = "data/tmp1.htm"
content = open(path,"rb").read()
page = html.document_fromstring(content) # 解析文件
text = page.text_content() # 去除所有标签
print(text)	 # 输出去除标签后解析结果

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




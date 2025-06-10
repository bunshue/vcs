"""
Python自學聖經(第二版) 14~22

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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



# ch14\df1.py

import pandas as pd
df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]])
print(df)

print("------------------------------------------------------------")  # 60個

# ch14\df2.py

import pandas as pd
df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]],
                   index=['王小明','李小美','陳大同','林小玉'],
                   columns=['國文','英文','數學','自然','社會'])
print(df)

print("------------------------------------------------------------")  # 60個

# ch14\df3.py

import pandas as pd
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)
print(df)    

print("------------------------------------------------------------")  # 60個

# ch14\df3_.py

import pandas as pd
scores = {'王小明':{'國文':65,'英文':92,'數學':78,'社會':83,'自然':70},
          '李小美':{'國文':90,'英文':72,'數學':76,'社會':93,'自然':56},
          '陳大同':{'國文':81,'英文':85,'數學':91,'社會':89,'自然':77},
          '林小玉':{'國文':79,'英文':53,'數學':47,'社會':94,'自然':80}}
df = pd.DataFrame(scores)
print(df)    

print("------------------------------------------------------------")  # 60個

# ch14\df4.py

import pandas as pd
se1 = pd.Series({'王小明':65,'李小美':90,'陳大同':81,'林小玉':79})
se2 = pd.Series({'王小明':92,'李小美':72,'陳大同':85,'林小玉':53})
se3 = pd.Series({'王小明':78,'李小美':76,'陳大同':91,'林小玉':47})
se4 = pd.Series({'王小明':83,'李小美':93,'陳大同':89,'林小玉':94})
se5 = pd.Series({'王小明':70,'李小美':56,'陳大同':94,'林小玉':80})
df = pd.DataFrame({'國文':se1, '英文':se2, '數學':se3, '自然':se4, '社會':se5})
print(df)

print("------------------------------------------------------------")  # 60個

# ch14\df5.py

import pandas as pd
se1 = pd.Series({'王小明':65,'李小美':90,'陳大同':81,'林小玉':79})
se2 = pd.Series({'王小明':92,'李小美':72,'陳大同':85,'林小玉':53})
se3 = pd.Series({'王小明':78,'李小美':76,'陳大同':91,'林小玉':47})
se4 = pd.Series({'王小明':83,'李小美':93,'陳大同':89,'林小玉':94})
se5 = pd.Series({'王小明':70,'李小美':56,'陳大同':94,'林小玉':80})
df = pd.concat([se1,se2,se3,se4,se5], axis=1)
df.columns=['國文','英文','數學','自然','社會']
print(df)

print("------------------------------------------------------------")  # 60個

# ch14\df6.py

import pandas as pd
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)
print(df["自然"])
print(df[["國文", "數學", "自然"]])
print(df[df["國文"] >= 80])
print(df.values)
print(df.values[1])
print(df.values[1][2])
# loc
print(df.loc["林小玉", "社會"])
print(df.loc["王小明", ["國文","社會"]])
print(df.loc[["王小明", "李小美"], ["數學", "自然"]])
print(df.loc["王小明":"陳大同", "數學":"社會"])
print(df.loc["陳大同", :])
print(df.loc[:"李小美", "數學":"社會"])
print(df.loc["李小美":, "數學":"社會"])
print(df.iloc[3, 4])
# iloc
print(df.iloc[0, [0, 4]])
print(df.iloc[[0, 1], [2, 3]])
print(df.iloc[0:3, 2:5])
print(df.iloc[2, :])
print(df.iloc[:2, 2:5])
print(df.iloc[1:, 2:5])
# head() tail()
print(df.head(2))
print(df.tail(2))

print("------------------------------------------------------------")  # 60個

# ch14\df7.py

import pandas as pd
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)
# 排序
print(df.sort_values(by="數學", ascending=False))
print(df.sort_index(axis=0))
# 修改
df.loc["王小明"]["數學"] = 90
print(df)
df.loc["王小明", :] = 80
print(df)
# 刪除
df1 = df.drop("王小明")
print(df1)
df1 = df.drop("數學", axis=1)
print(df1)
df1 = df.drop(["數學", "自然"], axis=1)
print(df1)
df1 = df.drop(df.index[1:4])
print(df1)
df1 = df.drop(df.columns[1:4], axis=1)
print(df1)

print("------------------------------------------------------------")  # 60個

# ch14\np1.py

import numpy as np
np1 = np.array([1,2,3,4])	#使用list
np2 = np.array((5,6,7,8))	#使用tuple
print(np1)
print(np2)
print(type(np1), type(np2))

print("------------------------------------------------------------")  # 60個

# ch14\np10.py

import numpy as np
na = np.arange(0,6)
print(na)           #[0 1 2 3 4 5]
print(na[0])        #0
print(na[5])        #5
print(na[1:5])      #[1 2 3 4]
print(na[1:5:2])    #[1 3]
print(na[5:1:-1])   #[5 4 3 2]
print(na[:])        #[0 1 2 3 4 5]
print(na[:3])       #[0 1 2]
print(na[3:])       #[3 4 5]

print("------------------------------------------------------------")  # 60個

# ch14\np11.py

import numpy as np
na = np.arange(1, 17).reshape(4, 4)
print(na[2, 3])			#12
print(na[1, 1:3])		#[6,7]
print(na[1:3, 2])		#[7,11]
print(na[1:3, 1:3])		#[[6,7],[7,11]]
print(na[::2, ::2])		#[[1,3],[9,11]]
print(na[:, 2])			#[3,7,11,15]
print(na[1, :])			#[5,6,7,8]
print(na[:, :])			#矩陣全部

print("------------------------------------------------------------")  # 60個

# ch14\np12.py

import numpy as np
print('1.產生2x3 0~1之間的隨機浮點數\n',
      np.random.rand(2,3))
print('2.產生2x3常態分佈的隨機浮點數\n',
      np.random.randn(2,3))
print('3.產生0~4(不含5)隨機整數\n',
      np.random.randint(5))
print('4.產生2~4(不含5)5個隨機整數\n',
      np.random.randint(2,5,[5]))
print('5.產生3個 0~1之間的隨機浮點數\n',
      np.random.random(3),'\n',
      np.random.random_sample(3),'\n',
      np.random.sample(3))
print('6.產生0~4(不含5)2x3的隨機整數\n',
      np.random.choice(5,[2,3]))
print('7.產生0~42(不含43)6個不重複的隨機整數\n',
      np.random.choice(43,6,replace=False))

print("------------------------------------------------------------")  # 60個

# ch14\np13.py

import numpy as np
a = np.genfromtxt('scores.csv', delimiter=',', skip_header=1)
print(a.shape)

print("------------------------------------------------------------")  # 60個

# ch14\np14.py

import numpy as np
a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
print('a 陣列內容：\n', a)
print('b 陣列內容：\n', b)
print('a 陣列元素都加值：\n', a + 1)
print('a 陣列元素都平方：\n', a ** 2)
print('a 陣列元素加判斷：\n', a < 5)
print('a 陣列取出第一個row都加1：\n', a[0,:] + 1)
print('a 陣列取出第一個col都加1：\n', a[:,0] + 1)
print('a b 陣列對應元素相加：\n', a + b)
print('a b 陣列對應元素相乘：\n', a * b)
print('a b 陣列點積計算：\n', np.dot(a,b))

print("------------------------------------------------------------")  # 60個

# ch14\np15.py

import numpy as np
a = np.arange(1,10).reshape(3,3)
print('陣列的內容：\n', a)
print('1.最小值與最大值：\n',
      np.min(a), np.max(a))
print('2.每一直行最小值與最大值：\n',
      np.min(a, axis=0), np.max(a, axis=0))
print('3.每一橫列最小值與最大值：\n',
      np.min(a, axis=1), np.max(a, axis=1))
print('4.加總、乘積及平均值：\n',
      np.sum(a), np.prod(a), np.mean(a))
print('5.每一直行加總、乘積與平均值：\n',
      np.sum(a, axis=0), np.prod(a, axis=0), np.mean(a, axis=0))
print('6.每一橫列加總、乘積與平均值：\n',
      np.sum(a, axis=1), np.prod(a, axis=1), np.mean(a, axis=1))

print("------------------------------------------------------------")  # 60個

# ch14\np15_.py

import numpy as np
na = np.genfromtxt('scores.csv', delimiter=',', skip_header=1)
print('國文最高分數：', na[:,1].max())
print('英文最低分數：', na[:,2].min())
print('數學平均分數：', na[:,3].mean())
total1 = na[:,1] + na[:,2] + na[:,3]
print(total1)
print('全班最高總分：',total1.max())

total2 = na[:,1:4].sum(axis=1)
print(total2)
print('全班最高總分：',total2.max())

print("------------------------------------------------------------")  # 60個

# ch14\np16.py

import numpy as np
a = np.random.randint(100,size=50)
print('陣列的內容：', a)
print('1.標準差：', np.std(a))
print('2.變異數：', np.var(a))
print('3.中位數：', np.median(a))
print('4.百分比值：', np.percentile(a, 80))
print('5.最大最小差值：', np.ptp(a))

print("------------------------------------------------------------")  # 60個

# ch14\np17.py

import numpy as np
a = np.random.choice(50, size=10, replace=False)
print('排序前的陣列：', a)
print('排序後的陣列：', np.sort(a))
print('排序後的索引：', np.argsort(a))
#用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=',')

print("------------------------------------------------------------")  # 60個

# ch14\np18.py

import numpy as np
a = np.random.randint(0,10,(3,5))
print('原陣列內容：')
print(a)
print('將每一直行進行排序：')
print(np.sort(a, axis=0))
print('將每一橫列進行排序：')
print(np.sort(a, axis=1))

print("------------------------------------------------------------")  # 60個

# ch14\np2.py

import numpy as np
na = np.array([1,2,3,4], dtype=int)
print(na)
na = np.array([1,2,3,4], dtype=float)
print(na)

print("------------------------------------------------------------")  # 60個

# ch14\np3.py

import numpy as np
na = np.arange(0, 31, 2)
print(na)

print("------------------------------------------------------------")  # 60個

# ch14\np4.py

import numpy as np
na = np.linspace(1, 15, 3)
print(na)

print("------------------------------------------------------------")  # 60個

# ch14\np5.py

import numpy as np
a = np.zeros((5,))
print(a)

print("------------------------------------------------------------")  # 60個

# ch14\np6.py

import numpy as np
b = np.ones((5,))
print(b)

print("------------------------------------------------------------")  # 60個

# ch14\np7.py

import numpy as np

np1 = np.array([[[1,2,3,4],[5,6,7,8]],
                [[9,10,11,12],[13,14,15,16]],
                [[17,18,19,20],[21,22,23,24]],
               ])

print(np1.shape)

print("------------------------------------------------------------")  # 60個

# ch14\np8.py

import numpy as np
listdata = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]]
na = np.array(listdata)
print(na)
print('維度', na.ndim)
print('形狀', na.shape)
print('數量', na.size)

print("------------------------------------------------------------")  # 60個

# ch14\np9.py

import numpy as np
adata = np.arange(1,17)
print(adata)
bdata = adata.reshape(4,4)
print(bdata)

print("------------------------------------------------------------")  # 60個

# ch14\pd1.py

import pandas as pd
df = pd.Series(['a','b','c','d','e'])
print(se[1:3])

print("------------------------------------------------------------")  # 60個

# ch14\plot1.py

import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "mingliu"

plt.rcParams["axes.unicode_minus"] = False 

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])
g1 = df.plot(kind='bar', title='長條圖', figsize=[10,5])
g2 = df.plot(kind='barh', title='橫條圖', figsize=[10,5])
g3 = df.plot(kind='bar', stacked=True, title='堆疊圖', figsize=[10,5])

print("------------------------------------------------------------")  # 60個

# ch14\plot2.py

import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "mingliu"
plt.rcParams["axes.unicode_minus"] = False 

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])
g1 = df.iloc[0].plot(kind='line', legend=True, xticks=range(2015,2020), title='公司分區年度銷售表', figsize=[10,5])
g1 = df.iloc[1].plot(kind='line', legend=True, xticks=range(2015,2020))
g1 = df.iloc[2].plot(kind='line', legend=True, xticks=range(2015,2020))

print("------------------------------------------------------------")  # 60個

# ch14\plot3.py

import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "mingliu"
plt.rcParams["axes.unicode_minus"] = False 

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])
df.plot(kind='pie', subplots=True, figsize=[20,20])

print("------------------------------------------------------------")  # 60個

# ch14\read_cvs.py

import pandas as pd
data = pd.read_csv("scores2.csv", header=0, index_col=0)
print(data)
print(type(data))

print("------------------------------------------------------------")  # 60個

# ch14\read_html.py

import pandas as pd
url = 'https://www.tiobe.com/tiobe-index/'
tables = pd.read_html(url, header=0, keep_default_na=False)
print(tables[0])

print("------------------------------------------------------------")  # 60個

# ch14\se1.py

import pandas as pd
se = pd.Series([1,2,3,4,5])
print(se)           #顯示Series
print(se.values)    #顯示值
print(se.index)     #顯示索引

print("------------------------------------------------------------")  # 60個

# ch14\se2.py

import pandas as pd
se = pd.Series([1,2,3,4,5])
print(se[2])
print(se[2:5])

print("------------------------------------------------------------")  # 60個

# ch14\se3.py

import pandas as pd
se = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(se)
print(se['b'])
print(se['c':'d'])

print("------------------------------------------------------------")  # 60個

# ch14\se4.py

import pandas as pd
dict1 = {'Taipei': '台北', 'Taichung': '台中', 'Kaohsiung': '高雄'}
se = pd.Series(dict1)
print(se)           #顯示Series
print(se.values)    #顯示值
print(se.index)     #顯示索引
print(se['Taipei']) #用索引取值
print(se['Taichung':'Kaohsiung'])

print("------------------------------------------------------------")  # 60個

# ch14\to_cvs.py

import pandas as pd
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)
df.to_csv('scores3.csv', encoding='utf-8-sig')

print("------------------------------------------------------------")  # 60個

# ch15\create_data.py

import pandas as pd
import numpy as np

def c_item(x):
  if x<2: return '筆電'
  elif x<7: return '冰箱'
  else: return '電視'

def s_item(x):
  if x<5: return '張三安'
  elif x<7: return '李四友'
  else: return '王五信'

df = pd.DataFrame({'業務員':np.random.randint(0,10,size = 100),
          '商品':np.random.randint(0,10,size = 100),
          '數量':np.random.randint(30,300,size = 100),
          '價格':np.random.randint(100,200,size = 100)})
df['商品'] = df['商品'].map(c_item)
df['業務員'] = df['業務員'].map(s_item)
df['價格'] = df['價格'].map(lambda x: x*100)

df.to_csv('sale.csv', index=False)

print("------------------------------------------------------------")  # 60個

# ch15\create_score.py

import pandas as pd
import numpy as np

tem = []
for i in range(3): tem.append(i+1)
df = pd.DataFrame(np.random.randint(40,101,size=(3,3)), columns=['英文','社會','公民'])
#df = pd.DataFrame(np.random.randint(40,101,size=(3,4)), columns=['國文','數學','自然','社會'])
df.insert(0, '座號', tem)
df.to_csv('score2_6.csv', index=False)

print("------------------------------------------------------------")  # 60個

# ch15\split_data.py

import pandas as pd
import numpy as np

df1 = pd.read_csv('titanic.csv')
df2 = df1[['row.names','pclass','survived','name','age','embarked']]
df2.to_csv('titanic1.csv', index=False)
df3 = df1[['row.names','home.dest','room','ticket','boat','sex']]
df3.to_csv('titanic2.csv', index=False)

print("------------------------------------------------------------")  # 60個

# ch16\get1.py

from flask import Flask
from flask import request
app = Flask(__name__)

from flask import render_template
@app.route('/get1', methods=['GET'])
def get1():
    name = request.args.get('name')
    city = request.args.get('city')
    return render_template('get1.html', **locals())

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\hello.py

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return '歡迎來到 Flask!'

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\hello2.py

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return '{}，歡迎來到 Flask!'.format(name)

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\index.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '這是本網站首頁!'

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\post1.py

from flask import Flask
from flask import request
app = Flask(__name__)

from flask import render_template
@app.route('/post1')
def post1():
    return render_template('post1.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.values['username']
    password = request.values['password']
    if username=='david' and password=='1234':
        return '歡迎光臨本網站！'
    else:
        return '帳號或密碼錯誤！'

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\show.py

from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/show')
def show():
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    return render_template('show.html', **locals())

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\template1.py

from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\template2.py

from flask import Flask
app = Flask(__name__)

from flask import render_template
from datetime import datetime
@app.route('/hello/<string:name>')
def hello(name):
    now = datetime.now()
    return render_template('hello2.html', **locals())

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\template3.py

from flask import Flask
app = Flask(__name__)

from flask import render_template
from datetime import datetime
@app.route('/hello/<string:name>')
def hello(name):
    now = datetime.now()
    return render_template('hello3.html', **locals())

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\test.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '這是本網站首頁!'

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch16\variable.py

from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/variable')
def variable():
    student = {'學號':'874523', '姓名':'張三', '性別':'男'}
    fruit = ['蘋果', '香蕉', '芭樂', '百香果']
    return render_template('variable.html', **locals())

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個

# ch18\linebotTest.py

from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('5P6YQbws0M1vMwSq5r0cpGZe1VBJCZX2cT65ywd+6hvsrjXI6gi3Je64Hau6kmTd+AEQL2AGNk3G7nm8Fjw1L/wL9qIDepSTuMV+2OysJRK0hZQRwykaOIeCAgKsdaytNDLWaDVyfVzjsKeQ8HBiMAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e03713c489707ceac29953031dde79a0')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()

print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

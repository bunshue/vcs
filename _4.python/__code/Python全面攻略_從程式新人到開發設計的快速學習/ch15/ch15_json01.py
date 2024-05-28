#json01.py

import json

print("------------------------------------------------------------")  # 60個

dictMeal={"編號":"A", "品名":"雙人分享餐", "單價":120}
jsonStr=json.dumps(dictMeal, ensure_ascii=False, indent=4)
print(jsonStr)

print("------------------------------------------------------------")  # 60個

# json02.py

jsonStr='{"編號":"A", "品名":"雙人分享餐", "單價":120}'

dictMeal=json.loads(jsonStr)

print("編號：%s"%(dictMeal["編號"]))
print("品名：%s"%(dictMeal["品名"]))
print("單價：%d"%(dictMeal["單價"]))


print("------------------------------------------------------------")  # 60個

# json03.py

jsonStr='''
    [    
        {"編號": "A","品名": "雙人分享餐","單價": 120},
        {"編號": "B","品名": "歡樂全家餐","單價": 399},
        {"編號": "C","品名": "情人精緻餐","單價": 540}
    ]
'''

listMeal=json.loads(jsonStr)

for meal in listMeal:
    print("編號：%s"%(meal["編號"]))
    print("品名：%s"%(meal["品名"]))
    print("單價：%d"%(meal["單價"]))
    print("="*20) 
'''
for meal in listMeal:
    for key in meal:
        print("%s：%s" %(key, meal[key]))
    print("="*20)
'''

print("------------------------------------------------------------")  # 60個

# json04.py

listMeal=[{"編號":"A", "品名":"雙人分享餐", "單價":120},
          {"編號":"B", "品名":"歡樂全家餐", "單價":399},
          {"編號":"C", "品名":"情人精緻餐", "單價":540}]

f=open("meal.json","w",encoding="utf_8")

json.dump(listMeal, f,  ensure_ascii=False, indent=4)
f.close()
print("JSON餐點記錄建置完成")

print("------------------------------------------------------------")  # 60個

# json05.py

f=open("meal.json", "r", encoding="utf_8")
listMeal = json.load(f)
f.close()

for meal in listMeal:
    for key in meal:
        print("%s：%s" %(key, meal[key]))
    print("折扣：%.2f" %(float(meal[key])*0.9))
    print("="*20)

print("------------------------------------------------------------")  # 60個

# json06.py

import os
import matplotlib.pyplot as plt  	# 引用圖表使用套件
# 讀取109年9月臺中市10大易肇事路口.json資料並放入listTrafficEvent串列物件
f=open("109年9月臺中市10大易肇事路口.json", "r",       encoding="utf_8")
listTrafficEvent = json.load(f)
f.close()

# 將 listTrafficEvent 串列中的每筆字典物件印出來
for trafficEvent in listTrafficEvent:
    for key in trafficEvent:
        show=False
        # 若該筆字典的編號(key)有值(value)即印出
        if (trafficEvent['編號']!=""):
            print("%s：%s" %(key, trafficEvent[key]))
            show=True
        else:
            break
    if (show==True):
        print("="*30)
        
total=0.0        # 統計肇事數量
listAllEvent=[]  # listAllEvent用來存放車禍主要肇因
for trafficEvent in listTrafficEvent:
    if (trafficEvent['編號']!=""):
        listAllEvent+=[trafficEvent['主要肇因']]
        total+=1
            
listEvent=[]   		#存放所有車禍主要肇因，此串列存放不重複的車禍主要肇因
listCount=[]  		#存放各主要肇因對應的車禍數量
for event in set(listAllEvent):   # 使用set()移除listAllEvent串列中重複的主要肇因
   print('主要肇因 %s 共 %s 件' %(event,listAllEvent.count(event)))
   listEvent+=[event]
   listCount+=[listAllEvent.count(event)]   

# 計算各車禍主要肇因的百分比，並放入listPercent串列
listPercent=[] 
for c in listCount:
    listPercent.append(round((float(c)/total)*100))
    
# 繪製車禍主要肇因的圓餅圖
font={"family":"DFKai-SB"}
plt.rc("font", **font)
plt.pie(listPercent, labels=listEvent, autopct="%3.1f%%")
plt.savefig('event.png', dpi=300) 	# 將圓餅圖出成圖片，檔名為event.png 
plt.show()                 	        # 顯示圓餅圖
os.system('event.png')  	        # 開啟圓餅圖event.png圖片
print("圖表建置成成功")

print("------------------------------------------------------------")  # 60個


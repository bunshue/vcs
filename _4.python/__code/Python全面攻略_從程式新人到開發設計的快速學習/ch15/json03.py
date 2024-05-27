import json
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

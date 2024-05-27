import json
f=open("meal.json", "r", encoding="utf_8")
listMeal = json.load(f)
f.close()

for meal in listMeal:
    for key in meal:
        print("%s：%s" %(key, meal[key]))
    print("折扣：%.2f" %(float(meal[key])*0.9))
    print("="*20)
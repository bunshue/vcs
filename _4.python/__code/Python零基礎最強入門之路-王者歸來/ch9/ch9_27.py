# ch9_27.py
survey_dict = {}                        # 建立市場調查空字典
market_survey = True                    # 設定迴圈布林值     

# 讀取參加市場調查者姓名和夢幻旅遊景點
while market_survey:
    name = input("\n請輸入姓名  : ")
    travel_location = input("夢幻旅遊景點: ")

# 將輸入存入survey_dict字典
    survey_dict[name] = travel_location

# 可由此決定是否離開市場調查
    repeat = input("是否有人要參加市場調查?(y/n) ")
    if repeat != 'y':               # 不是輸入y,則離開while迴圈
        market_survey = False

# 市場調查結束
print("\n\n以下是市場調查的結果")
for user, location in survey_dict.items( ):
    print(user, "夢幻旅遊景點: ", location)



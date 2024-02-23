# 定義HelloByName()函式，可接收name和gender參數
def HelloByName(name, gender) :
    if (gender ) :
        str = "先生"
    else :
        str = "小姐"
    print("Hello!大家好, 我是" , name , str)

HelloByName("王小明", True)  # 呼叫Hello()函式並傳入 "王小明" 和 True 參數
HelloByName("李小華", False)  # 呼叫Hello()函式並傳入 "李小華" 和 False 參數



try:
    "1" + 2
except SyntaxError:
    print("SyntaxError - 語法錯誤")
except TypeError:
    print("TypeError - 型態錯誤")
except NameError:
    print("NameError - 該變數未宣告")
except IndexError:
    print("IndexError - 指定索引位置錯誤")
else:
    print("無發生任何異常")
finally:
    print("finally - 不管有沒發生異常都會執行")

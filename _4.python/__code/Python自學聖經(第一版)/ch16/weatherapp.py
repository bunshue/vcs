from tkinter import *
import requests

def showWeather(event):  #下拉選單選取選項後執行的程式
    city = cbVar.get()  #使用者選取的選項
    if city != '請選擇：':  #選擇縣市
        report = requests.get('https://weathflask.herokuapp.com/weather/' + city).text  #取得Web API資料
        jsondata = eval(report)  #轉換為字典
        showdata = city + ' 天氣資料：\n'
        showdata += '天氣狀況：' + jsondata['天氣狀況'] + '\n'
        showdata += '最高溫：' + jsondata['最高溫'] + '\n'
        showdata += '最低溫：' + jsondata['最低溫'] + '\n'
        showdata += '舒適度：' + jsondata['舒適度'] + '\n'
        showdata += '降雨機率：' + jsondata['降雨機率'] + '\n'
        labelVar.set(showdata)
    else:
        labelVar.set('請選擇縣市！')

win = Tk()
win.title('縣市天氣資料')
win.geometry('300x350')

cbVar = StringVar()
cb = Combobox(win, textvariable=cbVar)  #下拉選單元件
cb['value'] = ("請選擇：","臺北","新北","桃園","臺中","臺南","高雄","基隆","新竹","嘉義","苗栗","彰化","南投","雲林","嘉義","屏東","宜蘭","花蓮","臺東","澎湖","金門","連江" )  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', showWeather)  #設定選取選項後執行的程式
cb.place(x=70, y=15)

labelVar = StringVar()  
labelShow = Label(win, foreground='red', justify='left', textvariable=labelVar)  #標籤元件
labelVar.set('尚未選擇縣市！')
labelShow.place(x=80, y=220)

win.mainloop()



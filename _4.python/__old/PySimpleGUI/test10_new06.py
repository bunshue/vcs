import PySimpleGUI as sg

title = "顯示所有資料"
infolder = "."
label1, value1 = "副檔名", "*.txt"

def confirm_data(value):
    msg = value + "先生／小姐、你好。"
    window["text1"].update(msg)

def execute1():
    msg = "你按了 執行1 按鈕"
    window["text1"].update(msg)

def execute2():
    msg = "你按了 執行2 按鈕"
    window["text1"].update(msg)

def execute3():
    msg = "你按了 執行3 按鈕"
    window["text1"].update(msg)

#應用程式的介面
layout = [[sg.Text("你的名字是？"), sg.Input("您的姓名", key="input1")],
          [sg.Button("確認")],
          [sg.Text(key="text1")],
          [sg.Text("你的名字是？")],
          [sg.Input()],
          [sg.Button("確認")],
          [sg.Text("第1列-1"), sg.Text("第1列-2")],
          [sg.Text("第2列-1"), sg.Input("第2列-2")],
          [sg.Button("第3列")],
          [sg.Text("要載入的資料夾", size=(14,1)),
           sg.Input(infolder, key="infolder"),sg.FolderBrowse("選取資料夾")],
          [sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
          [sg.Text("選取檔案", size=(12,1)),
           sg.Input(".", key="infile"),
           sg.FileBrowse("選取檔案")],
          [sg.Button("執行1", size=(20,1), pad=(5,15), bind_return_key=True)],
          [sg.Button("執行2", size=(20,1), pad=(5,15), bind_return_key=True)],
          [sg.Button("執行3", size=(20,1), pad=(5,15), bind_return_key=True)],
          [sg.Multiline(key="text1", size=(60,10))]]

#執行應用程式的處理
window = sg.Window(title, layout, font=(None,14))

while True:
    event, values = window.read()
    if event == None:
        break
    if event == "執行1":
      execute1()
    if event == "執行2":
      execute2()
    if event == "執行3":
      execute3()
    if event == "確認":
      confirm_data(values["input1"])

window.close()



"""
py        vcs    
Text      Label
Input     單行TextBox
Multiline 多行TextBox

"""


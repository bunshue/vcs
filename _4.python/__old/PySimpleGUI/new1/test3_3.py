import PySimpleGUI as sg

def execute():
    msg = "按下按鈕了。"
    window["text1"].update(msg)

title = "test3"
layout = [[sg.Text("你好。", key="text1")],
          [sg.Button("執行")]]

window = sg.Window(title, layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == "執行":
      execute()
window.close()

import PySimpleGUI as sg

def execute(value):
    msg = value + "先生／小姐、你好。"
    window["text1"].update(msg)

title = "test4"
layout = [[sg.Text("你的名字是？"), sg.Input("您的姓名", key="input1")],
          [sg.Button("執行")],
          [sg.Text(key="text1")]]

window = sg.Window(title, layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == "執行":
      execute(values["input1"])
window.close()

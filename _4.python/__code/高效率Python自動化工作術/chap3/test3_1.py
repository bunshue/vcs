import PySimpleGUI as sg

layout = [[sg.Text("你的名字是？")],
          [sg.Input()],
          [sg.Button("執行")]]

window = sg.Window("test1", layout)
while True:
    event, values = window.read()
    if event == None:
        break
window.close()

import PySimpleGUI as sg

layout = [[sg.Text("第1列-1"), sg.Text("第1列-2")],
          [sg.Text("第2列-1"), sg.Input("第2列-2")],
          [sg.Button("第3列")]]

window = sg.Window("test2", layout)
while True:
    event, values = window.read()
    if event == None:
        break
window.close()

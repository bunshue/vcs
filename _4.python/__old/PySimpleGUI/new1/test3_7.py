import PySimpleGUI as sg

title = "選取資料夾文字"
layout = [[sg.Text("選取資料夾", size=(12,1)),
           sg.Input(".", key="infolder"),
           sg.FolderBrowse("選取")]]

window = sg.Window(title, layout, font=(None,14))
while True:
    event, values = window.read()
    if event == None:
        break
window.close()
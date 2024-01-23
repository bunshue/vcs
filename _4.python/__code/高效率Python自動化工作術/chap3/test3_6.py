import PySimpleGUI as sg

title = "選取檔案文字"
layout = [[sg.Text("選取檔案", size=(12,1)),
           sg.Input(".", key="infile"),
           sg.FileBrowse("選取")]]

window = sg.Window(title, layout, font=(None,14))
while True:
    event, values = window.read()
    if event == None:
        break
window.close()


import PySimpleGUI as sg

layout = [
    [sg.Text('第一行'), sg.Text('第一行'), sg.Text('第一行')],
    [sg.Button('Y'), sg.Button('N'), sg.Button('Exit')]
]


#window = sg.Window(title = '這是個標題').Layout(layout)
#window = sg.Window(title = '這是個標題', layout = [[]], margins = (100,50)).read()

#button,value = window.Read()

#window = sg.Window(title = '這是個標題', layout)
#window = sg.Window("這是個標題").Layout(layout)
window = sg.Window('這是個標題', layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()



'''
print('button:',button)

print('value:',value)





child_layout=[[sg.Text('第一行')],[sg.Text('第二行')]]

layout=[
[sg.Text('第一行'),sg.Frame('標題',child_layout)]
]


window=sg.Window('這是個標題').Layout(layout)

button,value=window.Read()

print('button:',button)

print('value:',value)

'''



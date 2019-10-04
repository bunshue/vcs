import PySimpleGUI as sg

layout=[
[sg.Text('第一行'), sg.Text('第一行'), sg.Text('第一行')],
[sg.Button('Y'), sg.Button('N')]
]


window=sg.Window('這是個標題').Layout(layout)

button,value=window.Read()



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


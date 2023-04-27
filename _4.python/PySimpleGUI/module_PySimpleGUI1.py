import PySimpleGUI as sg

fnames = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee']

child_layout=[[sg.Text('第一行')],[sg.Text('第二行')]]
layout = [
    [sg.Text('第一欄'), sg.Text('第二欄'), sg.Text('第三欄')],
    [sg.Listbox(values=fnames, change_submits=True, size=(30, 20), key='listbox')],
    [sg.Button('Yes', size=(8, 2)), sg.Button('No', size=(8, 2)), sg.Button('Exit', size=(8, 2))],
    [sg.Text('第一行'),sg.Frame('標題',child_layout)]
]

#window = sg.Window(title = '這是個標題', layout = [[]], margins = (100,50)).read()   #無layout
#window = sg.Window(title = '這是個標題').Layout(layout) #same
#window = sg.Window('這是個標題').Layout(layout) #same
window = sg.Window('這是個標題', layout)

while True:
    event, value = window.read()
    print('event:', event)
    print('value:', value)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()


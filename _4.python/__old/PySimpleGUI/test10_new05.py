import PySimpleGUI as sg

sg.popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')

event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)

import PySimpleGUI as sg

sg.theme('Dark Grey 13')

layout = [[sg.Text('Filename')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()



import PySimpleGUI as sg

G_SIZE = (800,600)          # Size of the Graph in pixels.
sg.theme('DarkPurple1')

graph = sg.Graph(canvas_size=G_SIZE, graph_bottom_left=(0, 0), graph_top_right=G_SIZE, enable_events=True, key='-GRAPH-', pad=(0,0))

layout = [  [sg.Text('Click on the right side of the window to navigate forward, the left side to go backwards')],
            [sg.Text(f'Displaying image: '), sg.Text(k='-FILENAME-')],
            [graph]]

window = sg.Window('Scrolling Image Viewer', layout, margins=(0,0),  use_default_focus=False, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()




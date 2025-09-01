import PySimpleGUI as sg

print("------------------------------------------------------------")  # 60個

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)

print("------------------------------------------------------------")  # 60個

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText(key='-IN-')],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

text_input = values['-IN-']    
sg.popup('You entered', text_input)

print("------------------------------------------------------------")  # 60個

layout = [  [sg.LBox([], size=(100,40), key='-FILESLB-')],
            [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('瀏覽檔案', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # When choice has been made, then fill in the listbox with the choices
    if event == '-IN-':
        window['-FILESLB-'].Update(values['-IN-'].split(';'))
window.close()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import os
from PIL import Image, ImageTk
import io

"""
Simple Image Browser based on PySimpleGUI
--------------------------------------------
There are some improvements compared to the PNG browser of the repository:
1. Paging is cyclic, i.e. automatically wraps around if file index is outside
2. Supports all file types that are valid PIL images
3. Limits the maximum form size to the physical screen
4. When selecting an image from the listbox, subsequent paging uses its index
5. Paging performance improved significantly because of using PIL
Dependecies
------------
Python3
PIL
"""

# Get the folder containin:g the images from the user
folder = sg.popup_get_folder('Image folder to open', default_path='')
if not folder:
    sg.popup_cancel('Cancelling')
    raise SystemExit()

# PIL supported image types
img_types = (".png", ".jpg", "jpeg", ".tiff", ".bmp")

# get list of files in folder
flist0 = os.listdir(folder)

# create sub list of image files (no sub folders, no wrong file types)
fnames = [f for f in flist0 if os.path.isfile(
    os.path.join(folder, f)) and f.lower().endswith(img_types)]

num_files = len(fnames)                # number of images found
if num_files == 0:
    sg.popup('No files in folder')
    raise SystemExit()

del flist0                             # no longer needed

# ------------------------------------------------------------------------------
# use PIL to read data of one image
# ------------------------------------------------------------------------------


def get_img_data(f, maxsize=(1200, 850), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)
# ------------------------------------------------------------------------------


# make these 2 elements outside the layout as we want to "update" them later
# initialize to the first file in the list
filename = os.path.join(folder, fnames[0])  # name of first file in list
image_elem = sg.Image(data=get_img_data(filename, first=True))
filename_display_elem = sg.Text(filename, size=(80, 3))
file_num_display_elem = sg.Text('File 1 of {}'.format(num_files), size=(15, 1))

# define layout, show and read the form
col = [[filename_display_elem],
       [image_elem]]

col_files = [[sg.Listbox(values=fnames, change_submits=True, size=(60, 30), key='listbox')],
             [sg.Button('Next', size=(8, 2)), sg.Button('Prev', size=(8, 2)), file_num_display_elem]]

layout = [[sg.Column(col_files), sg.Column(col)]]

window = sg.Window('Image Browser', layout, return_keyboard_events=True,
                   location=(0, 0), use_default_focus=False)

# loop reading the user input and displaying image, filename
i = 0
while True:
    # read the form
    event, values = window.read()
    print(event, values)
    # perform button and keyboard operations
    if event == sg.WIN_CLOSED:
        break
    elif event in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34'):
        i += 1
        if i >= num_files:
            i -= num_files
        filename = os.path.join(folder, fnames[i])
    elif event in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33'):
        i -= 1
        if i < 0:
            i = num_files + i
        filename = os.path.join(folder, fnames[i])
    elif event == 'listbox':            # something from the listbox
        f = values["listbox"][0]            # selected filename
        filename = os.path.join(folder, f)  # read this file
        i = fnames.index(f)                 # update running index
    else:
        filename = os.path.join(folder, fnames[i])

    # update window with new image
    image_elem.update(data=get_img_data(filename, first=True))
    # update window with filename
    filename_display_elem.update(filename)
    # update page display
    file_num_display_elem.update('File {} of {}'.format(i+1, num_files))

window.close()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()

print("------------------------------------------------------------")  # 60個

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

print("------------------------------------------------------------")  # 60個

sg.popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')

event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)

print("------------------------------------------------------------")  # 60個

sg.theme('Dark Grey 13')

layout = [[sg.Text('Filename')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()

print("------------------------------------------------------------")  # 60個

title = "顯示所有資料"
infolder = "."
label1, value1 = "副檔名", "*.txt"

def confirm_data(value):
    msg = value + "先生／小姐、你好。"
    window["text1"].update(msg)

def execute1():
    msg = "你按了 執行1 按鈕"
    window["text1"].update(msg)

def execute2():
    msg = "你按了 執行2 按鈕"
    window["text1"].update(msg)

def execute3():
    msg = "你按了 執行3 按鈕"
    window["text1"].update(msg)

#應用程式的介面
layout = [[sg.Text("你的名字是？"), sg.Input("您的姓名", key="input1")],
          [sg.Button("確認")],
          [sg.Text(key="text1")],
          [sg.Text("你的名字是？")],
          [sg.Input()],
          [sg.Button("確認")],
          [sg.Text("第1列-1"), sg.Text("第1列-2")],
          [sg.Text("第2列-1"), sg.Input("第2列-2")],
          [sg.Button("第3列")],
          [sg.Text("要載入的資料夾", size=(14,1)),
           sg.Input(infolder, key="infolder"),sg.FolderBrowse("選取資料夾")],
          [sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
          [sg.Text("選取檔案", size=(12,1)),
           sg.Input(".", key="infile"),
           sg.FileBrowse("選取檔案")],
          [sg.Button("執行1", size=(20,1), pad=(5,15), bind_return_key=True)],
          [sg.Button("執行2", size=(20,1), pad=(5,15), bind_return_key=True)],
          [sg.Button("執行3", size=(20,1), pad=(5,15), bind_return_key=True)],
          [sg.Multiline(key="text1", size=(60,10))]]

#執行應用程式的處理
window = sg.Window(title, layout, font=(None,14))

while True:
    event, values = window.read()
    if event == None:
        break
    if event == "執行1":
      execute1()
    if event == "執行2":
      execute2()
    if event == "執行3":
      execute3()
    if event == "確認":
      confirm_data(values["input1"])

window.close()



"""
py        vcs    
Text      Label
Input     單行TextBox
Multiline 多行TextBox

"""


print("------------------------------------------------------------")  # 60個




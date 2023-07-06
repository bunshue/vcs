import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#from matplotlib.backends.backend_tkagg import FigureCanvasAgg
#import matplotlib.backends.tkagg as tkagg
import numpy as np

def set_plot(amp, function):
    global figure_w, figure_h, fig
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(-np.pi * 2, np.pi * 2, 100)
    if function == 'sine':
        y= amp * np.sin(x)
        ax.set_title('sin(x)')
    else:
        y=amp*np.cos(x)
        ax.set_title('cos(x)')
    plt.plot(x / np.pi, y)
    
    #centre bottom and left axes to zero

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    #Format axes - nicer eh!
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))

    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    
amp = 1
function = 'sine'

set_plot(amp, function)

plt.show()


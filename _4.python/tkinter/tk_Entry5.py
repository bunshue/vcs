import tkinter as tk

COLUMN = 10
ROW = 5

# Check if the numbers entered form a valid solution
def validate():
    print('需要全數字')
    '''
    # Get the numbers from the entries
    values = [[eval(x.get()) for x in cells[i]] for i in range(3)]
    print(values)
    for i in range(3):
        for j in range(3):
            print(cells[i][j]) # XXXXX
    '''

def fill_numbers():
    print('需要全數字')
    for i in range(ROW):
        for j in range(COLUMN):
            print('a')
            cells[i][j] = 5


    
window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = "Entry 測試"
window.title(title)

frame = tk.Frame(window) # Hold entries 
frame.pack()

cells = []
for i in range(ROW):
    cells.append([])
    for j in range(COLUMN):
        cells[i].append(tk.StringVar())
        
for i in range(ROW):
    for j in range(COLUMN):
        tk.Entry(frame, width = 6, justify = tk.RIGHT, textvariable = cells[i][j]).grid(row = i, column = j)
        
tk.Button(window, text = "Validate", command = validate).pack()
tk.Button(window, text = "填數字", command = fill_numbers).pack()
        
window.mainloop()




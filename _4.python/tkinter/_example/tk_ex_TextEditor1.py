import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class FileEditor:
    def __init__(self):
        window = tk.Tk()
        '''
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
        '''

        # 設定主視窗標題
        title = 'Simple Text Editor'
        window.title(title)
       
        # Create a menu bar
        menubar = tk.Menu(window)
        window.config(menu = menubar) # Display the menu bar
        
        # create a pulldown menu, and add it to the menu bar
        operationMenu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = operationMenu)
        operationMenu.add_command(label = "Open", command = self.openFile)
        operationMenu.add_command(label = "Save", command = self.saveFile)
        
        # Add a tool bar frame 
        frame0 = tk.Frame(window) # Create and add a frame to window
        frame0.grid(row = 1, column = 1, sticky = tk.W)
        
        # Create images
        opneImage = tk.PhotoImage(file = "../image/open.gif")
        saveImage = tk.PhotoImage(file = "../image/save.gif")
        
        tk.Button(frame0, image = opneImage, command = self.openFile).grid(row = 1, column = 1, sticky = tk.W)
        tk.Button(frame0, image = saveImage, command = self.saveFile).grid(row = 1, column = 2)
        
        frame1 = tk.Frame(window) # Hold editor pane
        frame1.grid(row = 2, column = 1)
        
        scrollbar = tk.Scrollbar(frame1)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.text = tk.Text(frame1, width = 40, height = 20, wrap = tk.WORD, yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)
        
        window.mainloop() # Create an event loop

    def openFile(self): 
        filenameforReading = askopenfilename()
        infile = open(filenameforReading, "r")
        self.text.insert(tk.END, infile.read()) # Read all from the file
        infile.close()  # Close the input file
    
    def saveFile(self):
        filenameforWriting = asksaveasfilename()
        outfile = open(filenameforWriting, "w")
        # Write to the file
        outfile.write(self.text.get(1.0, tk.END)) 
        outfile.close() # Close the output file
    
FileEditor() # Create GUI

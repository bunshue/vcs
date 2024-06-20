from tkinter import * # Import tkinter
   
class FigureCanvas(Canvas):
    def __init__(self, container, figureType, filled = False, 
                 width = 100, height = 100):
        super().__init__(container, 
                         width = width, height = height)
        self.__figureType = figureType
        self.__filled = filled
        self.drawFigure()
      
    def getFigureType(self):
        return self.__figureType 
        
    def getFilled(self):
        return self.__filled 
          
    def setFigureType(self, figureType):
        self.__figureType = figureType
        self.drawFigure()
        
    def setFilled(self, filled):
        self.__filled = filled
        self.drawFigure()
                
    def drawFigure(self):
        if self.__figureType == "line":
            self.line()
        elif self.__figureType == "rectangle":    
            self.rectangle()
        elif self.__figureType == "oval":
            self.oval()
        elif self.__figureType == "arc":    
            self.arc()
        
    def line(self):
        width = int(self["width"])
        height = int(self["height"])
        self.create_line(10, 10, width - 10, height - 10)
        self.create_line(width - 10, 10, 10, height - 10)

    def rectangle(self):
        width = int(self["width"])
        height = int(self["height"])
        if self.__filled:
            self.create_rectangle(10, 10, width - 10, height - 10, 
                              fill = "red")
        else:
            self.create_rectangle(10, 10, width - 10, height - 10)
            
    def oval(self):
        width = int(self["width"])
        height = int(self["height"])
        if self.__filled:
            self.create_oval(10, 10, width - 10, height - 10, 
                             fill = "red")
        else:
            self.create_oval(10, 10, width - 10, height - 10)

    def arc(self):
        width = int(self["width"])
        height = int(self["height"])
        if self.__filled:
            self.create_arc(10, 10, width - 10, height - 10, 
                        start = 0, extent = 145, fill = "red")
        else:
            self.create_arc(10, 10, width - 10, height - 10, 
                        start = 0, extent = 145)

class DisplayFigures:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Display Figures") # Set title
        
        figure1 = FigureCanvas(window, "line", width = 100, height = 100) 
        figure1.grid(row = 1, column = 1)
        figure2 = FigureCanvas(window, "rectangle", False, 100, 100) 
        figure2.grid(row = 1, column = 2)
        figure3 = FigureCanvas(window, "oval", False, 100, 100) 
        figure3.grid(row = 1, column = 3)
        figure4 = FigureCanvas(window, "arc", False, 100, 100) 
        figure4.grid(row = 1, column = 4)
        figure5 = FigureCanvas(window, "rectangle", True, 100, 100) 
        figure5.grid(row = 1, column = 5)
        figure6 = FigureCanvas(window, "oval", True, 100, 100) 
        figure6.grid(row = 1, column = 6)
        figure7 = FigureCanvas(window, "arc", True, 100, 100) 
        figure7.grid(row = 1, column = 7)
        
        window.mainloop() # Create an event loop

DisplayFigures() # Create GUI

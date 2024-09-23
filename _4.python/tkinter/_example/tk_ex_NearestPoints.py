print('找出最相鄰的兩點')

import tkinter as tk
       
RADIUS = 2 # Radius of the point

# Compute the distance between two points (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

def nearestPoints(points):
    # p1 and p2 are the indices in the points list
    p1, p2 = 0, 1  # Initial two points

    shortestDistance = distance(points[p1][0], points[p1][1], 
        points[p2][0], points[p2][1]) # Initialize shortestDistance
    
    # Compute distance for every two points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1], 
                         points[j][0], points[j][1])  # Find distance

            if shortestDistance > d:
                p1, p2 = i, j # Update p1, p2
                shortestDistance = d # New shortestDistance 

    return p1, p2
    
class NearestPointsGUI:
    def __init__(self):
        self.points = [] # Store self.points
        window = tk.Tk() # Create a window
        window.title("Find Nearest Points") # Set title
        
        self.canvas = tk.Canvas(window, width = 400, height = 200)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.addPoint)
        
        window.mainloop() # Create an event loop

    def addPoint(self, event):
        if not self.isTooCloseToOtherPoints(event.x, event.y):
            self.addThisPoint(event.x, event.y)
            
    def addThisPoint(self, x, y):
        # Display this point
        self.canvas.create_oval(x - RADIUS, y - RADIUS,
            x + RADIUS, y + RADIUS)
        # Add this point to self.points list
        self.points.append([x, y]) 
        if len(self.points) > 2:
            p1, p2 = nearestPoints(self.points)
            self.canvas.delete("line") 
            self.canvas.create_line(self.points[p1][0], 
                self.points[p1][1], self.points[p2][0], 
                self.points[p2][1], tags = "line")
        
    def isTooCloseToOtherPoints(self, x, y):
        for i in range(len(self.points)):
            if distance(x, y, 
                self.points[i][0], self.points[i][1]) <= RADIUS + 2:
                return True
        
        return False

NearestPointsGUI() # Create GUI

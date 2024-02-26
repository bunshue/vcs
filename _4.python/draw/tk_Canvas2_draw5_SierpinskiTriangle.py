from tkinter import * # Import tkinter
    
def display():
    canvas.delete("line")
    p1 = [width / 2, 10]
    p2 = [10, height - 10]
    p3 = [width - 10, height - 10]
    displayTriangles(order, p1, p2, p3)

def displayTriangles(order, p1, p2, p3):
    if order == 0: # Base condition
        # Draw a triangle to connect three points
        drawLine(p1, p2)
        drawLine(p2, p3)
        drawLine(p3, p1)
    else:    
        # Get the midpoint of each triangle's edge 
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)

        # Recursively display three triangles
        displayTriangles(order - 1, p1, p12, p31)
        displayTriangles(order - 1, p12, p2, p23)
        displayTriangles(order - 1, p31, p23, p3)

def drawLine(p1, p2):
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags = "line")
    
# Return the midpoint between two points
def midpoint(p1, p2):
    p = 2 * [0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p


window = Tk() # Create a window
window.title("Sierpinski Triangle") # Set a title
    
width = 200
height = 200
canvas = Canvas(window, width = width, height = height)
canvas.pack()

order = 5
display()

window.mainloop()


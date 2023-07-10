import tkinter as tk
from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))
        
# Define a Ball class
class Ball:
    def __init__(self):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2 # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

def add(): # Add a new ball
    ballList.append(Ball())

def animate(): # Move the message
    while True:
        canvas.after(sleepTime) # Sleep 
        canvas.update() # Update canvas
        canvas.delete("ball") 
            
        for ball in ballList:
            redisplayBall(ball)
    
def redisplayBall(ball):
    if ball.x > width or ball.x < 0:
        ball.dx = -ball.dx
            
    if ball.y > height or ball.y < 0:
        ball.dy = -ball.dy
    
    ball.x += ball.dx
    ball.y += ball.dy
    canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius, ball.y + ball.radius, fill = ball.color, tags = "ball")


ballList = [] # Create a list for balls

window = tk.Tk() # Create a window
window.title("Bouncing Balls") # Set a title

width = 350 # Width of the canvas
height = 150 # Width of the canvas
canvas = tk.Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

frame = tk.Frame(window)
frame.pack()
button1 = tk.Button(frame, text = "+", command = add)
button1.pack(side = tk.LEFT)

add()
sleepTime = 100 # Set a sleep time, in msec
animate()

window.mainloop()

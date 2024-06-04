import sys

print("------------------------------------------------------------")  # 60個

'''
#只能用gif
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

import tkinter as tk
    
window = tk.Tk() # Create a root window

photo = tk.PhotoImage(file = filename)
tk.Label(window, text = "Blue", image = photo, bg = "blue").pack(fill = tk.BOTH, expand = 1)

window.mainloop() # Create an event loop

print("------------------------------------------------------------")  # 60個

#DisplayUnicode
import turtle

turtle.write("\u6B22\u8FCE \u03b1 \u03b2 \u03b3")

turtle.done() 


print("------------------------------------------------------------")  # 60個

# Exception
def getArea(radius):
    if radius < 0:
        raise RuntimeError("Negative radius")
    
    return radius * radius * 3.1415

try:
    print(getArea(5))
    print(getArea(-5))
except RuntimeError:
    print("Invalid radius")

print("------------------------------------------------------------")  # 60個


from tkinter import * # Import tkinter
    
window = Tk() # Create a window
window.title("Pack Manager Demo 1") # Set title

Label(window, text = "Blue", bg = "blue").pack()
Label(window, text = "Red", bg = "red").pack(
    fill = BOTH, expand = 1)
Label(window, text = "Green", bg = "green").pack(
    fill = BOTH)

window.mainloop() # Create an event loop

print("------------------------------------------------------------")  # 60個

from tkinter import * # Import tkinter
    
window = Tk() # Create a window
window.title("Place Manager Demo") # Set title

Label(window, text = "Blue", bg = "blue").place(
    x = 20, y = 20)
Label(window, text = "Red", bg = "red").place(
    x = 50, y = 50)
Label(window, text = "Green", bg = "green").place(
    x = 80, y = 80)

window.mainloop() # Create an event loop

print("------------------------------------------------------------")  # 60個

from tkinter import * # Import tkinter
    
window = Tk() # Create a window
window.title("Scroll Text Demo") # Set title

frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = Y)
text = Text(frame1, width = 40, height = 10, wrap = WORD, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

window.mainloop() # Create an event loop

print("------------------------------------------------------------")  # 60個

# Create a deck of cards
deck = [x for x in range(0, 52)]

# Create suits and ranks lists
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
      "10", "Jack", "Queen", "King"]
        
# Shuffle the cards
import random
random.shuffle(deck)

# Display the first four cards
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is", rank, "of", suit)

print("------------------------------------------------------------")  # 60個

from tkinter import *

root = Tk()

Button(root, text = "OK").pack(side = LEFT)
Button(root, text = "Cancel").pack(side = LEFT)
Label(root, text = "Enter your name:").pack(side = LEFT)
Entry(root, text = "Type Name").pack(side = LEFT)
Checkbutton(root, text = "Bold").pack(side = LEFT)
Checkbutton(root, text = "Italic").pack(side = LEFT)
Radiobutton(root, text = "Red").pack(side = LEFT)
Radiobutton(root, text = "Yellow").pack(side = LEFT)

root.mainloop()

print("------------------------------------------------------------")  # 60個

from random import randint 

# Open file for writing data
outfile = open("Numbers.txt", "w")
for i in range(10):
    outfile.write(str(randint(0, 9)) + " ")
outfile.close() # Close the file

# Open file for reading data
infile = open("Numbers.txt", "r")
s = infile.read()
numbers = [eval(x) for x in s.split()]
for number in numbers:
    print(number, end = " ")
infile.close() # Close the file

print()

print("------------------------------------------------------------")  # 60個

import math # import Math module to use the math functions
 
# Test algebraic functions
print("exp(1.0) =", math.exp(1))
print("log(3.78) =", math.log(math.e))
print("log10(10, 10) =", math.log(10, 10))
print("sqrt(4.0) =", math.sqrt(4.0))
 
# Test trigonometric functions
print("sin(PI / 2) =", math.sin(math.pi / 2))
print("cos(PI / 2) =", math.cos(math.pi / 2))
print("tan(PI / 2) =", math.tan(math.pi / 2))
print("degrees(1.57) =", math.degrees(1.57))
print("radians(90) =", math.radians(90))

print("------------------------------------------------------------")  # 60個

# Compute Loan

# Enter yearly interest rate
annualInterestRate = eval(input(
  "Enter annual interest rate, e.g., 8.25: "))
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numberOfYears = eval(input(
  "Enter number of years as an integer, e.g., 5: "))
    
# Enter loan amount
loanAmount = eval(input("Enter loan amount, e.g., 120000.95: "))
    
# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / (1
  - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

# Display results
print("The monthly payment is", int(monthlyPayment * 100) / 100)
print("The total payment is", int(totalPayment * 100) /100)


print("------------------------------------------------------------")  # 60個

# Receive the amount 
amount = eval(input("Enter an amount in double, e.g., 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = int(remainingAmount / 100)
remainingAmount = int(remainingAmount % 100)

# Find the number of quarters in the remaining amount
numberOfQuarters = int(remainingAmount / 25)
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = int(remainingAmount / 10)
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = int(remainingAmount / 5)
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display results
print("Your amount", amount, "consists of\n", 
    "\t", numberOfOneDollars, "dollars\n", 
    "\t", numberOfQuarters, "quarters\n",
    "\t", numberOfDimes,  "dimes\n",
    "\t", numberOfNickels, "nickels\n",
    "\t", numberOfPennies, "pennies")


print("------------------------------------------------------------")  # 60個

#data analysis

NUMBER_OF_ELEMENTS = 5 # For simplicity, use 5 instead of 100
numbers = [] # Create an empty list
sum = 0

for i in range(NUMBER_OF_ELEMENTS): 
    value = eval(input("Enter a new number: "))
    numbers.append(value)
    sum += value
    
average = sum / NUMBER_OF_ELEMENTS

count = 0 # The number of elements above average
for i in range(NUMBER_OF_ELEMENTS): 
    if numbers[i] > average:
        count += 1

print("Average is", average)
print("Number of elements above the average is", count)

print("------------------------------------------------------------")  # 60個

filename = 'tmp_Presidents.txt'

#製作一個檔案 
# Open file for output
outfile = open(filename, "w")

# Write data to the file
outfile.write("Bill Clinton\n")
outfile.write("George Bush\n")
outfile.write("Barack Obama")

outfile.close() # Close the output file

print("------------------------------------------------------------")  # 60個

filename = 'tmp_Presidents.txt'

fp = open(filename, "r")
zops = fp.readlines()
fp.close()

i=1
print("檔案內容")
for zen in zops:
    print("第 {} 行 : {}".format(i, zen), end="")
    i += 1

print()

print("------------------------------------------------------------")  # 60個

filename = 'tmp_Presidents.txt'

def main():
    # Open file for input
    infile = open(filename, "r")
    print("(1) Using read(): ")
    print(infile.read())
    infile.close() # Close the input file

    # Open file for input
    infile = open(filename, "r")
    print("\n(2) Using read(number): ")
    s1 = infile.read(4)
    print(s1)
    s2 = infile.read(10)
    print(repr(s2))
    infile.close() # Close the input file

    # Open file for input
    infile = open(filename, "r")
    print("\n(3) Using readline(): ")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    infile.close() # Close the input file

    # Open file for input
    infile = open(filename, "r")
    print("\n(4) Using readlines(): ")
    print(infile.readlines())
    infile.close() # Close the input file

main() # Call the main function

print("------------------------------------------------------------")  # 60個

print('各種讀取檔案的方法')

filename = 'tmp_Presidents.txt'

# Open file for input
infile = open(filename, "r")
print("(1) Using read(): ")
print(infile.read())
infile.close() # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(2) Using read(number): ")
s1 = infile.read(4)
print(s1)
s2 = infile.read(10)
print(repr(s2))
infile.close() # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(3) Using readline(): ")
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()
print(repr(line1))
print(repr(line2))
print(repr(line3))
print(repr(line4))
infile.close() # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(4) Using readlines(): ")
print(infile.readlines())
infile.close() # Close the input file

print('------------------------------------------------------------')	#60個

import time

currentTime = time.time() # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

print(totalSeconds)

print('------------------------------------------------------------')	#60個

import tkinter as tk

window = tk.Tk()

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

tkimage = tk.PhotoImage(file = filename)

canvas = tk.Canvas(window, width = 600, height = 600)
canvas.pack()
canvas.create_image(256, 256, image = tkimage)

window.mainloop()

print("------------------------------------------------------------")  # 60個

import urllib.request
input = urllib.request.urlopen('http://www.yahoo.com/index.html')
print(input.read())

print("------------------------------------------------------------")  # 60個

#Social Security Number

import re

regex = "\d{3}-\d{2}-\d{4}"
#ssn = input("Enter SSN: ")
ssn = "123-45-6789"
match1 = re.match(regex, ssn)

if match1 != None:
    print(ssn, " is a valid SSN")
    print("start position of the matched text is " + str(match1.start()))
    print("start and end position of the matched text is " + str(match1.span()))
else:
    print(ssn, " is not a valid SSN")
    

print("------------------------------------------------------------")  # 60個

import re

regex = "\d{3}-\d{2}-\d{4}"
text = input("Enter a text: ")
match1 = re.search(regex, text)

if match1 != None:
    print(text, " contains a SSN")
    print("start position of the matched text is " + 
        str(match1.start()))
    print("start and end position of the matched text is " +
        str(match1.span()))
else:
    print(text, " does not contain a SSN")

print("------------------------------------------------------------")  # 60個

s = "1 2 3 4 5"
items = s.split() # Extract items from the string
lst = [eval(x) for x in items] # Convert items to numbers

print(lst)

print("------------------------------------------------------------")  # 60個

from turtle import *
color('green', 'red')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done() 
'''
print("------------------------------------------------------------")  # 60個

students = [("John", "Smith", 96), ("Susan", "King", 76), 
            ("Kim", "Yao", 99)]
students.sort(key=lambda e: (e[1]))

print(students)
print(sorted(students, key = lambda t: (t[2]), reverse = True))

print("------------------------------------------------------------")  # 60個

from tkinter import * # Import tkinter
    
class WidgetsDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Widgets Demo") # Set a title
        
        # Add a button, a check button, and a radio button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()      
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", 
            variable = self.v1, command = self.processCheckbutton) 
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red",
                variable = self.v2, value = 1, 
                command = self.processRadiobutton) 
        rbYellow = Radiobutton(frame1, text = "Yellow", 
                bg = "yellow", variable = self.v2, value = 2, 
                command = self.processRadiobutton) 
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)
        
        # Add a button, a check button, and a radio button to frame1
        frame2 = Frame(window) # Create and add a frame to window
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name) 
        btGetName = Button(frame2, text = "Get Name", 
            command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)
        
        # Add a text
        text = Text(window) # Create a text add to the window
        text.pack()
        text.insert(END, 
            "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, 
            "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")
        
        window.mainloop() # Create an event loop

    def processCheckbutton(self):
        print("check button is " 
            + ("checked " if self.v1.get() == 1 else "unchecked"))
        
    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") 
            + " is selected " )
    
    def processButton(self):
        print("Your name is " + self.name.get())

WidgetsDemo() # Create GUI

print("------------------------------------------------------------")  # 60個

from tkinter import * # Import tkinter

def drawABar(x, percent, color, title):
    canvas.create_line(0, height - 10, width, height - 10)
    canvas.create_rectangle(x, (1 - percent) * (height - 30), x + width / 4.3 - 5, height - 10, fill = color)
    canvas.create_text((x + x + width / 4.3 - 5) / 2, (1 - percent) * (height - 30) - 10,
                        text = title)

window = Tk() # Create a window
window.title("Pyramid") # Set a title

width = 400
height = 150
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

x = 10
drawABar(x, 0.4, "red", "Project -- 20%")
  
x += width / 4.3 - 5 + 10  
drawABar(x, 0.1, "blue", "Quizzes -- 10%")

x += width / 4.3 - 5 + 10  
drawABar(x, 0.3, "green", "Midterm -- 30%")

x += width / 4.3 - 5 + 10  
drawABar(x, 0.4, "orange", "Final -- 40%")

window.mainloop() # Create an event loop

print("------------------------------------------------------------")  # 60個

#河內塔

# The function for finding the solution to move n disks
#   from fromTower to toTower with auxTower 
def moveDisks(n, fromTower, toTower, auxTower):
    if n == 1: # Stopping condition
        print("Move disk", n, "from", fromTower, "to", toTower)
    else: 
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        moveDisks(n - 1, auxTower, toTower, fromTower)

print('盤子數 5')
n = 5

# Find the solution recursively
print("The moves are:")
moveDisks(n, 'A', 'B', 'C')

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# Convert a decimal to a hex as a string 
def decimalToHex(decimalValue):
    hex = ""
 
    while decimalValue != 0:
        hexValue = decimalValue % 16 
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
    
    return hex
  
# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

decimalValue = 170

print("The hex number for decimal", decimalValue, "is", decimalToHex(decimalValue))
  


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import sys

print("------------------------------------------------------------")  # 60個

'''
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

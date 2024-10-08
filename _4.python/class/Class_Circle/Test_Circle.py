from Class_Circle import Circle

print("------------------------------------------------------------")  # 60個

# Create a circle with radius 1
circle1 = Circle()
print("The area of the circle of radius", circle1.radius, "is", circle1.getArea())

# Create a circle with radius 25
circle2 = Circle(25)
print("The area of the circle of radius", circle2.radius, "is", circle2.getArea())

# Create a circle with radius 125
circle3 = Circle(125)
print("The area of the circle of radius", circle3.radius, "is", circle3.getArea())

# Modify circle radius
circle2.radius = 100
print("The area of the circle of radius", circle2.radius, "is", circle2.getArea())

print("------------------------------------------------------------")  # 60個

from Class_Circle import Circle 

def main():
    # Create a Circle object with radius 1
    myCircle = Circle()

    # Print areas for radius 1, 2, 3, 4, and 5.
    n = 5
    printAreas(myCircle, n)

    # Display myCircle.radius and times
    print("\nRadius is", myCircle.radius)
    print("n is", n)
  
# Print a table of areas for radius 
def printAreas(c, times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius, "\t\t", c.getArea())
        c.radius = c.radius + 1
        times -= 1

main() # Call the main function

print("------------------------------------------------------------")  # 60個




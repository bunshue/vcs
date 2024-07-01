def getMatrix(): 
    matrix = [] # Create an empty list

    numberOfRows = 3
    numberOfColumns = 3
    for row in range(numberOfRows): 
        matrix.append([]) # Add an empty new row 
        for column in range(numberOfColumns): 
            #value = eval(input("Enter a value and press Enter: "))
            value = row + column
            value = 5
            matrix[row].append(value) 

    return matrix

def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)

    return total

m = getMatrix() # Get an list
print(m)

# Display sum of elements
print("\nSum of all elements is", accumulate(m))


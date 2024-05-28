import NearestPoints

print('找出多點中最近的兩點')

# Create a list to store points
points = []
    
point = 2 * [0]
point[0], point[1] = 0, 0
points.append(point)

point = 2 * [0]
point[0], point[1] = 5, 0
points.append(point)

point = 2 * [0]
point[0], point[1] = 5, 5
points.append(point)

point = 2 * [0]
point[0], point[1] = 3, 1
points.append(point)

# p1 and p2 are the indices in the points list
p1, p2 = NearestPoints.nearestPoints(points)  

# Display result
print("The closest two points are (" +
    str(points[p1][0]) + ", " + str(points[p1][1]) + ") and (" +
    str(points[p2][0]) + ", " + str(points[p2][1]) + ")")


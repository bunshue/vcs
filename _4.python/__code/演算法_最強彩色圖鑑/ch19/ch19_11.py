# ch19_11.py
def minCost(costs):
    red, blue, green = 0, 0, 0                  
    for r, b, g in costs:                       
        red,blue,green = r+min(blue,green), b+min(red,green), g+min(red,blue)
    return min(red, blue, green)                
                          
print(minCost([[17, 2, 14], [15, 16, 5], [14, 3, 18]]))












      



    





        






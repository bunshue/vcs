# ch17_14.py
import turtle

t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for line in range(200):            
    t.color(colorsList[line % 8])
    t.forward(line*2)
    t.left(91)
    
 


    


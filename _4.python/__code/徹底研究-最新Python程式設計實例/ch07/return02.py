def func(length,width,height):
    p1 = length*width*height
    p2 = length+width+height
    p3 = (length*width+height*length+width*height)*2
    return p1, p2, p3
 
num1 ,num2, num3 = func(5, 4, 3)
print(num1)  
print(num2)
print(num3)

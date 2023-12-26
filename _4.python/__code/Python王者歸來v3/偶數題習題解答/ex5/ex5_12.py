# ex5_12.py
side1, side2, side3 = eval(input("請輸入3邊長 : "))
if (side1 + side2) > side3:
    if (side1 + side3) > side2:
        if (side2 + side3) > side1:
            print("三角形周長是 : ", (side1 + side2 + side3))
        else:
            print("這不是三角形的邊長")
    else:
        print("這不是三角形的邊長")    
else:
    print("這不是三角形的邊長")





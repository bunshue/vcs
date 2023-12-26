# ch31_26.py
import turtle
# 依據特定階級數繪製Sierpinski三角形
def sierpinski(order, p1, p2, p3):
    if order == 0:      # 階級數為0
        # 將3個點連接繪製成三角形
        drawLine(p1, p2)
        drawLine(p2, p3)
        drawLine(p3, p1)
    else:    
        # 取得三角形各邊長的中點
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)
        # 遞迴呼叫處理繪製三角形
        sierpinski(order - 1, p1, p12, p31)
        sierpinski(order - 1, p12, p2, p23)
        sierpinski(order - 1, p31, p23, p3)   
# 繪製p1和p2之間的線條
def drawLine(p1,p2):
    t.penup()
    t.setpos(p1[0],p1[1])
    t.pendown()
    t.setpos(p2[0],p2[1])
    t.penup()
    t.seth(0)  
# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0,0]                       # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p

# main
t = turtle.Pen()
p1 = [0, 86.6]
p2 = [-100, -86.6]
p3 = [100, -86.6]
order = eval(input("輸入階級數 : "))
sierpinski(order, p1, p2, p3)





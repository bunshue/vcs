#顯示畫圖 03/16/2021
from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()
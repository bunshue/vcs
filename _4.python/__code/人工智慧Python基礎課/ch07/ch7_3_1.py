# 函數: 計算體積
def volume(length, width = 2, height = 3):
    return length * width * height

l, w, h = 10, 5, 15            
print("盒子體積: ", volume(l, w, h)) 
print("盒子體積: ", volume(l, w)) 
print("盒子體積: ", volume(l))




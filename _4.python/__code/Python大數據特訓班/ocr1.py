import cv2,re
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def codeocr(offset):
    global result    
    img = cv2.imread("img_source.png")	#讀取本機圖片
    dst = cv2.fastNlMeansDenoisingColored(img, None, 30, 30, 7, 21) # 去雜點
    ret,thresh = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY_INV)  #黑白
    imgarr = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY) #灰階    
#    plt.imshow(thresh)
#    plt.show()
    
#    print(imgarr.shape)
    height= imgarr.shape[0]  # 高度
    width = imgarr.shape[1]  # 寬度
    
    start = offset   # 要測試後調整，offset 為左右留的邊界
    end = width-offset 
    
    # 去除回歸曲線
    imgarr[:, start:end] = 0  # 從左邊界起至右邊界止，全部挖空
    imagedata = np.where(imgarr == 255) # 找到所有白色的點
    
    plt.scatter(imagedata[1], height - imagedata[0], s = 100, color = "red", label = "Cluster")
    plt.ylim(0, height)
    plt.show() # 顯示起始、結束
    
    ploy_reg = PolynomialFeatures(degree = 2)
    X = np.array([imagedata[1]])
    Y = height-imagedata[0]
    X_ = ploy_reg.fit_transform(X.T)
    regr = LinearRegression()
    regr.fit(X_, Y)
    LinearRegression()
    
    X2 = np.array([[i for i in range(0,width)]])
    X2_ = ploy_reg.fit_transform(X2.T)
    plt.plot(X2.T, regr.predict(X2_), color = "blue", linewidth = 30) #顯示回歸線
    
    grayimg = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY) 
    for ele in np.column_stack([regr.predict(X2_).round(0), X2[0],] ):
        pos = height-int(ele[0])
        try:
            grayimg[pos-3:pos+3, int(ele[1])] = 255 - grayimg[pos - 3:pos + 3, int(ele[1])]
        except IndexError:
            pass
    
    cv2.imwrite("temp.png", grayimg)  #存檔             
    _, inv = cv2.threshold(grayimg, 150, 255, cv2.THRESH_BINARY_INV)  #轉為反相黑白
    for i in range(len(inv)):  #i為每一列
        for j in range(len(inv[i])):  #j為每一行
            if inv[i][j] == 255:  #顏色為白色
                count = 0 
                for k in range(-2, 3):
                    for l in range(-2, 3):
                        try:
                            if inv[i + k][j + l] == 255:  #若是白點就將count加1
                                count += 1
                        except IndexError:
                            pass
                if count <= 6:  #週圍少於等於6個白點
                    inv[i][j] = 0  #將白點去除    
            
    dilation = cv2.dilate(inv, (8,8), iterations=1)  #圖形加粗
    cv2.imwrite("final.png",dilation)
    
    #文字辨識       
    from PIL import Image
    import sys
    import pyocr
    import pyocr.builders
    
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]  #取得可用工具
    
    result = tool.image_to_string(
        Image.open('final.png'),
        builder=pyocr.builders.TextBuilder()
    )
    
# 主程式  
offset=1
results=[]
while offset<20:
    print("\noffset=",offset,end="   ")
    offset+=1
    codeocr(offset)
    result=result.replace(" ","").strip()
    result=re.findall('[a-zA-Z0-9]*',result)[0]
    if len(result)==4:
        results.append(result)
        print("find:",result)
    else:   
        print("no fonud!")
    
print("Results=" , results) 

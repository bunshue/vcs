from PIL import Image
from PIL import ImageStat
import numpy as np
def darkchannel(input_img,h,w):
    dark_img=Image.new("L",(h,w),0)
    for x in range(0,h-1):
        for y in range(0,w-1):
            dark_img.putpixel((x,y),min(input_img.getpixel((x,y))))
    return dark_img
  
def airlight(input_img,h,w):
    nMinDistance=65536    
    w=int(round(w/2))
    h=int(round(h/2))
    if h*w>200:
        lu_box = (0, 0, w, h) 
        ru_box = (w, 0, 2*w, h) 
        lb_box = (0, h, w, 2*h) 
        rb_box = (w, h, 2*h,2*w)  
               
        lu = input_img.crop(lu_box);
        ru = input_img.crop(ru_box);
        lb = input_img.crop(lb_box);
        rb = input_img.crop(rb_box);
        lu_m=ImageStat.Stat(lu)
        ru_m=ImageStat.Stat(ru)
        lb_m=ImageStat.Stat(lb)
        rb_m=ImageStat.Stat(rb)
        lu_mean = lu_m.mean
        ru_mean = ru_m.mean
        lb_mean = lb_m.mean
        rb_mean = rb_m.mean
        lu_stddev = lu_m.stddev
        ru_stddev = ru_m.stddev
        lb_stddev = lb_m.stddev
        rb_stddev = rb_m.stddev 
        score0 = lu_mean[0]+lu_mean[1]+lu_mean[2] - lu_stddev[0]-lu_stddev[1]-lu_stddev[2]
        score1 = ru_mean[0]+ru_mean[1]+lu_mean[2] - ru_stddev[0]-ru_stddev[1]-ru_stddev[2]  
        score2 = lb_mean[0]+lb_mean[1]+lb_mean[2] - lb_stddev[0]-lb_stddev[1]-lb_stddev[2]
        score3 = rb_mean[0]+rb_mean[1]+rb_mean[2] - rb_stddev[0]-rb_stddev[1]-rb_stddev[2]
        x =max(score0,score1,score2,score3)       
        if x == score0:
             air =airlight(lu,h,w)
        if x == score1:
             air =airlight(ru,h,w)
        if x == score2:
             air =airlight(lb,h,w)
        if x == score3:
             air =airlight(rb,h,w)
    else:
        for i in range(0,h-1):
            for j in range(0,w-1):
                temp=input_img.getpixel((i,j))            
                distance = ((255 - temp[0])**2 +  (255 - temp[1])**2 + (255 - temp[2])**2)**0.5
                if nMinDistance > distance:
                    nMinDistance = distance;
                    air = temp
    return air

def transmssion(air,dark_img,h,w,OMIGA):
    trans_map=np.zeros((h,w))
    A=max(air)
    for i in range(0,h-1):
        for j in range(0,w-1):
            temp=1-OMIGA*dark_img.getpixel((i,j))/A
            trans_map[i,j]=max(0.1,temp)  
    for i in range(1,h-1):
        for j in range(1,w-1):
                tempup=(trans_map[i-1][j-1]+2*trans_map[i][j-1]+trans_map[i+1][j-1])
                tempmid=2*(trans_map[i-1][j]+2*trans_map[i][j]+trans_map[i+1][j])
                tempdown=(trans_map[i-1][j+1]+2*trans_map[i][j+1]+trans_map[i+1][j+1])
                trans_map[i,j]=(tempup+tempmid+tempdown)/16
    return trans_map
                   
def defog(img,t_map,air,h,w):
    dehaze_img=Image.new("RGB",(h,w),0)
    for i in range(0,h-1):
        for j in range(0,w-1):
            R,G,B=img.getpixel((i,j))
            R=int((R-air[0])/t_map[i,j]+air[0])
            G=int((G-air[1])/t_map[i,j]+air[1])
            B=int((B-air[2])/t_map[i,j]+air[2])
            dehaze_img.putpixel((i,j),(R,G,B)) 
    return dehaze_img                       
                    
if __name__== '__main__':
    img=Image.open("castle1.jpg")
    [h,w]=img.size
    OMIGA =0.8  
    dark_image=darkchannel(img,h,w)
    air=airlight(img,h,w)
    T_map=transmssion(air,dark_image,h,w,OMIGA)
    fogfree_img=defog(img,T_map,air,h,w)       
    fogfree_img.show()  

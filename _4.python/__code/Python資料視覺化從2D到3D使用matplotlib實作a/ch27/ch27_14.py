# ch27_14.py
import matplotlib.pyplot as plt
import matplotlib.patches as patch
  
fig = plt.figure()
ax = fig.subplots()
# 繪製楔形, wedge1 使用預設顏色
wedge1 = patch.Wedge((1,3),0.6,     # center, r
                     theta1=0,      # 楔形第 1 掃描角
                     theta2=270)    # 楔形第 2 掃描角
    
wedge2 = patch.Wedge((1,1),0.6,     # center, r
                     theta1=90,     # 楔形第 1 掃描角
                     theta2=360,    # 楔形第 2 掃描角
                     color='r')     # 紅色
                
                 
wedge3 = patch.Wedge((3,1),0.6,     # center, r
                     theta1=180,    # 楔形第 1 掃描角
                     theta2=90,     # 楔形第 2 掃描角
                     color='g')     # 藍色

wedge4 = patch.Wedge((3,3),0.6,     # center, r
                     theta1=270,    # 楔形第 1 掃描角
                     theta2=180,    # 楔形第 2 掃描角
                     color='m')     # 品紅色
ax.add_patch(wedge1)
ax.add_patch(wedge2)
ax.add_patch(wedge3)
ax.add_patch(wedge4)
ax.axis([0,4,0,4])  
ax.set_aspect('equal')              #   
plt.show()






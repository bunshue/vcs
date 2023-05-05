# plot 集合

selected_font = 'C:/_git/vcs/_1.data/______test_files1/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

def process_key(event):
    fig = event.canvas.figure
    ax = fig.axes[0]

    if event.key == "p":
        #previous_slice(ax) #上一張
        #draw(ax, False)
        print('你在圖上按了 p')
    elif event.key == "n":
        #next_slice(ax) #下一張
        #draw(ax, False)
        print('你在圖上按了 n')
    elif event.key == "c":
        #change_axis(ax)
        #draw(ax, True)
        print('你在圖上按了 c')

    fig.canvas.draw_idle()


fig, ax = plt.subplots()

#ax.volume = volume
#ax.index = volume.shape[0] // 2
ax.axis = 0
#ax.imshow(volume[ax.index, :, :], cMap, vmin=cMin, vmax=cMax)
fig.canvas.mpl_connect("key_press_event", process_key)



plt.show()





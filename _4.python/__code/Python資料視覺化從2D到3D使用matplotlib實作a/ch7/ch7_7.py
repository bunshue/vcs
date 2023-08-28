# ch7_7.py
import matplotlib.pyplot as plt

def demo(ax, connectionstyle):
    ''' 繪製子圖與箭頭樣式說明 '''
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6
    ax.plot([x1, x2], [y1, y2], "g.")
    ax.annotate("",
                xy=(x1, y1),
                xytext=(x2, y2),
                arrowprops=dict(arrowstyle="->", color="m",
                                shrinkA=5,
                                shrinkB=5,
                                connectionstyle=connectionstyle,
                                ),
                )
    ax.text(0.1, 0.96, connectionstyle.replace(",", ",\n"),
            transform=ax.transAxes, ha="left", va="top", c='b')
# 主程式開始
fig, axs = plt.subplots(3, 5, figsize=(7, 6.2))
demo(axs[0, 0], "angle3,angleA=90,angleB=0")
demo(axs[1, 0], "angle3,angleA=0,angleB=90")
demo(axs[0, 1], "angle,angleA=-90,angleB=180,rad=0")
demo(axs[1, 1], "angle,angleA=-90,angleB=180,rad=5")
demo(axs[2, 1], "angle,angleA=-90,angleB=10,rad=5")
demo(axs[0, 2], "arc3,rad=0.")
demo(axs[1, 2], "arc3,rad=0.3")
demo(axs[2, 2], "arc3,rad=-0.3")
demo(axs[0, 3], "arc,angleA=-90,angleB=0,armA=30,armB=30,rad=0")
demo(axs[1, 3], "arc,angleA=-90,angleB=0,armA=30,armB=30,rad=5")
demo(axs[2, 3], "arc,angleA=-90,angleB=0,armA=0,armB=40,rad=0")
demo(axs[0, 4], "bar,fraction=0.3")
demo(axs[1, 4], "bar,fraction=-0.3")
demo(axs[2, 4], "bar,angle=180,fraction=-0.3")
# 取消刻度標記與標籤
for ax in axs.flat:
    ax.set(xlim=(0, 1), ylim=(0, 1.25), xticks=[], yticks=[])
plt.tight_layout()          # 緊縮佈局
plt.show()





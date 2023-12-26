# ch35_4.py
from moviepy.editor import VideoFileClip, vfx

clip = VideoFileClip("short南極.mp4")
# 將播放速度加快兩倍
faster_clip = clip.fx(vfx.speedx, 2)
# 保存新影片
faster_clip.write_videofile(r"out35_4_faster.mp4")

# 將播放速度減慢到一半
slower_clip = clip.fx(vfx.speedx, 0.5)
# 保存新影片
slower_clip.write_videofile("out35_4_slower.mp4")



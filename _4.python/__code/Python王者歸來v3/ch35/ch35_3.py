# ch35_3.py
from moviepy.editor import VideoFileClip

clip = VideoFileClip("short南極.mp4")
# 調整影片的尺寸為寬度為 480 像素
resized_480 = clip.resize(width=480)
# 保存新影片
resized_480.write_videofile(r"out35_3_resized_480.mp4")

# 或者按照原始尺寸的一半
resized_half = clip.resize(0.5)
# 保存新影片
resized_half.write_videofile("out35_3_resized_half.mp4")

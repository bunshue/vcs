# ch35_5.py
from moviepy.editor import VideoFileClip, vfx

clip = VideoFileClip("short南極.mp4")
# 提高亮度
brighter_clip = clip.fx(vfx.colorx, 1.2)                # 亮度增加 20%
# 保存新影片
brighter_clip.write_videofile("out35_5_brighter.mp4")

# 設定亮度與對比度, 0.5是亮度, 1.5是對比度
contrast_clip = clip.fx(vfx.lum_contrast, 0.5, 1.5, 0)  # 對比度增加 50%
# 保存新影片
contrast_clip.write_videofile("out35_5_contrast.mp4")


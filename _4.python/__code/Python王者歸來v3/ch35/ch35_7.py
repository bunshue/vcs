# ch35_7.py
from moviepy.editor import VideoFileClip

# 載入影片
video_clip = VideoFileClip("short南極企鵝.mp4")

# 將影片的音量放大兩倍
video_clip = video_clip.volumex(2)

# 將調整音量後的影片儲存
video_clip.write_videofile("out35_7_企鵝聲音double.mp4")



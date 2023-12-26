# ch35_10.py
from moviepy.editor import VideoFileClip

# 載入影片
video_clip = VideoFileClip("penguin.mp4")

# 設定淡出效果的持續時間
fade_duration = 2

# 添加淡出效果
video_fadeout = video_clip.fadeout(fade_duration)

# 儲存帶有淡出效果的影片
video_fadeout.write_videofile("out35_10.mp4",codec="libx264",audio_codec="aac")



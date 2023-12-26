# ch35_8.py
from moviepy.editor import VideoFileClip,afx

# 加載影片文件
video = VideoFileClip("short南極企鵝.mp4")

# 設定音訊淡出的時間，單位為秒
fadeout_duration = 3                # 音訊淡出 3 秒

# 應用音訊淡出效果
audio_fadeout = video.audio.fx(afx.audio_fadeout, fadeout_duration)

# 將帶有淡出效果的音訊設置回影片
video = video.set_audio(audio_fadeout)

# 儲存處理後的影片文件
video.write_videofile("out35_8_淡出.mp4",codec="libx264",audio_codec="aac")



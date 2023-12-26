# ch35_9.py
from moviepy.editor import VideoFileClip, AudioFileClip

# 載入影片文件和音訊文件
video_clip = VideoFileClip("short南極.mp4")
audio_clip = AudioFileClip("out35_6_企鵝聲音.mp3")

# 如果音訊比影片長，則截斷音訊以匹配影片的長度
if audio_clip.duration > video_clip.duration:
    audio_clip = audio_clip.subclip(0, video_clip.duration)

# 如果音訊比影片短，則循環音訊以填滿影片的長度
elif audio_clip.duration < video_clip.duration:
    # 計算循環次數
    number_of_loops = video_clip.duration // audio_clip.duration + 1
    audio_clip = audio_clip.loop(number_of_loops)
    audio_clip = audio_clip.subclip(0, video_clip.duration)

# 將新音訊設定到影片文件中
final_clip = video_clip.set_audio(audio_clip)

# 儲存結果到文件
final_clip.write_videofile("out35_9.mp4",codec="libx264",audio_codec="aac")



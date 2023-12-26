# ch35_11.py
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# 載入影片
video_clip = VideoFileClip("short南極.mp4")

# 創建文本剪輯，指定字體
txt_clip = TextClip("您的文本", fontsize=70, color='white', font='Arial')

# 設定文本位置和持續時間
txt_clip = txt_clip.set_position('center').set_duration(2)

# 將文本合成到影片上
final_clip = CompositeVideoClip([video_clip, txt_clip])

# 儲存結果
final_clip.write_videofile("out35_11.mp4", codec="libx264", audio_codec="aac")




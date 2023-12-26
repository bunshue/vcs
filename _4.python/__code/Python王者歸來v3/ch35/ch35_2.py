#ch35_2.py
from moviepy.editor import VideoFileClip
import os

# 確保輸出資料夾存在
output_folder = "out35_2"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 載入原始影片
original_clip = VideoFileClip("南極.mp4")

# 剪輯指定時間範圍（第 2 秒到第 3 秒）
clip = original_clip.subclip(2, 3)

# 轉換並保存為 GIF 格式
output_file = os.path.join(output_folder, "gif_video.gif")
clip.write_gif(output_file)

# 釋放資源
clip.close()
original_clip.close()



# ch35_1.py
from moviepy.editor import VideoFileClip
import os

# 確保輸出資料夾存在
output_folder = "out35_1"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 載入原始影片
original_clip = VideoFileClip("南極.mp4")

# 定義不同的輸出格式
formats = ["avi"]

# 對每個格式進行轉換
for fmt in formats:
    output_file = os.path.join(output_folder, f"output_video.{fmt}")
    original_clip.write_videofile(output_file, codec='libx264')

# 釋放資源
original_clip.close()




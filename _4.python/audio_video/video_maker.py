from moviepy.editor import VideoFileClip
import os

print("------------------------------------------------------------")  # 60個

# 確保輸出資料夾存在
output_folder = "tmp_video_1"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 載入原始影片
original_clip = VideoFileClip("data/南極.mp4")

# 定義不同的輸出格式
formats = ["avi"]

# 對每個格式進行轉換
for fmt in formats:
    output_file = os.path.join(output_folder, f"output_video.{fmt}")
    original_clip.write_videofile(output_file, codec="libx264")

# 釋放資源
original_clip.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip
import os

# 確保輸出資料夾存在
output_folder = "tmp_video_2"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 載入原始影片
original_clip = VideoFileClip("data/南極.mp4")

# 剪輯指定時間範圍（第 2 秒到第 3 秒）
clip = original_clip.subclip(2, 3)

# 轉換並保存為 GIF 格式
output_file = os.path.join(output_folder, "tmp_gif_video.gif")
clip.write_gif(output_file)

# 釋放資源
clip.close()
original_clip.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
from moviepy.editor import VideoFileClip

clip = VideoFileClip("data/short南極.mp4")
# 調整影片的尺寸為寬度為 480 像素
resized_480 = clip.resize(width=480)
# 保存新影片
resized_480.write_videofile(r"tmp_video_3_resized_480.mp4")

# 或者按照原始尺寸的一半
resized_half = clip.resize(0.5)
# 保存新影片
resized_half.write_videofile("tmp_video_3_resized_half.mp4")
"""

print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip, vfx

clip = VideoFileClip("data/short南極.mp4")
# 將播放速度加快兩倍
faster_clip = clip.fx(vfx.speedx, 2)
# 保存新影片
faster_clip.write_videofile(r"tmp_video_4_faster.mp4")

# 將播放速度減慢到一半
slower_clip = clip.fx(vfx.speedx, 0.5)
# 保存新影片
slower_clip.write_videofile("tmp_video_4_slower.mp4")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip, vfx

clip = VideoFileClip("data/short南極.mp4")
# 提高亮度
brighter_clip = clip.fx(vfx.colorx, 1.2)  # 亮度增加 20%
# 保存新影片
brighter_clip.write_videofile("tmp_video_5_brighter.mp4")

# 設定亮度與對比度, 0.5是亮度, 1.5是對比度
contrast_clip = clip.fx(vfx.lum_contrast, 0.5, 1.5, 0)  # 對比度增加 50%
# 保存新影片
contrast_clip.write_videofile("tmp_video_5_contrast.mp4")

print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip

clip = VideoFileClip("data/short南極企鵝.mp4")
audio = clip.audio
audio.write_audiofile("tmp_video_6_企鵝聲音.mp3")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip

# 載入影片
video_clip = VideoFileClip("data/short南極企鵝.mp4")

# 將影片的音量放大兩倍
video_clip = video_clip.volumex(2)

# 將調整音量後的影片儲存
video_clip.write_videofile("tmp_video_7_企鵝聲音double.mp4")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip, afx

# 加載影片文件
video = VideoFileClip("data/short南極企鵝.mp4")

# 設定音訊淡出的時間，單位為秒
fadeout_duration = 3  # 音訊淡出 3 秒

# 應用音訊淡出效果
audio_fadeout = video.audio.fx(afx.audio_fadeout, fadeout_duration)

# 將帶有淡出效果的音訊設置回影片
video = video.set_audio(audio_fadeout)

# 儲存處理後的影片文件
video.write_videofile("tmp_video_8_淡出.mp4", codec="libx264", audio_codec="aac")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip, AudioFileClip

# 載入影片文件和音訊文件
video_clip = VideoFileClip("data/short南極.mp4")
audio_clip = AudioFileClip("tmp_video_6_企鵝聲音.mp3")

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
final_clip.write_videofile("tmp_video_9.mp4", codec="libx264", audio_codec="aac")

print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip

# 載入影片
video_clip = VideoFileClip("data/penguin.mp4")

# 設定淡出效果的持續時間
fade_duration = 2

# 添加淡出效果
video_fadeout = video_clip.fadeout(fade_duration)

# 儲存帶有淡出效果的影片
video_fadeout.write_videofile("tmp_video_10.mp4", codec="libx264", audio_codec="aac")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip
from moviepy.editor import VideoFileClip, vfx
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

if __name__ == "__main__":
    # 用一位老同学写的短诗的中英文作为TextClip显示内容，由于内容过长需要滚动显示
    text = """致敬奋战在一线的巾帼女英雄  

    你也是孩子的妈妈，

    你也是爸妈的孩子。

    但你说只要穿上白大褂，

    我就是一名医护人员，

    这就是我的职责。

    我看不清你的长相，

    在层层的防护服里，

    都是一颗颗金子般的心。

    “青山一道同云雨，明月何曾是两乡”

    引用自王昌龄的《送柴侍御》，

    为在抗击疫情一线的女性“逆行者”致敬。

    中国加油！武汉加油！

    武汉人民感谢所有白衣天使！

    Pay tribute to the heroine fighting in the front line
            Yao Junfeng, Wuhan University
    
    You are also the mother of the child,
    You're also a parent's child.
    But you said just put on the white coat,
    I'm a healthcare worker,
    This is my duty.
    I can't see what you look like,
    In layers of protective clothing,
    Every heart is like gold.
    "The green mountains are the same as the clouds and the rain. How could the bright moon be the two villages?"
    It is quoted from Wang Changling's "See  Mr. Chai Off",

    To pay tribute to the female "reverse" in the front line of fighting the epidemic.

    Go China! Come on, Wuhan!

    Wuhan people thank all angels in white!

    """
    font_filename = "C:/_git/vcs/_1.data/______test_files5/taipei_sans_tc_beta.ttf"

    clip = (
        VideoFileClip("kkkk.mp4", audio=False).crop(0, 300, 540, 840).subclip(0, 0.05)
    )

    txtclip = (
        TextClip(text, fontsize=18, color="blue", bg_color="white", transparent=True)
        .set_duration(30)
        .resize((clip.size[0], clip.size[1] * 2))
        .set_fps(clip.fps)
        .set_start(clip.end)
    )

    w = None
    h = clip.size[1]
    x_speed = x_start = y_start = 0
    y_speed = 20
    txtclip = txtclip.fx(
        vfx.scroll, w, h, x_speed, y_speed, x_start, y_start
    )  # .set_start(clip.end)

    newclip = CompositeVideoClip(
        [txtclip, clip], bg_color=(255, 255, 255), ismask=False
    )
    newclip.write_videofile(r"WinBasedWorkHard_scroll.mp4", threads=8)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# 載入影片
video_clip = VideoFileClip("data/short南極.mp4")

# 創建文本剪輯，指定字體
txt_clip = TextClip("您的文本", fontsize=70, color="white", font="Arial")

# 設定文本位置和持續時間
txt_clip = txt_clip.set_position("center").set_duration(2)

# 將文本合成到影片上
final_clip = CompositeVideoClip([video_clip, txt_clip])

# 儲存結果
final_clip.write_videofile("tmp_video_11.mp4", codec="libx264", audio_codec="aac")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

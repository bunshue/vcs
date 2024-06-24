print("------------------------------------------------------------")  # 60個
print("Python 影片處理")
print("------------------------------------------------------------")  # 60個

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

from moviepy.editor import *

video = VideoFileClip(video_filename)  # 讀取影片

format_list = ["avi", "mov", "wmv", "flv", "asf", "mkv"]  # 要轉換的格式清單

# 使用 for 迴圈轉換成所有格式
for i in format_list:
    output = video.copy()
    output.write_videofile(
        f"tmp_aa_output.{i}",
        temp_audiofile="tmp_temp-audio.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
    )

print("ok")

print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

format_list = ["avi", "mov", "wmv", "flv", "asf", "mkv"]

for n in range(3):
    video = VideoFileClip(f"oxxo_{n}.mp4")  # 使用 for 迴圈讀取影片
    for i in format_list:
        output = video.copy()
        output.write_videofile(
            f"output_{n}.{i}",
            temp_audiofile="tmp_temp-audio1.m4a",
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
        )

print("ok")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

video = AudioSegment.from_file(video_filename)  # 讀取 mp4 檔案
output.export("tmp_video.mp3")  # 講讀取的聲音輸出為 mp3
print("ok")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment

video = AudioSegment.from_file(video_filename)
output = video[2000:10000]  # 剪輯聲音
output = output[:] + 10  # 放大聲音
output.export("tmp_output.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip(video_filename)  # 讀取影片
audio = video.audio  # 取出聲音
audio.write_audiofile("tmp_song.mp3")  # 輸出聲音為 mp3
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip(video_filename)  # 讀取影片
audio = AudioFileClip("tmp_song.mp3")  # 讀取音樂

output = video2.set_audio(audio)  # 合併影片與聲音
output.write_videofile(
    "tmp_output.mp4",
    temp_audiofile="temp-audio2.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 注意要設定相關參數，不然轉出來的影片會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip(video_filename)  # 讀取影片
output = video.subclip(12, 15)  # 剪輯影片 ( 單位秒 )
output.write_videofile(
    "tmp_output_1.mp4",
    temp_audiofile="tmp_temp-audio3.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")  # 開啟第一段影片
o2 = VideoFileClip("oxxo2.mp4")  # 開啟第二段影片
o3 = VideoFileClip("oxxo3.mp4")  # 開啟第三段影片
output = concatenate_videoclips([o1, o2, o3])  # 合併影片
output.write_videofile(
    "output123.mp4",
    temp_audiofile="tmp_temp-audio4.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")

print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")
o1 = o1.resize((1280, 720))  # 改變尺寸
o2 = VideoFileClip("oxxo2.mp4")
o3 = VideoFileClip("oxxo3.mp4")
output = concatenate_videoclips([o1, o2, o3])
output.write_videofile(
    "output456.mp4",
    fps=30,
    temp_audiofile="tmp_temp-audio5.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")
o2 = VideoFileClip("oxxo2.mp4")
o3 = VideoFileClip("oxxo3.mp4")
output = concatenate_videoclips([o1, o2, o3], method="compose")  # 設定 method 為 compose
output.write_videofile(
    "output456.mp4",
    fps=30,
    temp_audiofile="tmp_temp-audio5.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
v3 = VideoFileClip("oxxo3.mp4")  # 讀取影片
v4 = VideoFileClip("oxxo4.mp4")  # 讀取影片
v1 = v1.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v2 = v2.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v3 = v3.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v4 = v4.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
output = clips_array([[v1, v2], [v3, v4]])  # 排列影片，v1 和 v2 一組，v3 和 v4 一組
output.write_videofile(
    "output.mp4",
    temp_audiofile="tmp_temp-audio6.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
output = CompositeVideoClip([v2, v1])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="tmp_temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
v1 = mask_color(v1, color=0, thr=10, s=0)  # 設定 v1 遮罩為半透明
# color=0 表示黑色，thr 和 s 是參數，這種設定為半透明
output = CompositeVideoClip([v2, v1])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip(video_filename)  # 讀取影片
clip_1 = video.subclip(2, 5)  # 裁切出三秒影片
clip_2 = video.subclip(17, 21).set_start(2).crossfadein(1)  # 裁切出四秒影片，設定兩秒後再開始，淡入一秒
clip_3 = video.subclip(50, 53).set_start(5).crossfadein(1)  # 裁切出三秒影片，設定五秒後再開始，淡入一秒

output = CompositeVideoClip([clip_1, clip_2, clip_3])

output.write_videofile(
    "tmp_output222.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

from moviepy.editor import *

video = VideoFileClip(video_filename)  # 讀取影片
output = video.resize((480, 360))  # 改變尺寸
output.write_videofile(
    "tmp_output333.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

from moviepy.editor import *

video = VideoFileClip(video_filename)
output = video.resize(width=480)  # 改變尺寸，設定寬度改變為 480
output.write_videofile(
    "tmp_output444.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip(video_filename)
output_1 = crop(video, x1=10, y1=10, width=50, height=50)  # 方法 1，指定左上 (x1, y1) 座標和寬高
output_2 = crop(
    video, x1=10, y1=10, x2=50, y2=50
)  # 方法 2，指定左上 (x1, y1) 座標和右下 ( x2, y2 )座標
output_3 = crop(video, x1=10, width=100)  # 方法 3，指定左上 x1 座標和寬度，就會自動採用 y1=0 和影片高度

output_1.write_videofile(
    "tmp_output555.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip(video_filename)
output = video.rotate(90)  # 影片旋轉 90 度
output.write_videofile(
    "tmp_output666.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip(video_filename)
output_x = mirror_x(video)  # 左右翻轉
output_y = mirror_y(video)  # 垂直翻轉

output_x.write_videofile(
    "tmp_output_x.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_y.write_videofile(
    "output_y.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip(video_filename)  # 讀取影片
output_1 = speedx(video, factor=2)  # 2 倍速
output_2 = speedx(video, factor=0.5)  # 0.5 倍速
output_3 = speedx(video, final_duration=2)  # 將影片變成 2 秒長

output_1.write_videofile(
    "tmp_output_1777.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip(video_filename)  # 讀取影片
output_1 = time_mirror(video)  # 反轉影片
output_2 = time_symmetrize(video)  # 播到底後反轉影片回頭

output_1.write_videofile(
    "tmp_output_888.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip(video_filename)
output_1 = lum_contrast(video, lum=-50, contrast=0)  # 亮度減少 50
output_2 = lum_contrast(video, lum=150, contrast=0)  # 亮度增加 150
output_3 = lum_contrast(video, lum=0, contrast=-0.5)  # 對比減少 0.5
output_4 = lum_contrast(video, lum=0, contrast=2)  # 對比增加 2

output_1.write_videofile(
    "tmp_output_999.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_4.write_videofile(
    "output_4.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip(video_filename)
output_1 = colorx(video, 1.5)  # 調整顏色
output_2 = gamma_corr(video, 1)  # 調整 gamma 值
output_3 = blackwhite(video)  # 黑白影片
output_4 = invert_colors(video)  # 負片效果

output_1.write_videofile(
    "tmp_output_aaa.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_4.write_videofile(
    "output_4.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip(video_filename)  # 讀取影片
output = video.resize((360, 180))  # 壓縮影片
output = output.subclip(13, 15)  # 取出 13～15 秒的片段
output.write_gif("tmp_output.gif")  # 將這個片段轉換成 gif
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip(video_filename)
output = video.resize((360, 180))
output = output.subclip(13, 15)
output.write_gif("tmp_output_fps24.gif", fps=24)  # 256 色一秒 24 格
output.write_gif("tmp_output_fps8.gif", fps=8)  # 256 色一秒 8 格
output.write_gif("tmp_output_fps8_c2.gif", fps=8, colors=2)  # 2 色一秒 8 格
output.write_gif("tmp_output_fps8_c16.gif", fps=8, colors=16)  # 16 色一秒 8 格
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (360, 180))
font = ImageFont.truetype("NotoSansTC-Regular.otf", 40)
draw = ImageDraw.Draw(img)
draw.text(
    (10, 120),
    "OXXO.STUDIO",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="red",
)
draw.text(
    xy=(50, 0),
    text="大家好\n哈哈",
    align="center",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="blue",
)
img.save("ok.png")

video = VideoFileClip("baby_shark.mp4")  # 讀取影片
clip = video.resize((360, 180)).subclip(10, 12)  # 縮小影片尺寸，剪輯出 10～12 秒的片段
text_clip = ImageClip("ok.png", transparent=True).set_duration(2)  # 讀取圖片，將圖片變成長度兩秒的影片

output = CompositeVideoClip([clip, text_clip])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

img_empty = Image.new("RGBA", (360, 180))  # 產生 RGBA 空圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 24)  # 設定文字字體和大小
video = VideoFileClip(video_filename).resize((360, 180))  # 讀取影片，改變尺寸
output_list = []  # 記錄最後要組合的影片片段


# 建立文字字卡函式
def text_clip(xy, text, name):
    img = img_empty.copy()  # 複製空圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件，並寫入文字
    draw.text(
        xy, text, fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill="black"
    )
    img.save(name)  # 儲存


# 建立影片和文字合併的函式
def text_in_video(t, text_img):
    clip = video.subclip(t[0], t[1])  # 剪輯影片到指定長度
    text = ImageClip(text_img, transparent=True).set_duration(
        t[1] - t[0]
    )  # 讀取字卡，調整為影片長度
    combine_clip = CompositeVideoClip([clip, text])  # 合併影片和文字
    output_list.append(combine_clip)  # 添加到影片片段裡


# 文字串列，包含座標和內容
text_list = [
    [(100, 140), "你到底要怎樣？"],
    [(90, 140), "給我 CDPRO2 呀！"],
    [(60, 140), "但是 CDPRO2 過時啦！"],
]

# 影片串列，包含要切取的時間片段
video_list = [[13, 16], [21, 24], [38, 41]]

# 使用 for 迴圈，產生文字字卡
for i in range(len(text_list)):
    text_clip(text_list[i][0], text_list[i][1], f"text_{i}.png")

# 使用 for 迴圈，合併字卡和影片
for i in range(len(video_list)):
    text_in_video(video_list[i], f"text_{i}.png")

output = concatenate_videoclips(output_list)  # 合併所有影片片段
output.write_gif("tmp_output.gif", fps=6, colors=32)  # 轉換成 gif 動畫
print("ok")


print("------------------------------------------------------------")  # 60個


# 定義轉換為總秒數的函式
def time2sec(t):
    arr = t.split(" --> ")  # 根據「' --> '」拆分文字
    s1 = arr[0].split(",")  # 前方的文字為開始時間
    s2 = arr[1].split(",")  # 後方的文字為結束時間
    # 計算開始時間的總秒數
    start = (
        int(s1[0].split(":")[0]) * 3600
        + int(s1[0].split(":")[1]) * 60
        + int(s1[0].split(":")[2])
        + float(s1[1]) * 0.001
    )
    # 計算結束時間的總秒數
    end = (
        int(s2[0].split(":")[0]) * 3600
        + int(s2[0].split(":")[1]) * 60
        + int(s2[0].split(":")[2])
        + float(s2[1]) * 0.001
    )
    return [start, end]  # 回傳開始時間與結束時間的串列


f = open("oxxostudio.srt", "r")  # 使用 open 方法的 r 開啟字幕檔案
srt = f.read()  # 讀取字幕檔案內容
f.close()  # 關閉檔案
srt_list = srt.split("\n")  # 將內容根據換行符號 \n 拆分成串列
sec = 1  # 串列中秒數從第二項開始 ( 串列的第二項的索引值為 1 )
text = 2  # 串列中文字內容從第三項開始 ( 串列的第三項的索引值為 2 )
sec_list = [[0, 0]]  # 定義時間串列的開頭為 [0,0]
text_list = [""]  # 定義字幕內容串列的開頭為空字串 ''
# 使用迴圈，讀取字幕檔案串列的每個項目
for i in range(len(srt_list)):
    if i == sec:
        sec = sec + 4  # 如果遇到時間內容，就將 sec + 4 ( 因為時間每隔 4 個項目會出現 )
        # 如果兩個串列項目內容前後對不上 ( 前一個結束時間不等於後一個的開始時間 )
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            # 在時間串列中間添加一個開始時間與結束時間內容 ( 表示該區間沒有字幕 )
            sec_list.append([sec_list[-1][1], time2sec(srt_list[i])[0]])
            # 在文字串列中間添加一個空字串 ( 表示該區間沒有字幕 )
            text_list.append("")
        sec_list.append(time2sec(srt_list[i]))  # 添加時間到時間串列
    if i == text:
        text = text + 4  # 如果遇到文字內容，就將 text + 4 ( 因為文字每隔 4 個項目會出現 )
        text_list.append(srt_list[i])  # 添加文字到文字串列

print(sec_list)
print(text_list)


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw


def time2sec(t):
    arr = t.split(" --> ")
    s1 = arr[0].split(",")
    s2 = arr[1].split(",")
    start = (
        int(s1[0].split(":")[0]) * 3600
        + int(s1[0].split(":")[1]) * 60
        + int(s1[0].split(":")[2])
        + float(s1[1]) * 0.001
    )
    end = (
        int(s2[0].split(":")[0]) * 3600
        + int(s2[0].split(":")[1]) * 60
        + int(s2[0].split(":")[2])
        + float(s2[1]) * 0.001
    )
    return [start, end]


f = open("oxxostudio.srt", "r")
srt = f.read()
f.close()
srt_list = srt.split("\n")
# print(text_list)
sec = 1
text = 2
srt_list = [[0, 0]]
text_list = [""]
for i in range(len(srt_list)):
    if i == sec:
        sec = sec + 4
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            sec_list.append([sec_list[-1][1], time2sec(srt_list[i])[0]])
            text_list.append("")
        sec_list.append(time2sec(srt_list[i]))
    if i == text:
        text = text + 4
        text_list.append(srt_list[i])

print(sec_list)
print(text_list)

img_empty = Image.new("RGBA", (480, 240))  # 產生 RGBA 空圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 20)  # 設定文字字體和大小
video = VideoFileClip("baby_shark.mp4").resize((480, 240))  # 讀取影片，改變尺寸
video_duration = float(video.duration)  # 讀取影片總長度
output_list = []  # 記錄最後要組合的影片片段

# 如果字幕最後的時間小於總長度
if sec_list[-1][1] != video_duration:
    sec_list.append([sec_list[-1][1], video_duration])  # 添加時間到時間串列
    text_list.append("")  # 添加空字串到文字串列


# 建立文字字卡函式
def text_clip(text, name):
    img = img_empty.copy()  # 複製空圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件，並寫入文字
    text_width = 21 * len(text)  # 在 480x240 文字大小 20 狀態下，一個中文字長度約 21px
    draw.text(
        ((480 - text_width) / 2, 10),
        text,
        fill=(255, 255, 255),
        font=font,
        stroke_width=2,
        stroke_fill="black",
    )
    img.save(name)  # 儲存


# 建立影片和文字合併的函式
def text_in_video(t, text_img):
    clip = video.subclip(t[0], t[1])  # 剪輯影片到指定長度
    text = ImageClip(text_img, transparent=True).set_duration(
        t[1] - t[0]
    )  # 讀取字卡，調整為影片長度
    combine_clip = CompositeVideoClip([clip, text])  # 合併影片和文字
    output_list.append(combine_clip)  # 添加到影片片段裡


# 使用 for 迴圈，產生文字字卡
for i in range(len(text_list)):
    text_clip(text_list[i], "srt.png")
    text_in_video(sec_list[i], "srt.png")

output = concatenate_videoclips(output_list)  # 合併所有影片片段
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip(video_filename)
frame = video.save_frame("tmp_frame1.jpg", t=22)
frame = video.save_frame("tmp_frame2.jpg", t=22.1)
frame = video.save_frame("tmp_frame3.jpg", t=22.2)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

img_clip = ImageClip("oxxostudio.jpg", transparent=True).set_duration(2)
img_clip.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

img1 = ImageClip("oxxo1.jpg", transparent=True).set_duration(3)
img2 = (
    ImageClip("oxxo2.jpg", transparent=True).set_duration(4).set_start(2).crossfadein(1)
)
img3 = (
    ImageClip("oxxo3.jpg", transparent=True).set_duration(3).set_start(5).crossfadein(1)
)

output = CompositeVideoClip([img1, img2, img3])

output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")

print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.gif")
video.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

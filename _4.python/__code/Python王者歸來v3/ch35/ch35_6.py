# ch35_6.py
from moviepy.editor import VideoFileClip

clip = VideoFileClip("short南極企鵝.mp4")
audio = clip.audio
audio.write_audiofile("out35_6_企鵝聲音.mp3")



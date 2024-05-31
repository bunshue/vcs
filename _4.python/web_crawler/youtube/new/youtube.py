from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

video_url = "https://www.youtube.com/watch?v=IrwxueGgRYs"
save_dir = "C:/_git/vcs/_4.python/__code/techwithtim/Python-Beginner-Automation-Projects-main"

print("Started download...")
download_video(video_url, save_dir)

print("Started download... OK")
   

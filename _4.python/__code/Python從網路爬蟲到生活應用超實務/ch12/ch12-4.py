from image_downloader.image_downloader import download_csv_file_images
from apscheduler.schedulers.blocking import BlockingScheduler

csvfile = "ptt_beauty.csv"

def task(file):
    download_csv_file_images(file)

scheduler = BlockingScheduler() 
run_date = "2020-9-6 14:40:00"
scheduler.add_job(task, "date", run_date=run_date, args=[csvfile])
print("自動排程在", run_date, "下載 ", csvfile, " 的圖檔...")
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 
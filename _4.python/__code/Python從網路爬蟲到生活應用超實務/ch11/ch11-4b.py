from image_downloader.image_downloader import download_csv_file_images
import pandas as pd

df = pd.read_csv("imgur_dog.csv")
print(df.head())
df.columns = ["imgur-src"]
df.to_csv("imgur_dog2.csv",index=False)

download_csv_file_images("imgur_dog2.csv")

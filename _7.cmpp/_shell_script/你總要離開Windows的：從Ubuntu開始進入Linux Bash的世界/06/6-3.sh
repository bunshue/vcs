#範例指令稿6-3.sh  掛載後目錄中內容的變化
#! /bin/bash

echo 檢視目的目錄 /home/media中的內容
echo 裝置掛載
sudo mount /dev/sda7 /home/media

echo掛載結束
echo 檢視掛載後的目錄檔案
ls -l /home/media

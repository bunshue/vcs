#範例指令稿6-2.sh  裝置的掛載
#! /bin/bash

echo 使用mount指令掛在硬碟/dev/sda7到目錄 /home/media
sudo mount /dev/sda7 /home/media

echo掛載結束
echo 檢視掛載後的目錄檔案
ls -l /home/media

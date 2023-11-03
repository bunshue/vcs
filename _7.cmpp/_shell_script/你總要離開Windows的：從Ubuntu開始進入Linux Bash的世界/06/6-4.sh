#範例指令稿6-4.sh  裝置的移除
#! /bin/bash

echo 檢視掛載後的目錄檔案
ls -l /home/media

echo 裝置移除
sudo umount /dev/sda7 /home/media

echo移除結束

echo 檢視移除後的目錄檔案
ls -l /home/media

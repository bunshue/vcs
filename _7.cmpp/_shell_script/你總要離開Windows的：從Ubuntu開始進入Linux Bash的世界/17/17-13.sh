#範例指令稿17-13.sh  使用tar備份日志
#! /bin/bash

echo進入日志目錄
cd /var/log

echo對記錄檔進行打包
tar -cvf * log.tar
ls -l | grep log.tar
echo

echo搬移記錄檔到備份目錄
sudo mv log.tar /home
sudo rm log.tar

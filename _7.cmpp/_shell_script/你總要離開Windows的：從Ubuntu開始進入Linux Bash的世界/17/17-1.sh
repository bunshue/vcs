#範例指令稿17-1.sh  顯示CPU資源訊息
#! /bin/bash

echo 顯示CPU閒置比例
idle=`top -b -n 1 | grep Cpu | gawk '{print $5}' | cut -f 1 -d "."`
echo CPU目前的閒置比例為$idle

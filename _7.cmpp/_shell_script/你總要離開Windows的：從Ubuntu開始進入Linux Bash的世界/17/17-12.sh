#範例指令稿17-12.sh  顯示記錄檔
#! /bin/bash

cd /var/log
echo 顯示所有系統記錄檔
ls  | grep syslog

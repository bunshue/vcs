#範例指令稿17-14.sh  日志的定時動作
#! /bin/bash

echo 在午夜進行日志的備份動作
at -f 17-11.sh midnight

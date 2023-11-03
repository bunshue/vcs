#案例指令稿17-6.sh   使用時間增量
#! /bin/bash

echo使用時間增量完成工作的設定
at  -f 17-4.sh  midnight +2 hours
echo

at  -f 17-4.sh teatime + 2hours

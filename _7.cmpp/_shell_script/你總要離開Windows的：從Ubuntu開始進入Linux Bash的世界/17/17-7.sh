#案例指令稿17-7.sh   指定工作佇列
#! /bin/bash

echo 使用-q選型指定工作佇列
at  -f 17-4.sh  midnight +2 hours -q b

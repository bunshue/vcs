#範例指令稿11-7.sh  屏蔽特殊字元
#! /bin/bash

grep "*\$*" 11-7.sh
echo

echo '不使用反斜槓比對$'
grep "*$*" 11-7.sh

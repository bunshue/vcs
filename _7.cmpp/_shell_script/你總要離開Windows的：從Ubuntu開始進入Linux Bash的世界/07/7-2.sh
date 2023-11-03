#範例指令稿7-2.sh指令“[]”的使用
#! /bin/bash

echo 使用[] 代替test指令進行算術運算
[ 3 -le 5 ]
echo "[ 3 -le 5 ] :$?"

[ 5 -le 3 ]
echo "[ 5 -le 3 ]:$?"

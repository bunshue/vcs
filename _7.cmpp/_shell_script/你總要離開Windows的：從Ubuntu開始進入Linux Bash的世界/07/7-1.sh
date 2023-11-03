#範例指令稿7-1.sh指令test的使用
#! /bin/bash

echo 使用test指令進行算術運算
test 3 -le 5
echo "3 -le 5 :$?"

test 5 -le 3
echo "5 -le 3:$?"

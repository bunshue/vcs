#範例指令稿5-4.sh 通配符星號*的使用
#! /bin/bash

echo 使用通配符星號\"*\"
mkdir file1 filE2 fiLE3 fILE4 FILE5

echo 只使用1個字元f
ls f*

echo 使用2個字元fi
ls fi*

echo 使用3個字元fil
ls fil*

echo 使用4個字元fiile
ls 'file*'

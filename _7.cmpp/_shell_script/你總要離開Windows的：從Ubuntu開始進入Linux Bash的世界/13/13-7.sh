#範例指令稿13-7.sh  使用多行指令
#! /bin/bash
sed '
> N
> /this\nis/d
> ' data.txt

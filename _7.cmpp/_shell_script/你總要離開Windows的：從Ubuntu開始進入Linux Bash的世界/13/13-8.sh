#範例指令稿13-8.sh  使用多行指令
#! /bin/bash

sed -n '/b/{
> h
> p
> n
> p
> g
> p
> }' data.txt

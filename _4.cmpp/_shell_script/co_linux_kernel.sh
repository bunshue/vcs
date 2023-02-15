#!/bin/bash
DIR="linux-2.6.12"
echo Update Linux kernel ST
cd $DIR
svn up -r $1
cd ..

echo Update Linux kernel SP and tar Linux kernel ST.
tar cjvBpf linux.$1.tar.bz2 $DIR
echo Tar Linux kernel SP. Tar-file is linux.$1.tar.bz2


#範例指令稿17-2.sh  監控指令稿範例
#! /bin/bash

echo 取得剩余交換空間
swap_free=`free -m | grep Swap | gawk '{print $4}'`
if (( swap_free < 15 ))
then
    echo 交換空間剩余不足
  fi
echo 交換空間還剩$swap_free
echo

echo 取得剩余普通記憶體空間
mem_free=`free -m | grep Mem | gawk '{print $4}'`
if (( mem_free < 15 ))
then
    echo 記憶體空間剩余不足
fi
echo 記憶體空間還剩$mem_free
echo

echo 取得剩余硬碟空間
diska_free=`df -h | grep /dev/sda6 | awk '{print $5}' | cut -f 1 -d "%"`
if ((diska_free < 15 ))
then
    echo "磁碟/dev/sda6空間剩余不足"
fi
echo "磁碟/dev/sda$i 的剩余空間為$diska_free"

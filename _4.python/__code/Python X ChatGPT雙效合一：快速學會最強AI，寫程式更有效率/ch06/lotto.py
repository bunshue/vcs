number={1,2,3,4,5,6,7,8,9,10,11,12}
print(number)
lotto1={3,5,7,10,12} #第一組幸運彩蛋
print("第一組樂透:",lotto1)
lotto2={2,5,6,11,12} #第二組幸運彩蛋
print("第二組樂透:",lotto2)
lucky=lotto1 | lotto2
print("有 %d 個數字出現在其中一次開獎" %len(lucky), lucky)
biglucky=lotto1 & lotto2
print("有 %d 個數字出現在每一次開獎" %len(biglucky), biglucky)
badnum=number -lucky
print("總共有 %d 個不幸運的數字" %len(badnum), badnum)

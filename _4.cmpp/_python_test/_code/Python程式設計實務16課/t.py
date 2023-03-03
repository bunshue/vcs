# _*_ coding: utf-8 _*_

age = input("請輸入你的年紀：")
with_parent = raw_input("和父母一起來嗎？(Y/N)")

if age >= 18:
  print "可以看限制級電影"
elif age >=12:
  print "可以看輔導級電影"
elif (age >= 6 and age < 12) and (with_parent=='Y' or with_parent=='y'):
  print "可以看保護級電影"
else:
  print "只能看普遍級電影"


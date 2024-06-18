import sys

print("------------------------------------------------------------")  # 60個

#chap5-06c
#引入自訂模組handgame.py，別名hg
import handgame as hg
#使用hand()自訂函式
computer=hg.hand()
#產生選項文字
hgs=""
for i in range(0,len(hg.handgesture)):
  hgs=hgs+str(i)+hg.handgesture[i]
#使用者輸入選項
yourchoice=int(input("請輸入你的選擇"+hgs+": "))
#使用自訂模組中的handgesture串列
you=hg.handgesture[yourchoice]
print("You:",you,"Computer:",computer)
#電腦獲勝的條件
if (computer=="剪刀" and you=="布") or (computer=="布" and you=="石頭") or (computer=="石頭" and you=="剪刀"):
  print("電腦獲勝")
#平手的條件
elif computer==you:
  print("平手")
#剩下的都是遊戲者獲勝
else:
  print("你獲勝")


print("------------------------------------------------------------")  # 60個

#chap5-06d
#引入自訂套件games(/content/games資料夾)
import games
for i in range(3):
  print(games.dice.dice())
  print(games.hand.hand())
  print(games.poker.poker())
  print(games.coin.coin())
  print("-------")

print("------------------------------------------------------------")  # 60個

#chap5-06e
#改寫成 from ... import
from games import dice,hand,poker,coin
for i in range(3):
  print(dice.dice())
  print(hand.hand())
  print(poker.poker())
  print(coin.coin())
  print("-------")


print("------------------------------------------------------------")  # 60個

#chap5-06g
#引入handgames.py當成自訂模組
import handgames
handgames.handgame()

print("------------------------------------------------------------")  # 60個

#chap5-06h
#產生cmdlineargs.py檔案
file1=open("cmdlineargs.py","w") #打開檔案，建立cmdlineargs.py
file1.write("import sys\n") 
file1.write("for arg in sys.argv:\n") 
file1.write("\tprint(arg)\n") 
file1.close() #關閉檔案

#!python cmdlineargs.py 1 2 3


print("------------------------------------------------------------")  # 60個

#chap5-06i
file1=open("multiply.py","w") #打開檔案，建立multiply.py
file1.write("import sys\n") 
file1.write("if len(sys.argv)>=3:\n") 
file1.write("\tprint(int(sys.argv[1])*int(sys.argv[2]))\n") 
file1.write("else:\n") 
file1.write("\tprint('參數不足')\n") 
file1.close() #關閉檔案
#!python multiply.py
#!python multiply.py 8 9 
#!python multiply.py 5 9 

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



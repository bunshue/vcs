import handgame as hg


def handgame():
    computer = hg.hand()
    hgs = ""
    for i in range(0, len(hg.handgesture)):
        hgs = hgs + str(i) + hg.handgesture[i]
    yourchoice = int(input("請輸入你的選擇" + hgs + ": "))
    you = hg.handgesture[yourchoice]
    print("You:", you, "Computer:", computer)
    if (
        (computer == "剪刀" and you == "布")
        or (computer == "布" and you == "石頭")
        or (computer == "石頭" and you == "剪刀")
    ):
        print("電腦獲勝")
    elif computer == you:
        print("平手")
    else:
        print("你獲勝")


if __name__ == "__main__":
    for i in range(3):
        handgame()
else:
    print("被import使用中")

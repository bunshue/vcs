import random

bossHp=100
listPcCard=[["青眼白龍",20],["紅髮女妖",11],["白骷髏王",9],["碧眼狐怪",12]]
random.shuffle(listPcCard)
dictMyCard=dict(listPcCard)

while True:
    n = int(input("功能選項：1.抽卡攻擊 2.補齊卡牌 3.目前卡牌 4.離開遊戲："))
    if n==1:
        if not dictMyCard: 
            print("目前沒有卡牌，請補卡牌")
            continue
        card=dictMyCard.popitem()
        listCard=list(card)
        cardName=listCard[0]
        cardAttack=listCard[1]
        bossHp-=cardAttack  
        if bossHp<=0:
            bossHp=0
            print("%s最後一擊 %d 點\t魔王血量歸 %d，成功過關"
                    %(cardName, cardAttack, bossHp))
            break
        print("使用%s攻擊 %d 點\t魔王目前血量：%d"
              %(cardName, cardAttack, bossHp))
    elif n==2:
        random.shuffle(listPcCard)
        dictMyCard=dict(listPcCard)
        print("完成補齊卡牌!")
    elif n==3:
        print("目前卡牌：", dictMyCard)
    elif n==4:
        break
    else:
        print("無此選項功能!")

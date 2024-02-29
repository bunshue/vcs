import random

# 遊戲設定
player_hp = 100
enemy_hp = 100
score = 0

# 遊戲主迴圈
while True:
    # 顯示遊戲狀態
    print(f"你的血量: {player_hp}")
    print(f"敵人的血量: {enemy_hp}")
    print(f"得分: {score}")
    print("")
    
    # 玩家選擇行動
    print("請選擇行動:")
    print("1. 射擊敵人")
    print("2. 治療自己")
    choice = input()
    print("")
    
    # 玩家射擊敵人
    if choice == "1":
        damage = random.randint(10, 20)
        enemy_hp -= damage
        score += 10
        print(f"你對敵人造成了 {damage} 點傷害!")
        print("")
        
        # 檢查敵人是否死亡
        if enemy_hp <= 0:
            print("你打敗了敵人!")
            break
        
        # 敵人攻擊
        damage = random.randint(5, 15)
        player_hp -= damage
        print(f"敵人對你造成了 {damage} 點傷害!")
        print("")
        
        # 檢查玩家是否死亡
        if player_hp <= 0:
            print("你死了!")
            break
    
    # 玩家治療自己
    elif choice == "2":
        heal = random.randint(10, 20)
        player_hp += heal
        print(f"你回復了 {heal} 點生命!")
        print("")
        
        # 敵人攻擊
        damage = random.randint(5, 15)
        player_hp -= damage
        print(f"敵人對你造成了 {damage} 點傷害!")
        print("")
        
        # 檢查玩家是否死亡
        if player_hp <= 0:
            print("你死了!")
            break
    
    # 無效行動
    else:
        print("請選擇有效的行動!")
        print("")

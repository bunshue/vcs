age = 45  # 客人年齡
has_loyalty_card = True  # 客人是否有集點卡
movies_watched = 6  # 客人看過的電影數量

if age < 18:
    print('未滿 18 歲不能觀賞此部電影')
elif 18 <= age < 59:
    if has_loyalty_card and movies_watched >= 5:
        print('票價為 200 元')
    else:
        print('票價為 400 元')
else:  # 60 歲以上的客人
    if has_loyalty_card and movies_watched >= 5:
        print('票價為 200 元')
    else:
        print('票價為 200 元')  # 60 歲以上的客人票價都是 200 元，無論是否有集點卡

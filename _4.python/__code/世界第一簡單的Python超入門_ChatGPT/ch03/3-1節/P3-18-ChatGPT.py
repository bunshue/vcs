age = 45
has_loyalty_card = True
movies_watched = 6

if age < 18:
    print('未滿 18 歲不能觀賞此部電影')
elif (18 <= age < 59 and not (has_loyalty_card and movies_watched >= 5)) or (age >= 59 and not has_loyalty_card):
    print('票價為 400 元')
else:
    print('票價為 200 元')







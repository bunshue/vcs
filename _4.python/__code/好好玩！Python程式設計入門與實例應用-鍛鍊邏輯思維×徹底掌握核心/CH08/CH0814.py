import wordcloud   # 滙入詞雲

word = '''we programmed the computer to make
decisions based on conditions. In this chapter, we’ll
program the computer to pick a number between 1
and 10, to play Rock-Paper-Scissors, and even to roll
dice or pick a card!'''

# 1.建立詞雲物件，背景為黑色
sample = wordcloud.WordCloud(background_color = 'Black')
# 2. 詞雲裡放入文字資料
sample.generate(word)
# 3. 產生詞雲圖片
sample.to_file('fun.png')
